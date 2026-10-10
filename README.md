# Lean · KVP · Kaizen – interaktive Lern-Werkzeuge

Kostenlose, interaktive Werkzeuge zum Lernen und Üben von Lean-Methoden, kontinuierlichem Verbesserungsprozess (KVP) und Kaizen.
Jedes Werkzeug ist **eine einzige HTML-Datei**: im Browser öffnen, fertig. Es braucht keine Installation und kein Konto, und es läuft auch offline.

**▶ Online öffnen:** https://ipbaz.github.io/lean-kvp-kaizen-tools/

## Werkzeuge

| Werkzeug | Inhalt | Online |
|---|---|---|
| **Kanban-Regelkreisläufe simulieren** | Pull-Simulation eines Leveling-Withdraw-Kanban (Heijunka): Entnahme → Lot-Post → Chute → 4 Stationen (One-Piece-Flow) → Loading cart → Versand | [öffnen](https://ipbaz.github.io/lean-kvp-kaizen-tools/kanban-regelkreislauf.html) |

Weitere Werkzeuge folgen.

### Kanban-Regelkreisläufe – Funktionen

- Schritt-für-Schritt-Simulation mit Live-Erklärung auf Deutsch
- Animierte Szene „Fabrik live“: Werker, Rüstwechsel, Loading cart, LKW, Fehlmengen-Alarm
- **✨ Optimieren:** findet automatisch die kleinste Kanban-Anzahl mit 0 Fehlmengen (optional auch die Losgröße)
- **📄 PDF-Bericht** für Führungskräfte und Kunden mit wählbaren Inhalten: Management-Zusammenfassung mit Ampel, Kennzahlen, Bestandsverlauf, Empfehlung, Glossar
- Palettengröße frei wählbar oder an die Losgröße gekoppelt
- Bereiche per Drag & Drop anordnen, schwebender Mini-Player
- Simulationen speichern und laden, Export als Markdown, JSON oder Obsidian-Notiz

## Nutzung

- **Online:** Link oben öffnen.
- **Offline:** `kanban-regelkreislauf.html` herunterladen und per Doppelklick im Browser öffnen (Chrome, Edge, Firefox oder Safari).
- **PDF-Bericht:** Button „📄 Bericht (PDF)“ → Inhalte auswählen → im Druckdialog „Als PDF sichern“. Die beste Darstellung liefern Chrome und Edge.

## Herkunft, Urheberschaft & Genehmigung

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
- Animierte Fabrik-Szene mit Cartoon-Illustrationen, Live-Erzählung auf Deutsch, 7-Schritte-Ablaufleiste
- PDF-Bericht mit wählbaren Abschnitten
- Drag & Drop der Bereiche, Mini-Player; die Seite bleibt während der Wiedergabe scrollbar

## Lizenz

Für dieses Repository gibt es **keine Open-Source-Lizenz**. Die Rechte am Original-Tool liegen bei John Naska (mokka.solutions).
Die Nutzung zum Lernen ist ausdrücklich erwünscht. Wer das Tool weiterentwickeln oder weitergeben möchte, nennt bitte die Herkunftskette: Video → John Naska (mokka.solutions) → diese Fassung (Milad Karami), jeweils mit Datum und einer kurzen Beschreibung der eigenen Änderungen.
