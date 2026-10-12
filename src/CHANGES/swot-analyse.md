# swot-analyse.html – change log (Toolkit bug fixes)

| # | Bug | Cause | Fix | Verified |
|---|-----|-------|-----|----------|
| 1 | Multi-line TOWS strategies (the strategy fields are textareas) lost everything after the first line when a Markdown or Obsidian export was imported again; a continuation line starting with `- [ ]` or `### SO` was even read as a new strategy / heading. | Strategies were written as `- [ ] text` with raw line breaks; the importer reads one line per strategy. | Export indents continuation lines by two spaces; the importer appends indented lines to the previous strategy. Existing single-line exports import unchanged. | Original: `"Zeile1\nZeile2\n  eingerückt"` → `"Zeile1"`; fixed: identical text for Markdown, Obsidian and JSON. |

Checked and **not** changed: object and S/W/O/T items are single-line `<input>` fields, so line breaks cannot occur there
from the UI. No »last opened« key in this tool family (original design, see step-analyse.md).

## What was tested (headless Chromium via Playwright, file://)

- Page load at 1280 px and 375 px: no console/page errors, no horizontal overflow, narrow layout checked visually.
- Every example from the template dropdown: `buildMarkdown()`, `buildJSON()`, `buildObsidian()` return content, and each export
  imported back (`importFromText`) gives the same state (only the template label differs, by design).
- Stress round trip: every free-text field filled with `| > --> " ` umlauts backticks `[[ ]] #`, and a second run with line breaks.
- Original file (`origin/main`) vs. fixed file with the same scripts, to confirm each bug and its fix.
- UI: switching templates via the dropdown, editing, draft restore after reload, »Speichern« → save dialog, autosave after 3 s,
  reopening the saved project after reload, discarding changes when switching, file import of all three formats via the file input.
- Click-through of every visible button for every example (no runtime errors), guided mode forward/back to »fertig«.
