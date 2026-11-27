Ergebnisse
==========

.. contents::

Wenn dupeGuru den Scan nach Duplikaten abgeschlossen hat, zeigt es seine Ergebnisse in Form einer Liste von Duplikatgruppen an.

Über Duplikatgruppen
--------------------

Eine Duplikatgruppe ist eine Gruppe von Dateien, die alle miteinander übereinstimmen. Jede Gruppe hat eine **Referenzdatei** und eine oder mehrere **doppelte Dateien**. Die Referenzdatei ist die erste Datei der Gruppe. Ihr Markierungsfeld ist deaktiviert. Darunter, eingerückt, stehen die doppelten Dateien.

Sie können doppelte Dateien markieren, aber standardmäßig können Sie die Referenzdatei einer Gruppe nicht markieren. Das ist eine Sicherheitsmaßnahme, damit dupeGuru nicht nur doppelte Dateien löscht, sondern auch deren Referenz. Das wollen Sie sicher nicht, oder?

Wenn jede Datei einer Gruppe verschwinden soll, aktivieren Sie in den erweiterten Einstellungen **Markieren von Referenzdateien erlauben**. Referenzdateien erhalten dann ebenfalls ein Markierungsfeld, und eine markierte Referenz wird durchgestrichen dargestellt. Eine Referenz markieren Sie, indem Sie auf ihr Markierungsfeld klicken oder sie auswählen und die **Leertaste** drücken. **Alle markieren** und **Markierung umkehren** lassen Referenzen weiterhin unberührt, und **Markierung aufheben** hebt ihre Markierung auf. Eine Datei aus einem Referenzordner kann nie markiert werden. Vor dem Löschen, Verschieben oder Kopieren markierter Dateien, die Referenzen enthalten, fragt dupeGuru nach einer Bestätigung, und gelöschte Dateien können nicht durch Links ersetzt werden, solange Referenzen markiert sind. Wird eine Referenz gelöscht oder verschoben, übernimmt die nächste Datei ihrer Gruppe die Referenzposition, unmarkiert.

Was bestimmt, welche Dateien Referenz und welche Duplikate sind, ist zuerst ihr Ordnerzustand. Eine Datei aus einem Referenzordner ist in einer Duplikatgruppe immer die Referenz. Stammen alle Dateien aus einem normalen Ordner, bestimmt die Größe, welche Datei die Referenz einer Duplikatgruppe wird. dupeGuru nimmt an, dass Sie immer die größte Datei behalten möchten, daher übernehmen die größten Dateien die Referenzposition.

Sie können die Referenzdatei einer Gruppe manuell ändern. Wählen Sie dazu die doppelte Datei aus, die Sie zur Referenz befördern möchten, und klicken Sie auf **Aktionen-->Ausgewählte zur Referenz machen**.

Ergebnisse prüfen
-----------------

Obwohl Sie einfach auf **Bearbeiten-->Alle markieren** und dann auf **Aktionen-->Markierte in den Papierkorb verschieben** klicken können, um alle doppelten Dateien in Ihren Ergebnissen schnell zu löschen, wird immer empfohlen, alle Duplikate vor dem Löschen zu prüfen.

Um Ihnen beim Prüfen der Ergebnisse zu helfen, können Sie das **Detailfenster** einblenden. Dieses Fenster zeigt alle Details der aktuell ausgewählten Datei sowie die Details ihrer Referenz. Das ist sehr praktisch, um schnell festzustellen, ob ein Duplikat wirklich ein Duplikat ist. Sie können auch auf eine Datei doppelklicken, um sie mit der zugehörigen Anwendung zu öffnen.

Haben Sie mehr falsche als echte Duplikate (wenn Ihre Filterschärfe sehr niedrig ist), gehen Sie am besten so vor: Prüfen Sie die Duplikate, markieren Sie die echten Duplikate und klicken Sie dann auf **Aktionen-->Markierte in den Papierkorb verschieben**. Haben Sie mehr echte als falsche Duplikate, können Sie stattdessen alle Dateien markieren, die falsche Duplikate sind, und **Aktionen-->Markierte aus Ergebnissen entfernen** verwenden.

Markieren und Auswählen
-----------------------

Ein **markiertes** Duplikat ist ein Duplikat, dessen Kästchen daneben ein Häkchen hat. Ein **ausgewähltes** Duplikat ist ein hervorgehobenes Duplikat. Mehrfachauswahl-Aktionen lassen sich in dupeGuru auf die übliche Weise ausführen (Umschalt-/Befehls-/Strg-Klick). Mit der **Leertaste** können Sie den Markierungszustand aller ausgewählten Duplikate umschalten.

Nur Duplikate anzeigen
----------------------

Ist dieser Modus aktiviert, werden die Duplikate ohne ihre jeweilige Referenzdatei angezeigt. Sie können diese Liste wie im normalen Modus auswählen, markieren und sortieren.

Die Ergebnisse von dupeGuru werden im normalen Modus nach der **Referenzdatei** der Duplikatgruppen sortiert. Das bedeutet: Wenn Sie zum Beispiel alle Duplikate mit der Erweiterung „exe“ markieren möchten, können Sie die Ergebnisse nicht einfach nach „Art“ sortieren, um alle exe-Duplikate beisammen zu haben, da eine Gruppe aus mehr als einer Dateiart bestehen kann. Hier kommt der Modus „Nur Duplikate“ ins Spiel. Um alle Ihre „exe“-Duplikate zu markieren, müssen Sie nur:

* Den Modus „Nur Duplikate“ aktivieren.
* Die Spalte „Art“ über das Menü „Spalten“ hinzufügen.
* Auf diese Spalte „Art“ klicken, um die Liste nach Art zu sortieren.
* Das erste Duplikat der Art „exe“ suchen.
* Es auswählen.
* In der Liste nach unten blättern, um das letzte Duplikat der Art „exe“ zu finden.
* Die Umschalttaste gedrückt halten und darauf klicken.
* Die Leertaste drücken, um alle ausgewählten Duplikate zu markieren.

.. _deltavalues:

Delta-Werte
-----------

Wenn Sie diesen Schalter einschalten, zeigen numerische Spalten den Wert relativ zur Referenz des Duplikats statt der absoluten Werte an. Diese Delta-Werte werden außerdem in einer anderen Farbe, Orange, dargestellt, damit Sie sie leicht erkennen. Ist ein Duplikat zum Beispiel 1,2 MB groß und seine Referenz 1,4 MB, zeigt die Spalte „Größe“ -0,2 MB an.

Außerdem werden auch nicht-numerische Werte orange dargestellt, wenn sie sich von ihrer Referenz unterscheiden, und bleiben schwarz, wenn der Wert derselbe ist. In Kombination mit der Spaltensortierung im Modus „Nur Duplikate“ ermöglicht das eine sehr leistungsfähige Filterung nach dem Scan.

Nur Duplikate und Delta-Werte
-----------------------------

Der Modus „Nur Duplikate“ zeigt seine wahre Stärke, wenn Sie ihn zusammen mit eingeschaltetem Schalter „Delta-Werte“ verwenden. Wenn Sie ihn einschalten, werden relative statt absolute Werte angezeigt. Wenn Sie also zum Beispiel aus Ihren Ergebnissen alle Duplikate entfernen möchten, die mehr als 300 KB von ihrer Referenz abweichen, können Sie die Ergebnisse im Modus „Nur Duplikate“ nach Größe sortieren, alle Duplikate unter -300 in der Spalte „Größe“ auswählen, löschen und dann dasselbe für Duplikate über 300 am Ende der Liste tun.

Dasselbe gilt für nicht-numerische Werte: Sind „Nur Duplikate“ und „Delta-Werte“ gleichzeitig aktiviert, gruppiert die Spaltensortierung die Zeilen danach, ob sie orange sind oder nicht. Beispiel: Sie haben einen Inhalts-Scan durchgeführt, möchten aber nur Duplikate löschen, die denselben Dateinamen haben? Sortieren Sie nach Dateiname, und alle Duplikate, deren Dateiname mit dem der Referenz übereinstimmt, werden zusammen gruppiert, wobei ihr Wert schwarz dargestellt wird.

Sie könnten damit auch die Referenzpriorität Ihrer Duplikatliste ändern. Wenn Sie einen frischen Scan durchführen und es keine Referenzordner gibt, ist die Referenzdatei jeder Gruppe die größte Datei. Wenn Sie das ändern möchten, zum Beispiel auf die neueste Änderungszeit, können Sie die Ergebnisse im Modus „Nur Duplikate“ **absteigend** nach Änderungszeit sortieren, alle Duplikate mit einem Delta-Wert der Änderungszeit größer als 0 auswählen und auf **Ausgewählte zur Referenz machen** klicken. Der Grund, warum die Sortierung absteigend sein muss: Sind zwei Dateien derselben Duplikatgruppe ausgewählt, wenn Sie auf **Ausgewählte zur Referenz machen** klicken, wird nur die erste der Liste zur Referenz gemacht, die andere wird ignoriert. Und da die zuletzt geänderte Datei die Referenz werden soll, stellt eine absteigende Sortierung sicher, dass der erste Eintrag der Liste der zuletzt geänderte ist.

Filtern
-------

dupeGuru unterstützt das Filtern nach dem Scan. Damit können Sie Ihre Ergebnisse eingrenzen, um Aktionen auf eine Teilmenge anzuwenden. Zum Beispiel könnten Sie mit dem Filter leicht alle Duplikate markieren, deren Dateiname „copy“ enthält.

Um die Filterfunktion zu verwenden, geben Sie Ihren Filter in das Suchfeld „Filter“ oben rechts im Ergebnisfenster ein. Was Sie in dieses Feld eingeben, wird auf den *gesamten Pfad* jedes Duplikats in den Ergebnissen angewendet. Es werden nur Duplikat-*Gruppen* angezeigt, die mindestens ein Duplikat enthalten, das dem Filter entspricht.

Gibt es Gruppen, in denen nicht alle Duplikate dem Filter entsprechen, zeigen wir dennoch alle Duplikate der Gruppe an. Die nicht passenden Duplikate befinden sich jedoch im „Referenzmodus“. Daher können Sie Aktionen wie „Alle markieren“ ausführen und sicher sein, nur gefilterte Duplikate zu markieren.

Um zu den ungefilterten Ergebnissen zurückzukehren, leeren Sie das Feld oder klicken Sie auf das „X“.

Im einfachen Modus (dem Standardmodus) ist das, was Sie als Filter eingeben, die Zeichenkette, die für die eigentliche Filterung verwendet wird, mit Ausnahme eines Platzhalters: **\***. Wenn Sie also „[*]“ als Filter eingeben, passt er auf alles, was eckige Klammern [] enthält, egal was dazwischen steht.

Für fortgeschrittenere Filterung können Sie „Beim Filtern reguläre Ausdrücke verwenden“ einschalten. Die Filterfunktion verwendet dann **reguläre Ausdrücke**. Ein regulärer Ausdruck ist eine Sprache zum Abgleichen von Text. Diese zu erklären würde den Rahmen dieses Dokuments sprengen. Ein guter Einstieg zum Erlernen ist `regular-expressions.info`_.

Treffer unterscheiden weder im einfachen noch im Regexp-Modus zwischen Groß- und Kleinschreibung.

Damit der Filter greift, muss Ihr regulärer Ausdruck nicht auf den gesamten Dateinamen passen; der Name muss lediglich eine Zeichenkette enthalten, die dem Ausdruck entspricht.

Aktionsmenü
-----------

**Ignorierliste leeren:**
    Entfernt alle von Ihnen hinzugefügten ignorierten Treffer. Sie müssen einen neuen Scan
    starten, damit die frisch geleerte Ignorierliste wirksam wird.
**Ergebnisse als XHTML exportieren:**
    Nimmt die aktuellen Ergebnisse und erstellt daraus eine XHTML-Datei. Die Spalten, die beim
    Klick auf diese Schaltfläche sichtbar sind, sind die Spalten in der XHTML-Datei. Die Datei
    wird automatisch in Ihrem Standardbrowser geöffnet.
**Markierte in den Papierkorb verschieben:**
    Verschiebt selbstverständlich alle markierten Duplikate in den Papierkorb. Bevor es
    weitergeht, werden Ihnen Löschoptionen angezeigt (siehe unten).
**Markierte verschieben nach...:**
    Fragt nach einem Ziel und verschiebt dann alle markierten Dateien dorthin. Je nach Einstellung
    „Kopieren und Verschieben“ wird der Pfad der Quelldatei im Ziel eventuell nachgebildet.
**Markierte kopieren nach...:**
    Fragt nach einem Ziel und kopiert dann alle markierten Dateien dorthin. Je nach Einstellung
    „Kopieren und Verschieben“ wird der Pfad der Quelldatei im Ziel eventuell nachgebildet.
**Markierte aus Ergebnissen entfernen:**
    Entfernt alle markierten Duplikate aus den Ergebnissen. Die eigentlichen Dateien werden nicht
    angetastet und bleiben, wo sie sind.
**Ausgewählte aus Ergebnissen entfernen:**
    Entfernt alle ausgewählten Duplikate aus den Ergebnissen. Beachten Sie, dass alle
    ausgewählten Referenzdateien ignoriert werden; mit dieser Aktion können nur Duplikate
    entfernt werden.
**Ausgewählte zur Referenz machen:**
    Befördert alle ausgewählten Duplikate zur Referenz. Ist ein Duplikat Teil einer Gruppe, deren
    Referenzdatei aus einem Referenzordner stammt (blaue Farbe), wird für dieses Duplikat keine
    Aktion ausgeführt. Sind mehrere Duplikate derselben Gruppe ausgewählt, wird nur das erste
    jeder Gruppe befördert.
**Ausgewählte zur Ignorierliste hinzufügen:**
    Entfernt zunächst alle ausgewählten Duplikate aus den Ergebnissen und fügt dann den Treffer
    dieses Duplikats mit der aktuellen Referenz zur Ignorierliste hinzu. Dieser Treffer taucht in
    weiteren Scans nicht mehr auf. Das Duplikat selbst kann wiederkehren, wird dann aber mit
    einer anderen Referenzdatei abgeglichen. Sie können die Ignorierliste mit dem Befehl
    „Ignorierliste leeren“ leeren.
**Ausgewählte mit Standardanwendung öffnen:**
    Öffnet die Datei mit der Anwendung, die dem Typ der ausgewählten Datei zugeordnet ist.
**Ausgewählte im Finder anzeigen:**
    Öffnet den Ordner, der die ausgewählte Datei enthält.
**Benutzerdefinierten Befehl aufrufen:**
    Ruft die in Ihren Einstellungen eingerichtete externe Anwendung auf und verwendet dabei die
    aktuelle Auswahl als Argumente. Enthält die Auswahl Referenzdateien, bei denen **%d** und
    **%r** dieselbe Datei sind, fragt dupeGuru zuvor nach einer Bestätigung.
**Ausgewählte umbenennen:**
    Fragt nach einem neuen Namen und benennt dann die ausgewählte Datei um.

Löschoptionen
-------------

Diese Optionen beeinflussen, wie das Löschen von Duplikaten abläuft. Meistens müssen Sie keine
davon aktivieren.

**Gelöschte Dateien verlinken:**
    Die gelöschten Dateien werden durch einen Link auf die Referenzdatei ersetzt. Sie können
    wählen, ob dies ein `Symlink`_ oder ein `Hardlink`_ sein soll. Für eine fundierte Wahl lesen
    Sie am besten die vollständigen Wikipedia-Seiten dazu, aber kurz gesagt: Ein Symlink ist eine
    Verknüpfung zum Pfad der Datei. Wird die Originaldatei gelöscht oder verschoben, ist der Link
    defekt. Ein Hardlink ist ein Link auf die Datei *selbst*. Dieser Link ist so gut wie eine
    „echte“ Datei. Erst wenn *alle* Hardlinks auf eine Datei gelöscht sind, wird die Datei selbst
    gelöscht.

    Unter OSX und Linux wird diese Funktion vollständig unterstützt, unter Windows ist es etwas
    kompliziert. Windows XP unterstützt sie nicht, Vista und neuer dagegen schon. Damit die
    Funktion jedoch arbeitet, muss dupeGuru mit Administratorrechten laufen.

**Dateien direkt löschen:**
    Löscht Dateien direkt, statt sie in den Papierkorb zu verschieben. Dies dient der
    Fehlersuche, und normalerweise müssen Sie es nicht aktivieren, es sei denn, dupeGuru hat
    Probleme, Dateien normal zu löschen, was vorkommen kann, wenn Sie versuchen, Dateien auf
    Netzwerkspeichern (NAS) zu löschen.

.. _regular-expressions.info: http://www.regular-expressions.info
.. _Hardlink: http://en.wikipedia.org/wiki/Hard_link
.. _Symlink: http://en.wikipedia.org/wiki/Symbolic_link
