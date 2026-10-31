# Mathematics Notes

This repository contains the original LaTeX mathematics notes and the staged online textbook migration.

The active publishing tree is [book/](book/). The first complete migrated course is [Differential Calculus](book/differential-calculus/index.md). Original sources remain under [Sections/](Sections/) and [fizztex.sty](fizztex.sty).

Read [CONTRIBUTING.md](CONTRIBUTING.md) for local HTML/PDF builds and [MIGRATION_CHECKLIST.md](MIGRATION_CHECKLIST.md) for migrating later courses. The audit, figure inventory, style guide and overall roadmap are linked from [MIGRATION_PLAN.md](MIGRATION_PLAN.md).

The site is deployed automatically to GitHub Pages whenever changes are pushed to `master`. To preview edits locally on Windows, run:

```powershell
python -m venv prototypes/.venv
prototypes/.venv/Scripts/python -m pip install -r prototypes/requirements-lock.txt
powershell -ExecutionPolicy Bypass -File book/serve.ps1
```

Then open <http://127.0.0.1:8765/>. After changing a page, stop the server with `Ctrl+C`, rerun the command to rebuild, and refresh the browser. Use `-SkipBuild` when only restarting the server:

```powershell
powershell -ExecutionPolicy Bypass -File book/serve.ps1 -SkipBuild
```
