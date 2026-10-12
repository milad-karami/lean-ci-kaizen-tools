# step-analyse.html – change log (Toolkit bug fixes)

| # | Bug | Cause | Fix | Verified |
|---|-----|-------|-----|----------|
| 1 | Markdown/Obsidian export could not be imported again as soon as any text contained `-->` (import threw *Unterminated string in JSON*). | The full state is stored in an HTML comment `<!-- tool-state: … -->`; a user `-->` ended the comment early. | `stateComment()` writes `-->` as `-->` (valid JSON, decodes to the same text). | Stress round trip: original throws for Markdown and Obsidian, fixed version round-trips exactly. |
| 2 | Obsidian mind map showed only `+` / `-` instead of the factor name for chances/risks. | In Mermaid mind maps `Text (+)` is node-shape syntax; the bracket content replaces the label. | Suffix written as ` +` / ` -` without brackets. | Checked generated Mermaid block. |

No other bugs found. Note: this tool family (step/swot/sipoc/kano) has no »last opened« key; after a reload the default
template is shown and saved analyses are reachable via the dropdown. That is the original design and was left as is.

## What was tested (headless Chromium via Playwright, file://)

- Page load at 1280 px and 375 px: no console/page errors, no horizontal overflow, narrow layout checked visually.
- Every example from the template dropdown: `buildMarkdown()`, `buildJSON()`, `buildObsidian()` return content, and each export
  imported back (`importFromText`) gives the same state (only the template label differs, by design).
- Stress round trip: every free-text field filled with `| > --> " ` umlauts backticks `[[ ]] #`, and a second run with line breaks.
- Original file (`origin/main`) vs. fixed file with the same scripts, to confirm each bug and its fix.
- UI: switching templates via the dropdown, editing, draft restore after reload, »Speichern« → save dialog, autosave after 3 s,
  reopening the saved project after reload, discarding changes when switching, file import of all three formats via the file input.
- Click-through of every visible button for every example (no runtime errors), guided mode forward/back to »fertig«.
