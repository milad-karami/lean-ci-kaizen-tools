# pdca.html – Änderungen (Toolkit)

Alle Fixes sind im Code mit `// FIX (Toolkit): …` markiert. Unverändert bleiben: IDs, Datenformat (`meta`, `kpi`, `cycles[]`, `cur`), localStorage-Schlüssel (`pdcaW1T3.v1.*`), Exportstruktur (inkl. `<!-- pdca-state v1 … -->`) und alle Credits (John Naska, mokka.solutions, Quellen).

**Hinweis aus dem Smoke-Test („EXAMPLES, aber kein `loadExample()`“):** Das ist kein Fehler. Die Beispiele werden über die Auswahl `#exampleSel` und `loadKey('ex:…')` geladen. Alle 4 Vorlagen (Leer, Produktion, Konditorei, Alltag) laden über das echte `change`-Event korrekt.

## Behobene Fehler

| # | Fehler | Ursache | Fix | Geprüft |
|---|---|---|---|---|
| 1 | Nach „Speichern“ (neues Vorhaben anlegen) oder einem Import öffnete das Tool beim nächsten Neuladen wieder die Vorlage „Produktion“ statt des gerade gespeicherten Vorhabens. Wer weiterarbeiten wollte, sah scheinbar seine Daten nicht mehr. | Beim Start liest das Tool `pdcaW1T3.v1.lastActive`. Diesen Schlüssel setzte nur `loadKey()`, nicht aber `doSaveAs()` und `applyImport()`, die `curKey` direkt umsetzen. Den Entwurf löscht `clearDirty()`, er griff also auch nicht. | Beide Funktionen schreiben `curKey` jetzt zusätzlich in `lastActive`. | Speichern als „Test“ → Neuladen: `curKey`, Inhalt und Auswahlfeld zeigen das Vorhaben (vorher `ex:produktion`). JSON-Export importiert → Neuladen: importiertes Vorhaben ist wieder offen. |
| 2 | Bei unveränderter Kennzahl stand im Soll-Ist-Vergleich „Zielerreichung **-0 %**“ (Richtung „Senken“). | `ist = −1 × (e − a)` ergibt −0, `toLocaleString` gibt „-0“ aus. | `fmtP` rechnet `+0`, sodass −0 zu 0 wird. | Ausgangswert = Ergebnis = 3,8 → „Zielerreichung 0 %“. Alle anderen Werte unverändert (50 %, 125 %, 83 %, 67 %, −50 %). |

## Was getestet wurde (headless Chromium über Playwright, `file://`)

- Laden ohne Konsolenfehler. Alle 4 Beispiele über `#exampleSel` geladen.
- **Soll-Ist-Rechnung geprüft** (Zielerreichung = erreichte ÷ geplante Veränderung, Vorzeichen nach Richtung):
  - Produktion D1: 4 → Ziel 3,6, Ergebnis 3,8 = 50 % „Teilerfolg“
  - Produktion D2: 3,8 → 3,6, Ergebnis 3,55 = 125 % „Ziel erreicht“
  - Konditorei: 8 → 2, Ergebnis 3 = 83 %
  - Alltag: 3 → 0, Ergebnis 1 = 67 %
  - Verschlechterung (4,2): −50 % mit Vorschlag „Verwerfen“
  - Ziel = Ausgangswert: Hinweis „Zielwert passt nicht zur Richtung“
  - %-Kennzahl wird in Prozentpunkten angezeigt
- `buildMarkdown()`, `buildJSON()` und `buildObsidian()` für jedes Beispiel ohne NaN/undefined. `importFromText()` aller drei Formate ergibt exakt den Stand.
- Export über die echten Menüpunkte (Download) und Re-Import der drei Dateien über `#importFile`: Stand identisch, neues Vorhaben angelegt. Eine fremde Datei zeigt „Kein PDCA-Stand in dieser Datei gefunden“.
- Durchläufe:
  - „Nächsten Durchlauf starten“ übernimmt das Ergebnis 3,55 als neuen Ausgangswert und den Standard-Text
  - Durchlauf entfernen und „Rückgängig“ funktionieren
  - Wechsel zwischen Durchläufen
- Karten: erledigt/offen umschalten, Entscheidung wählen (Karte A1 passt die Leitfragen an), Richtung umschalten.
- Speichern als Vorhaben, Auswahl wechseln und zurück ergibt einen identischen Stand.
- Geführter Modus Schritt 1–6 inklusive Kartennavigation (P1–P4, D1–D2, C1–C2, A1–A2), Abschlussübersicht und Sprung aus dem Bericht zu einer offenen Karte.
- 1400 px und 375 px: kein horizontaler Seiten-Scroll.

## Auffällig, aber nicht geändert

- `parseNum("1.500")` ergibt 1,5 (Punkt wird als Dezimaltrenner gelesen, „Komma und Punkt erlaubt“). Das ist so gewollt, kann bei Tausenderpunkten aber überraschen.
- Ist der Zielwert gleich dem Ausgangswert, lautet der Hinweis „Zielwert passt nicht zur Richtung“. Inhaltlich trifft das zu (keine geplante Veränderung), die Formulierung ist aber unscharf.
