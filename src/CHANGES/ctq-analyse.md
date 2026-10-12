# ctq-analyse.html – change log (Toolkit bug fixes)

CTQ uses the same project framework as five-forces, so fixes 1–5 are the same as there.

| # | Bug | Cause | Fix | Verified |
|---|-----|-------|-----|----------|
| 1 | After confirming »Trotzdem wechseln?« the newly opened template still counted as unsaved and the discarded draft stayed in storage. | `loadKey()` only re-painted the dirty dot. | `clearDirty()` when not silent. | Original: `dirty=true` + draft after switch; fixed: both cleared. |
| 2 | After »Speichern« (save as) the next start opened the template, not the saved analysis. | `doSaveAs()` did not set `K_LAST`. | Store `K_LAST`. | Reload reopens the saved project. |
| 3 | Same after importing a file. | Same in the import path. | Store `K_LAST`. | Reload after each import format reopens the imported project. |
| 4 | Loading from the »CTQ-Analysen« list discarded unsaved changes without asking. | No dirty check. | Same `confirm()` as the dropdown. | Cancel keeps, OK loads. |
| 5 | A restored draft was shown as saved and deleted – closing again lost the changes. | `init()` always ended with `clearDirty()`. | Keep it marked unsaved if it differs from its saved base. | Edit survives a second reload. |
| 6 | Switching from a project to a template kept the project's view settings (Kundendaten threshold, selected CTQ). | `loadKey()` reset `spec` only for projects; `loadExample()` does reset it. | Reset `spec` for templates in `loadKey()` too. | Threshold back to the default 80 after switching to a template. |
| 7 | Line breaks in the textareas (O-Ton, Bedürfnis, Treiber, Anforderung, CTQ-Merkmal, Messmethode) broke Markdown/Obsidian: on import the text after the break was lost, a requirement with a break disappeared **with all its CTQs**, and the matrix row broke. | Raw line breaks inside one-line Markdown structures (list items, table rows, `**…**`). | For these two exports line breaks are collapsed to spaces (`oneLine()` wrapper around `buildMarkdown`/`buildObsidian`; JSON keeps them; app state untouched). | Original: requirement + CTQs missing after import; fixed: full structure, texts with spaces instead of breaks. |
| 8 | A `[` in a CTQ metric (e.g. `Temperatur [°C]`) corrupted metric and unit on import. | The tree label `Merkmal [Einheit]` was re-split, the table columns were only used when the metric was empty. | Import takes metric and unit from the matrix table's own columns. | Stress round trip with `| > --> " [[ ]]` in every field now identical for all formats. |

Also checked: VoC suggestion → »übernehmen« writes USG/OSG into the matrix; all four step tabs; guided mode to »fertig«.

## What was tested (headless Chromium via Playwright, file://)

- Page load at 1280 px and 375 px: no console/page errors, no horizontal overflow, narrow layout checked visually.
- Every example from the template dropdown: `buildMarkdown()`, `buildJSON()`, `buildObsidian()` return content, and each export
  imported back (`importFromText`) gives the same state (only the template label differs, by design).
- Stress round trip: every free-text field filled with `| > --> " ` umlauts backticks `[[ ]] #`, and a second run with line breaks.
- Original file (`origin/main`) vs. fixed file with the same scripts, to confirm each bug and its fix.
- UI: switching templates via the dropdown, editing, draft restore after reload, »Speichern« → save dialog, autosave after 3 s,
  reopening the saved project after reload, discarding changes when switching, file import of all three formats via the file input.
- Click-through of every visible button for every example (no runtime errors), guided mode forward/back to »fertig«.
