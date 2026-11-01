"""Regression checks for legacy descriptors and multi-release paper mappings."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from scientific_data_survey import descriptor_dois


class ScientificDataIndexTests(unittest.TestCase):
    def test_legacy_article_url_and_doi_are_equivalent(self):
        expected = {'10.1038/sdata.2015.9'}
        self.assertEqual(descriptor_dois('https://www.nature.com/articles/sdata20159'), expected)
        self.assertEqual(descriptor_dois('https://doi.org/10.1038/sdata.2015.9'), expected)
        self.assertEqual(descriptor_dois('https://doi.org/10.1038%2Fsdata.2015.9'), expected)

    def test_generated_index_preserves_old_papers_and_shared_descriptor(self):
        index = json.loads((ROOT / 'data/scientific_data_index.json').read_text())
        mapping = {d['doi']: set(d['catalog_ids']) for d in index['descriptors']}
        ids = set().union(*mapping.values())
        for dataset_id in ['mp-elastic-2015', 'mp-piezo-2015', 'mp-dfpt-phonons-2018']:
            self.assertIn(dataset_id, ids)
        self.assertTrue({'3dsc-mp', '3dsc-icsd'} <= mapping['10.1038/s41597-023-02721-y'])

    def test_journal_years_do_not_truncate_three_digit_doi_segments(self):
        rows = {d['id']: d for d in json.loads((ROOT / 'data/datasets.json').read_text())}
        self.assertEqual(rows['predicted-high-dielectric-oxides']['year'], 2020)
        self.assertEqual(rows['cde-stress-strain-2024']['year'], 2024)
        self.assertEqual(rows['solgel-phase-purity-2026']['year'], 2026)

    def test_complete_metadata_harvest_and_title_screen_reconcile(self):
        folder = ROOT / 'research/sdata_20261101'
        receipt = json.loads((folder / 'journal_harvest_receipts.json').read_text())
        works = json.loads((folder / 'journal_works.json').read_text())
        candidates = json.loads((folder / 'journal_candidates.json').read_text())
        self.assertTrue(receipt['complete'])
        self.assertEqual(len({w['doi'] for w in works}), receipt['total_reported'])
        self.assertEqual(sum(p['returned'] for p in receipt['pages']), len(works))
        self.assertEqual(len(candidates), receipt['title_candidates'])
        self.assertTrue({w['doi'] for w in candidates} <= {w['doi'] for w in works})


if __name__ == '__main__':
    unittest.main()
