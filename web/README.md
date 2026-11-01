# Searchable MatVerse UI

The public directory is at https://usccolumbia.github.io/matverse/. The generated root `index.html` is self-contained and can also be opened directly from disk. It does not fetch catalog data, fonts or scripts from an external service.

Source files:

- `index.template.html`: semantic document and controls.
- `styles.css`: responsive teal/lime directory design inspired by the provided screenshot.
- `app.js`: search, combined filters, sorting, dataset details, resource search, URL state and CSV/JSON export.

After editing catalog data or UI sources:

```sh
python3 scripts/build_catalog.py
python3 scripts/build_sources.py
python3 scripts/build_site.py
node --test tests/ui.test.cjs
```

CI checks that all generated files match their sources. The root `.nojekyll` file permits direct static publication from the `main` branch on GitHub Pages. Catalog data remains authoritative in `data/datasets.json` and `data/resources.json`; the HTML embeds a generated copy. `data/ui_manifest.json` records the source and output hashes.

Search uses all words (AND), ignores case and dash variants, and supports quoted phrases. Filters combine with search. Numeric sort keeps unknown sizes last; the initial sort groups categories and orders each by descending size. The types tab groups the selected count unit rather than asserting that every row has the same kind of data. Exact counted units remain visible.

Search/filter state can be shared via URL parameters; `#dataset-id` opens a release's source details. Press `/` to focus search. All primary source links open separately. “Terms documented” includes restrictive or commercial terms, and must not be interpreted as an open license.
