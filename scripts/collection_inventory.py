"""Preserve every labeled link occurrence from the inspected collections."""
import hashlib
import json

SCOPES = {'crystal_related', 'adjacent', 'navigation', 'uncertain'}


def load_inventory(root):
    collections, entries = [], []
    for path in sorted((root / 'research').glob('collection_*.json')):
        if path.stem.endswith('_additions'):
            continue
        source = json.loads(path.read_text())
        if 'links' not in source:
            continue
        slug = path.stem.removeprefix('collection_')
        name = source.get('repository') or source.get('name') or slug
        url = source.get('url') or source.get('repository_url')
        collection_entries = []
        for position, link in enumerate(source['links'], 1):
            section = link.get('section', 'Not recorded')
            if isinstance(section, list):
                section = ' / '.join(section)
            scope = link.get('scope', 'uncertain')
            if scope not in SCOPES:
                raise ValueError(f'Unknown collection scope: {scope}')
            collection_entries.append({
                'id': f'{slug}-{position:03}', 'collection': slug,
                'collection_name': name, 'collection_url': url,
                'position': position, 'label': link.get('label') or link['url'],
                'url': link['url'], 'section': section, 'scope': scope,
            })
        entries.extend(collection_entries)
        collections.append({
            'id': slug, 'name': name, 'url': url,
            'revision': source.get('revision') or source.get('commit_sha') or source.get('commit'),
            'inventory_file': str(path.relative_to(root)),
            'inventory_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'entry_count': len(collection_entries),
            'unique_url_count': len({e['url'] for e in collection_entries}),
            'scope_counts': {s: sum(e['scope'] == s for e in collection_entries) for s in sorted(SCOPES)},
            'coverage_notes': source.get('coverage_notes', []),
        })
    return {'collections': collections, 'entries': entries,
            'entry_count': len(entries), 'unique_url_count': len({e['url'] for e in entries})}
