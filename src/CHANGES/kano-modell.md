# kano-modell.html – change log (Toolkit bug fixes)

| # | Bug | Cause | Fix | Verified |
|---|-----|-------|-----|----------|
| 1 | When a product or feature name contained `-->`, re-importing a Markdown/Obsidian export lost the individual answers: the tool fell back to the summary text and rebuilt answers from the distribution (different answer pairs). | Survey data is stored in `<!-- kano-data: … -->`; a user `-->` ended the comment. | `>` in that JSON is written as `>`. | Stress round trip: original changed several answer pairs (e.g. feature 4 `[2,2]` → `[4,0]`), fixed version identical. |

**Step navigation (smoke-test note »STEPS but no showStep()«):** works through the tool's own mechanism – `state.step`
plus `renderAll()`, driven by the stepper, `#btnBack` / `#btnNext` and the step numbers (`#wpos`). Verified 1 → 5 and back
to 1, with inputs, answers and the selected respondent preserved across step changes. No change needed.

**Open question (not changed):** the evaluation matrix `KANO` maps *Erwarte ich / Erwarte ich* and
*Kann ich tolerieren / Kann ich tolerieren* to **Q (fragwürdig)**. The common Kano evaluation table (Berger et al.)
has **I (indifferent)** there. None of the examples uses these pairs. Because it may follow the course material, the
author's matrix was left unchanged – please confirm.

No »last opened« key in this tool family (original design, see step-analyse.md).

## What was tested (headless Chromium via Playwright, file://)

- Page load at 1280 px and 375 px: no console/page errors, no horizontal overflow, narrow layout checked visually.
- Every example from the template dropdown: `buildMarkdown()`, `buildJSON()`, `buildObsidian()` return content, and each export
  imported back (`importFromText`) gives the same state (only the template label differs, by design).
- Stress round trip: every free-text field filled with `| > --> " ` umlauts backticks `[[ ]] #`, and a second run with line breaks.
- Original file (`origin/main`) vs. fixed file with the same scripts, to confirm each bug and its fix.
- UI: switching templates via the dropdown, editing, draft restore after reload, »Speichern« → save dialog, autosave after 3 s,
  reopening the saved project after reload, discarding changes when switching, file import of all three formats via the file input.
- Click-through of every visible button for every example (no runtime errors), guided mode forward/back to »fertig«.
