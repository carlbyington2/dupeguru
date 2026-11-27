Duplikate neu priorisieren
==========================

dupeGuru versucht automatisch zu bestimmen, welches Duplikat in jeder Gruppe die
Referenzposition erhalten soll, liegt dabei aber manchmal falsch. In vielen Fällen genügt es,
die Duplikate geschickt mit den Optionen „Delta-Werte“ und „Nur Duplikate“ sowie der Aktion
„Ausgewählte zur Referenz machen“ zu sortieren, aber manchmal wird eine leistungsfähigere
Möglichkeit benötigt. Hier kommt der Dialog „Ergebnisse neu priorisieren“ ins Spiel. Sie
können ihn über den Eintrag „Ergebnisse neu priorisieren“ im Menü „Aktionen“ aufrufen.

In diesem Dialog wählen Sie Kriterien aus, nach denen in jeder Duplikatgruppe ein
Referenz-Duplikat bestimmt wird. Die Liste der verfügbaren Kriterien befindet sich links, die
Liste der von Ihnen gewählten Kriterien rechts.

Ein Kriterium besteht aus einer Kategorie, gefolgt von einem Argument. „Größe (Höchste)“
bedeutet beispielsweise, dass das Duplikat mit der größten Größe gewinnt. „Ordner (/foo/bar)“
bedeutet, dass Duplikate in diesem Ordner gewinnen. Um der rechten Liste ein Kriterium
hinzuzufügen, wählen Sie zuerst eine Kategorie in der Auswahlliste, dann ein Unterargument in
der darunterliegenden Liste und klicken anschließend auf die nach rechts zeigende Pfeiltaste.

Die Reihenfolge der Liste rechts ist wichtig (Sie können Einträge per Drag & Drop umsortieren).
Bei der Wahl eines Duplikats für die Referenzposition wird zuerst das erste Kriterium
verwendet. Bei Gleichstand kommt das zweite Kriterium zum Zug und so weiter. Lauten Ihre
Argumente zum Beispiel „Größe (Höchste)“ und danach „Dateiname (Endet nicht mit einer
Zahl)“, dann wird als Referenz einer Gruppe die größte Datei gewählt; haben zwei oder mehr
Dateien dieselbe Größe, wird diejenige verwendet, deren Dateiname nicht mit einer Zahl endet.
Führen alle Kriterien zu einem Gleichstand, wird die Reihenfolge verwendet, in der die
Duplikate zuvor in der Gruppe standen.
