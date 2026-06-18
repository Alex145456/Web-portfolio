## Goal
Fix images/pictures not showing in the Flet portfolio.

## Information Gathered
- `main.py` starts the app with `ft.app(..., assets_dir="assets")`.
- Asset references must point to the served assets path. Your GitHub images use `src=/assets/github/<file>`.
- Certificate page (`pages/matlab_hub.py`) uses `course["file"]` values like `certificates/Matlab Onramp.png` without the `/assets/` prefix.
- Likely broken URLs: `/certificates/...` or relative paths instead of `/assets/certificates/...`.

## Plan (code changes)
1. Edit `pages/matlab_hub.py`:
   - Add a helper like `asset_url(rel_path) -> str` that returns `f"/assets/{rel_path}"`.
   - When setting `file_url = course["file"]`, convert it to `file_url = asset_url(course["file"])`.
   - Use this converted `file_url` for:
     - `ft.Image(src=...)`
     - `ft.WebView(url=...)`
     - `ft.IconButton(url=...)`
     - any `endswith` extension checks (ensure they check the original rel path or the full URL consistently).
2. Run the app and verify:
   - Certificates images/PDF preview load.
   - GitHub evidence images still load (unchanged).

## Dependent Files to be edited
- `pages/matlab_hub.py`

## Followup steps
- Start the app and manually navigate to `/matlab` and one `/certificate/<id>` to confirm assets load.
- If still failing, check the browser/Flet network requests for the failing URL to confirm the final path base.

