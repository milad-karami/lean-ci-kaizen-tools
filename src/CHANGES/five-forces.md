# five-forces.html – change log (Toolkit bug fixes)

| # | Bug | Cause | Fix | Verified |
|---|-----|-------|-----|----------|
| 1 | After confirming »Trotzdem wechseln?« the newly opened template still counted as unsaved (dot on, the next switch and closing the tab asked again) and the discarded draft stayed in storage. | `loadKey()` only re-painted the dirty dot instead of clearing the state. | `loadKey()` calls `clearDirty()` when not silent. | Original: after switch `dirty=true`, draft present; fixed: both cleared, reload opens the chosen template. |
| 2 | After »Speichern« (save as) the tool reopened the template instead of the saved analysis on the next start. | `doSaveAs()` did not update the »last opened« key (`K_LAST`). | Store `K_LAST` after saving. | Original fails »saved project reopened after reload«, fixed passes. |
| 3 | Same for an imported file (import creates a project). | Same cause in the import path. | Store `K_LAST` after import. | Reload after importing Markdown/JSON/Obsidian reopens the imported project. |
| 4 | Loading an analysis from the »Analysen« list discarded unsaved changes without asking (the dropdown does ask). | No dirty check in the list handler. | Same `confirm()` as the dropdown. | Cancel keeps the current unsaved state, OK loads the project. |
| 5 | A restored draft (after closing with unsaved changes) was shown as saved and the draft was deleted – closing again lost the changes. | `init()` always ended with `clearDirty()`. | If the restored draft differs from its saved base, it stays marked unsaved (`markDirty()`). | Original: second reload loses the edit; fixed: edit survives and stays marked unsaved. |
| 6 | Multi-line »Begründung« (textarea): only the first line was exported as quote and re-imported. | Line breaks were written raw after `> `. | Every line is prefixed with `> ` in Markdown and Obsidian; importer collects continuation lines. | Multi-line assessment round-trips through Markdown and Obsidian. |
| 7 | A driver with empty text (`- ↑`) was dropped on import, changing the force balance. | Import regex required text after the arrow. | Text after the arrow is optional. | Original: 4 drivers → 3 after re-import; fixed: 4 → 4. |
| 8 | Obsidian mind map showed only »hoch«/»mittel«/»niedrig« instead of the force name. | `Name [hoch]` is Mermaid node-shape syntax. | Written as `Name · hoch`. | Checked generated Mermaid block. |

## What was tested (headless Chromium via Playwright, file://)

- Page load at 1280 px and 375 px: no console/page errors, no horizontal overflow, narrow layout checked visually.
- Every example from the template dropdown: `buildMarkdown()`, `buildJSON()`, `buildObsidian()` return content, and each export
  imported back (`importFromText`) gives the same state (only the template label differs, by design).
- Stress round trip: every free-text field filled with `| > --> " ` umlauts backticks `[[ ]] #`, and a second run with line breaks.
- Original file (`origin/main`) vs. fixed file with the same scripts, to confirm each bug and its fix.
- UI: switching templates via the dropdown, editing, draft restore after reload, »Speichern« → save dialog, autosave after 3 s,
  reopening the saved project after reload, discarding changes when switching, file import of all three formats via the file input.
- Click-through of every visible button for every example (no runtime errors), guided mode forward/back to »fertig«.
