# MatVerse on MaterialsAtlas

MatVerse is integrated into the MaterialsAtlas Vue app catalog as **MatVerse Dataset Search**, under **Utilities & Tools**. It is a public, browser-based database app and does not submit computational jobs.

- Platform app: https://materialsatlas.org/apps/matverse
- Full-page directory: https://materialsatlas.org/matverse/index.html
- Example: https://materialsatlas.org/apps/matverse?q=superconductor

The platform hosts a copy of MatVerse's self-contained `index.html`. Search, filters, source details, API routes and CSV/JSON export run locally in the visitor's browser. Dataset download links retain their original providers, access requirements and licenses. The platform's existing app navigation, app search and workbench can discover the new catalog entry.

`MatVerseApp.vue` displays the locally hosted directory within the platform workspace using a slim toolbar and a compact embedded layout. The toolbar reuses the crystal logo with a dark teal MatVerse wordmark and DATASET ATLAS subtitle on the platform’s light background. The duplicate hero, overview cards and promotional sections are hidden only inside the platform frame; filters, source notes, record counts, details and export controls remain available. The results area fits the available viewport, with tighter row spacing. **Open full page** opens the current filter state in its own tab. Incoming MatVerse query parameters are forwarded from either the platform's clean route or its legacy hash route. The GitHub Pages directory remains independently available.

## Install or refresh

From the MatVerse repository, regenerate and validate the directory, then select the owning MaterialsAtlas source checkout explicitly:

```sh
python3 scripts/build_site.py --check
python3 integrations/materialsatlas/install.py --target /path/to/MToolbox2026 --check
python3 integrations/materialsatlas/install.py --target /path/to/MToolbox2026
```

The installer validates all source anchors before writing, supports repeat execution, and checks the MatVerse HTML against its UI manifest. It updates only:

- `backend_v2/app/catalog.py`: the public `matverse` app definition.
- `frontend_v2/src/App.vue`: async component routing and app icon.
- `frontend_v2/src/components/MatVerseApp.vue`: platform workspace integration.
- `frontend_v2/src/assets/images/matverse.png`: the existing MatVerse logo.
- `frontend_v2/public/matverse/index.html`: the generated directory snapshot.

Run the platform's TypeScript and production-build checks. Deploy through its existing frontend/backend image workflow after preserving the affected source, current image IDs, and an online SQLite backup. The app does not require worker changes, schema migrations, DNS changes or new credentials.

The mirror is a versioned snapshot. To publish catalog updates on MaterialsAtlas, rerun the installer with the newly generated MatVerse HTML and rebuild the frontend. GitHub Pages updates do not automatically refresh the platform mirror.
