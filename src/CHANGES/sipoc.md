# sipoc.html – change log (Toolkit bug fixes)

| # | Bug | Cause | Fix | Verified |
|---|-----|-------|-----|----------|
| 1 | A `\|` in any supplier/input/step/output/customer text broke the SIPOC table in the Markdown export (extra columns, shifted cells). | Cell texts were inserted unescaped. | Pipes in table cells are escaped as `\|`. | Original row `Vertrag \| unterschrieben` split into 6 cells; fixed output shows `Vertrag \| unterschrieben` in one cell; import still round-trips. |
| 2 | Markdown/Obsidian export could not be imported again when any text contained `-->` (JSON parse error). | State is kept in `<!-- tool-state: … -->`; a user `-->` ended the comment. | `>` in that JSON is written as `>` (valid JSON, same text after parsing). | Stress round trip: original throws, fixed version round-trips exactly. |

Also checked: all 9 phases forward/back via buttons and stepper (normal and guided mode). No »last opened« key in this
tool family (original design, see step-analyse.md).

## What was tested (headless Chromium via Playwright, file://)

- Page load at 1280 px and 375 px: no console/page errors, no horizontal overflow, narrow layout checked visually.
- Every example from the template dropdown: `buildMarkdown()`, `buildJSON()`, `buildObsidian()` return content, and each export
  imported back (`importFromText`) gives the same state (only the template label differs, by design).
- Stress round trip: every free-text field filled with `| > --> " ` umlauts backticks `[[ ]] #`, and a second run with line breaks.
- Original file (`origin/main`) vs. fixed file with the same scripts, to confirm each bug and its fix.
- UI: switching templates via the dropdown, editing, draft restore after reload, »Speichern« → save dialog, autosave after 3 s,
  reopening the saved project after reload, discarding changes when switching, file import of all three formats via the file input.
- Click-through of every visible button for every example (no runtime errors), guided mode forward/back to »fertig«.
