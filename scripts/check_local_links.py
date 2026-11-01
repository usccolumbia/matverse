#!/usr/bin/env python3
"""Check repository Markdown file targets and explicit catalog anchors."""
import re
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
errors = []
checked = 0
for path in [ROOT / 'README.md', ROOT / 'CONTRIBUTING.md', *sorted((ROOT / 'docs').rglob('*.md'))]:
    body = path.read_text()
    for target in re.findall(r'\]\(([^)]+)\)', body):
        if urlparse(target).scheme or target.startswith('mailto:'):
            continue
        dest, _, anchor = target.partition('#')
        dest = unquote(dest)
        resolved = (path.parent / dest).resolve() if dest else path
        checked += 1
        if not resolved.exists():
            errors.append(f'{path.relative_to(ROOT)} -> {target}: missing file')
        elif anchor and resolved.suffix == '.md' and anchor.startswith(tuple(['aggregated-', 'bulk-', 'experimental-', 'mlip-', 'two-', 'porous-', 'molecular-', 'surfaces-', 'property-', 'generation-', 'diffraction-'])):
            if f'id="{anchor}"' not in resolved.read_text():
                errors.append(f'{path.relative_to(ROOT)} -> {target}: missing explicit category anchor')
        elif anchor and 'docs/catalog/' in str(resolved):
            if f'id="{anchor}"' not in resolved.read_text():
                errors.append(f'{path.relative_to(ROOT)} -> {target}: missing dataset anchor')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Checked {checked} local Markdown links.')
