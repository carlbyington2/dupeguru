Ordnerauswahl
=============

Das erste Fenster, das Sie beim Start von dupeGuru sehen, ist das Fenster zur Ordnerauswahl.
Dieses Fenster enthält die grundlegenden Eingaben, die dupeGuru zum Starten eines Scans
benötigt:

* Eine Auswahl des Anwendungsmodus
* Eine Auswahl des Scan-Typs
* Die zu scannenden Ordner

Anwendungsmodus
---------------

dupeGuru hat drei Hauptmodi: Standard, Musik und Bilder.

Standard eignet sich für beliebige Dateitypen. Das macht diesen Modus zum vielseitigsten, doch
ihm fehlen die spezialisierten Funktionen der anderen Modi.

Der Musikmodus scannt nur Musikdateien, unterstützt dafür aber den Vergleich von Tags, und sein
Ergebnisfenster hat viele Informationsspalten zu Audiodaten.

Der Bildermodus scannt nur Bilder, aber sein Inhalts-Scan-Typ ist ein leistungsfähiger
Fuzzy-Matcher, der Bilder finden kann, die einander ähnlich, aber nicht exakt gleich sind.

Die Wahl eines Anwendungsmodus ändert nicht nur die verfügbaren Scan-Typen in der darunterliegenden
Auswahl, sondern auch die verfügbaren Optionen im Einstellungsfenster. Wenn Sie Ihren Scan
feinabstimmen möchten, öffnen Sie das Einstellungsfenster daher unbedingt **nachdem** Sie den
Anwendungsmodus gewählt haben.

Scan-Typ
--------

Diese Auswahl legt fest, welche Art von Scan durchgeführt wird. Details zu den Scan-Typen
finden Sie unter :doc:`scan`.

Ordnerliste
-----------

Um einen Ordner hinzuzufügen, klicken Sie auf die Schaltfläche **+**. Wenn Sie bereits früher
Ordner hinzugefügt haben, erscheint ein Popup-Menü mit einer Liste der zuletzt hinzugefügten
Ordner. Sie können auf einen davon klicken, um ihn direkt zu Ihrer Liste hinzuzufügen. Wenn Sie
auf den ersten Eintrag des Popup-Menüs, **Neuen Ordner hinzufügen...**, klicken, werden Sie
aufgefordert, einen Ordner auszuwählen. Wenn Sie noch nie einen Ordner hinzugefügt haben,
erscheint kein Menü, und Sie werden direkt aufgefordert, einen neuen Ordner auszuwählen.

Eine alternative Möglichkeit, Ordner zur Liste hinzuzufügen, besteht darin, sie in die Liste zu
ziehen.

Um einen Ordner zu entfernen, wählen Sie ihn aus und klicken auf **-**. Ist beim Klick auf die
Schaltfläche ein Unterordner ausgewählt, wird der ausgewählte Ordner stattdessen in den Zustand
**Ausgeschlossen** versetzt (siehe unten), anstatt entfernt zu werden.

Ordnerzustände
--------------

Jeder Ordner kann sich in einem von drei Zuständen befinden:

**Normal:**
    In diesem Ordner gefundene Duplikate können gelöscht werden.
**Referenz:**
    In diesem Ordner gefundene Duplikate können **nicht** gelöscht werden. Dateien aus diesem
    Ordner können in der Duplikatgruppe nur an **Referenz**-Position landen. Landen mehrere
    Dateien aus Referenzordnern in derselben Duplikatgruppe, wird nur eine behalten. Die
    anderen werden aus der Gruppe entfernt.
**Ausgeschlossen:**
    Dateien in diesem Verzeichnis werden nicht in den Scan einbezogen.

Der Standardzustand eines Ordners ist natürlich **Normal**. Sie können den Zustand **Referenz**
für einen Ordner verwenden, wenn Sie sicherstellen möchten, dass keine Datei daraus gelöscht
wird.

Wenn Sie den Zustand eines Verzeichnisses festlegen, erben alle Unterordner dieses Ordners
automatisch diesen Zustand, sofern Sie nicht ausdrücklich den Zustand eines Unterordners
festlegen.

Um mehrere Ordner auf einmal zu ändern, wählen Sie mit Strg-Klick einzelne Zeilen oder mit
Umschalt-Klick einen Bereich aus, genau wie im Ergebnisfenster. Klicken Sie auf die
Zustandszelle einer beliebigen ausgewählten Zeile und wählen Sie Normal, Referenz oder
Ausgeschlossen. Die Wahl gilt für jeden ausgewählten Ordner, während die Auswahl und die
aufgeklappten Ordner erhalten bleiben.

Lassen Sie zum Beispiel „Alben“ auf Normal, klappen Sie den Ordner auf, wählen Sie nur seine
Künstler-Unterordner aus und wählen Sie dann Referenz. „Alben“ bleibt Normal, und die tieferen
Unterordner der Künstler erben Referenz. Sind ein übergeordneter Ordner und sein
untergeordneter Ordner beide ausgewählt, erhalten beide den gewählten Zustand. Das Ändern des
Zustands eines übergeordneten Ordners setzt weiterhin die Überschreibungen seiner Nachfolger
gemäß den üblichen Vererbungsregeln zurück.

Scannen
-------

Wenn Sie bereit sind, klicken Sie auf die Schaltfläche **Scannen**, um den Scan-Vorgang zu
starten. Sobald er abgeschlossen ist, werden Ihnen die :doc:`results` angezeigt.
