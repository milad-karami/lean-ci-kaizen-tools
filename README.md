# Lean · KVP · Kaizen – interaktive Lern-Werkzeuge / interactive learning tools

**🇩🇪 [Deutsch](#deutsch) · 🇬🇧 [English](#english)**

**▶ Online:** https://milad-karami.github.io/lean-kvp-kaizen-tools/

| Werkzeug / Tool | 🇩🇪 Deutsch | 🇬🇧 English |
|---|---|---|
| **Kanban-Regelkreisläufe / Kanban control loops** | [öffnen](https://milad-karami.github.io/lean-kvp-kaizen-tools/kanban-regelkreislauf.html) | [open](https://milad-karami.github.io/lean-kvp-kaizen-tools/kanban-regelkreislauf-en.html) |

---

## Deutsch

Kostenlose, interaktive Werkzeuge zum Lernen und Üben von Lean-Methoden, kontinuierlichem Verbesserungsprozess (KVP) und Kaizen.
Jedes Werkzeug ist **eine einzige HTML-Datei**: im Browser öffnen, fertig. Es braucht keine Installation und kein Konto, und es läuft auch offline.

### Kanban-Regelkreisläufe – Funktionen

- Pull-Simulation eines Leveling-Withdraw-Kanban (Heijunka): Entnahme → Lot-Post → Chute → 4 Stationen (One-Piece-Flow) → Loading cart → Versand
- Schritt-für-Schritt-Simulation mit Live-Erklärung
- Animierte Szene „Fabrik live“: Werker, Rüstwechsel, Loading cart, LKW, Fehlmengen-Alarm
- **✨ Optimieren:** findet automatisch die kleinste Kanban-Anzahl mit 0 Fehlmengen (optional auch die Losgröße)
- **📄 PDF-Bericht** für Führungskräfte und Kunden mit wählbaren Inhalten: Management-Zusammenfassung mit Ampel, Kennzahlen, Bestandsverlauf, Empfehlung, Glossar
- Palettengröße frei wählbar oder an die Losgröße gekoppelt
- Bereiche per Drag & Drop anordnen, schwebender Mini-Player
- Simulationen speichern und laden, Export als Markdown, JSON oder Obsidian-Notiz

### Nutzung

- **Online:** Links oben öffnen.
- **Offline:** HTML-Datei herunterladen und per Doppelklick im Browser öffnen (Chrome, Edge, Firefox oder Safari).
- **PDF-Bericht:** Button „📄 Bericht (PDF)“ → Inhalte auswählen → im Druckdialog „Als PDF sichern“. Die beste Darstellung liefern Chrome und Edge.

### Herkunft, Urheberschaft & Genehmigung

- **Original-Tool:** John Naska, [mokka.solutions](https://www.mokka.solutions/). Aufbau, Simulationslogik und Oberfläche des Ursprungs-Tools stammen von ihm.
- **Fachliche Grundlage:** Erklärvideo [„Leveling withdraw Kanban“](https://www.youtube.com/watch?v=buD22g8wNWw). Das Video wird nur verlinkt, nicht eingebettet oder vervielfältigt. Die Rechte daran liegen bei den jeweiligen Urheberinnen und Urhebern.
- **Weiterentwicklung:** [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/), Oktober 2026.
- Die Veröffentlichung erfolgt **mit Genehmigung von John Naska**, unter Nennung seines Namens und mit Kennzeichnung der Änderungen.

### Änderungen gegenüber dem Original (09.10.2026)

- Logikfehler behoben:
  - Palettengröße wählbar statt fest 4
  - Linie läuft bei Lücken weiter
  - Verklemmungs-Erkennung, wenn die Kanban-Anzahl kleiner als die Losgröße ist
  - Fehlmengen-Urteil nur bei 0 Fehlmengen „grün“
  - Sicherheitsgrenze skaliert mit dem Bedarf
- Neue Funktion „✨ Optimieren“ (0 Fehlmengen bei minimaler Kanban-Anzahl)
- Animierte Fabrik-Szene mit Cartoon-Illustrationen, Live-Erzählung, 7-Schritte-Ablaufleiste
- PDF-Bericht mit wählbaren Abschnitten
- Drag & Drop der Bereiche, Mini-Player; die Seite bleibt während der Wiedergabe scrollbar
- Englische Fassung des Werkzeugs (10.10.2026)

### Lizenz

Für dieses Repository gibt es **keine Open-Source-Lizenz**. Die Rechte am Original-Tool liegen bei John Naska (mokka.solutions).
Die Nutzung zum Lernen ist ausdrücklich erwünscht. Wer das Tool weiterentwickeln oder weitergeben möchte, nennt bitte die Herkunftskette: Video → John Naska (mokka.solutions) → diese Fassung (Milad Karami), jeweils mit Datum und einer kurzen Beschreibung der eigenen Änderungen.

---

## English

Free, interactive tools for learning and practising Lean methods, continuous improvement (CI / KVP) and Kaizen.
Every tool is **a single HTML file**: open it in your browser and you're done. No installation, no account, and it also works offline.

### Kanban control loops – features

- Pull simulation of a leveling withdrawal kanban (Heijunka): withdrawal → lot size formation post → sequenced kanban chute → 4 stations (one-piece flow) → loading cart → shipping
- Step-by-step simulation with live explanations
- Animated “Factory live” scene: workers, changeovers, loading cart, truck, shortage alarm
- **✨ Optimize:** automatically finds the smallest number of kanban cards with zero shortages (optionally also the lot size)
- **📄 PDF report** for managers and customers, with selectable sections: management summary with traffic light, KPIs, inventory chart, recommendation, glossary
- Pallet size freely selectable or coupled to the lot size
- Rearrange sections via drag & drop, floating mini player
- Save and load simulations, export as Markdown, JSON or Obsidian note

### How to use

- **Online:** open the links above.
- **Offline:** download the HTML file and double-click it to open it in your browser (Chrome, Edge, Firefox or Safari).
- **PDF report:** click “📄 Report (PDF)” → select sections → choose “Save as PDF” in the print dialog. Chrome and Edge give the best result.

### Origin, authorship & permission

- **Original tool:** John Naska, [mokka.solutions](https://www.mokka.solutions/). The structure, simulation logic and interface of the original tool are his work.
- **Subject-matter basis:** explainer video [“Leveling withdraw Kanban”](https://www.youtube.com/watch?v=buD22g8wNWw). The video is only linked, not embedded or copied. All rights remain with its creators.
- **Further development:** [Milad Karami](https://www.linkedin.com/in/milad-karami-63075b78/), October 2026.
- Published **with the permission of John Naska**, crediting him by name and marking all changes.

### Changes compared to the original (2026-10-09)

- Logic bugs fixed:
  - pallet size selectable instead of a fixed 4
  - the line keeps flowing when there are gaps
  - deadlock detection when the number of kanban cards is smaller than the lot size
  - the shortage verdict is only “green” at zero shortages
  - the safety limit scales with demand
- New “✨ Optimize” function (zero shortages with the minimum number of kanban cards)
- Animated factory scene with cartoon illustrations, live narration, 7-step flow bar
- PDF report with selectable sections
- Drag & drop of sections, mini player; the page stays scrollable while playing
- English version of the tool (2026-10-10)

### License

This repository has **no open-source license**. All rights to the original tool remain with John Naska (mokka.solutions).
Using the tools for learning is explicitly welcome. If you develop the tool further or pass it on, please keep the chain of origin visible: video → John Naska (mokka.solutions) → this version (Milad Karami), each with the date and a short description of your own changes.
