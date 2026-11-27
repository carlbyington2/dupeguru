Einstellungen
=============

**Zu scannende Tags:**
    Bei Verwendung des Scan-Typs **Tags** können Sie die Tags auswählen, die zum Vergleich
    herangezogen werden.

**Wortgewichtung:**
    Siehe :ref:`word-weighting`.

**Ähnliche Wörter abgleichen:**
    Siehe :ref:`similarity-matching`.

**Bilder unterschiedlicher Abmessungen abgleichen:**
    Wenn Sie dieses Kästchen aktivieren, dürfen Bilder unterschiedlicher Abmessungen in
    derselben Duplikatgruppe vorkommen.

**Bilder unterschiedlicher Drehung abgleichen:**
    Wenn Sie dieses Kästchen aktivieren, dürfen Bilder unterschiedlicher Drehung in derselben
    Duplikatgruppe vorkommen.

.. _filter-hardness:

**Filterschärfe:**
    Der Schwellenwert, ab dem zwei Dateien als Duplikate gelten. Ein niedrigerer Wert bedeutet
    mehr Duplikate. Die Bedeutung des Schwellenwerts hängt vom Scan-Typ ab (siehe :doc:`scan`).
    Funktioniert nur bei :ref:`Wort-Scans <worded-scan>` und
    :ref:`Bildblock-Scans <picture-blocks-scan>`.

**Verschiedene Dateiarten mischen:**
    Wenn Sie dieses Kästchen aktivieren, dürfen Duplikatgruppen Dateien mit unterschiedlichen
    Erweiterungen enthalten. Aktivieren Sie es nicht, dürfen sie es eben nicht!

**Duplikate ignorieren, die per Hardlink auf dieselbe Datei verweisen:**
    Wenn diese Option aktiviert ist, prüft dupeGuru Duplikate daraufhin, ob sie auf denselben
    `Inode`_ verweisen. Ist das der Fall, gelten sie nicht als Duplikate. (Nur für OS X und
    Linux)

**Beim Filtern reguläre Ausdrücke verwenden:**
    Wenn Sie dieses Kästchen aktivieren, behandelt die Filterfunktion Ihre Filteranfrage als
    **regulären Ausdruck**. Diese zu erklären würde den Rahmen dieses Dokuments sprengen. Ein
    guter Einstieg zum Erlernen ist `regular-expressions.info`_.

**Leere Ordner nach dem Löschen oder Verschieben entfernen:**
    Wenn diese Option aktiviert ist, werden Ordner gelöscht, nachdem eine Datei gelöscht oder
    verschoben wurde und der Ordner leer ist.

**Dateien teilweise hashen, wenn größer als:**
    Wird nur von den Scan-Typen **Inhalt** und **Ordner** verwendet. Dateien, die größer als
    dieser Wert sind, werden zunächst anhand von Stichproben verglichen, die an einigen Stellen
    der Datei entnommen werden, sodass Dateien, die sich dort unterscheiden, nie vollständig
    gelesen werden. Das spart bei großen Dateien gleicher Größe Zeit. Dateien, deren Stichproben
    übereinstimmen, werden weiterhin vollständig verglichen.

**Kopieren und Verschieben:**
    Legt fest, wie sich die Operationen Kopieren und Verschieben (im Menü „Aktionen“) verhalten.

* **Direkt im Ziel:** Alle Dateien werden direkt im ausgewählten Ziel abgelegt, ohne den
  Quellpfad überhaupt nachzubilden.
* **Relativen Pfad nachbilden:** Der Pfad der Quelldatei wird im Zielordner bis zur
  Wurzelauswahl im Verzeichnisbereich nachgebildet. Wenn Sie beispielsweise
  ``/Users/foobar/SomeFolder`` zu Ihrem Verzeichnisbereich hinzugefügt haben und
  ``/Users/foobar/SomeFolder/SubFolder/SomeFile.ext`` in das Ziel ``/Users/foobar/MyDestination``
  verschieben, lautet das endgültige Ziel der Datei ``/Users/foobar/MyDestination/SubFolder``
  (``SomeFolder`` wurde vom Quellpfad im endgültigen Ziel abgeschnitten).
* **Absoluten Pfad nachbilden:** Der Pfad der Quelldatei wird im Zielordner vollständig
  nachgebildet. Wenn Sie beispielsweise ``/Users/foobar/SomeFolder/SubFolder/SomeFile.ext`` in
  das Ziel ``/Users/foobar/MyDestination`` verschieben, lautet das endgültige Ziel der Datei
  ``/Users/foobar/MyDestination/Users/foobar/SomeFolder/SubFolder``.

In allen Fällen behandelt dupeGuru Namenskonflikte elegant, indem dem Zieldateinamen eine Zahl
vorangestellt wird, falls der Dateiname im Ziel bereits existiert.

**Markieren von Referenzdateien erlauben:**
    Im Reiter „Erweitert“. Wenn diese Option aktiviert ist, erhalten auch Referenzdateien ein
    Markierungsfeld, sodass jede Datei einer Gruppe gelöscht, verschoben oder kopiert werden
    kann. Unter :doc:`results` steht, wie sich markierte Referenzen verhalten und wie dupeGuru
    sie schützt.

**Benutzerdefinierter Befehl:**
    Diese Einstellung legt den Befehl fest, der von der Aktion „Benutzerdefinierten Befehl
    aufrufen“ ausgeführt wird. Über diese Aktion können Sie jede beliebige externe Anwendung
    aufrufen. Das kann nützlich sein, wenn Sie zum Beispiel ein praktisches Vergleichsprogramm
    (Diff-Tool) installiert haben.

Das Format des Befehls entspricht dem, was Sie auf der Kommandozeile schreiben würden, nur dass
es 2 Platzhalter gibt: **%d** und **%r**. Diese Platzhalter werden durch den Pfad des
ausgewählten Duplikats (%d) und den Pfad der Referenzdatei des ausgewählten Duplikats (%r)
ersetzt.

Wenn der Pfad zu Ihrer ausführbaren Datei Leerzeichen enthält, sollten Sie ihn in
Anführungszeichen "" setzen. Auch die Platzhalter sollten Sie in Anführungszeichen setzen, da
Pfade zu Duplikaten und Referenzen sehr wahrscheinlich Leerzeichen enthalten. Hier ein Beispiel
für einen benutzerdefinierten Befehl::

    "C:\Program Files\SuperDiffProg\SuperDiffProg.exe" "%d" "%r"

.. _Inode: http://en.wikipedia.org/wiki/Inode
.. _regular-expressions.info: http://www.regular-expressions.info
