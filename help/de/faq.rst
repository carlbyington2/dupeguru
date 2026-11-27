Häufig gestellte Fragen
=======================

.. contents::

Was ist dupeGuru?
-----------------

dupeGuru ist ein Werkzeug, um doppelte Dateien auf Ihrem Computer zu finden. Es hat drei
Betriebsmodi: Standard, Musik und Bilder. Jeder Modus hat seine eigenen spezialisierten
Einstellungen.

Jeder Modus bietet mehrere Scan-Typen, etwa Dateiname, Inhalt oder Tags. Einige Scan-Typen
verfügen über fortgeschrittene Fuzzy-Matching-Algorithmen, mit denen Sie Duplikate finden
können, die andere, starrere Duplikat-Scanner nicht finden.

Was macht es besonders?
-----------------------

Vor allem die Anpassbarkeit. Es gibt viele Scan-Optionen, mit denen Sie genau die Art von
Ergebnissen erhalten, die Sie wirklich suchen.

Wie sicher ist die Verwendung von dupeGuru?
-------------------------------------------

Sehr sicher. dupeGuru wurde so entworfen, dass Sie keine Dateien löschen, die Sie nicht löschen
wollten. Zum einen gibt es das Referenzordner-System, mit dem Sie Ordner festlegen können, aus
denen dupeGuru Sie absolut **keine** Dateien löschen lassen soll, und zum anderen das
Gruppenreferenz-System, das sicherstellt, dass Sie **immer** mindestens ein Mitglied der
Duplikatgruppe behalten.

Wie kann ich einen Fehler melden oder eine Funktion vorschlagen?
----------------------------------------------------------------

dupeGuru wird auf `GitHub`_ gehostet, und dort werden auch die Issues verfolgt. Am besten melden
Sie einen Fehler oder schlagen eine Funktion vor, indem Sie sich bei GitHub anmelden und
`ein Issue eröffnen`_.

Das Markierungsfeld einer Datei, die ich löschen möchte, ist deaktiviert. Was muss ich tun?
-------------------------------------------------------------------------------------------

Die Referenz (die erste Datei) einer Duplikatgruppe können Sie nicht markieren. Sie können aber
eine doppelte Datei zur Referenz befördern. Ist also eine Datei, die Sie markieren möchten, die
Referenz, wählen Sie in der Gruppe ein Duplikat aus, das Sie zur Referenz befördern möchten, und
klicken Sie auf **Aktionen-->Ausgewählte zur Referenz machen**. Stammt die Referenzdatei aus
einem Referenzordner (Dateiname in blauer Schrift), können Sie sie nicht von der Referenzposition
entfernen.

Ich habe einen Ordner, aus dem ich auf keinen Fall Dateien löschen möchte.
--------------------------------------------------------------------------

Wenn Sie sicher sein möchten, dass dupeGuru nie Dateien aus einem bestimmten Ordner löscht,
setzen Sie dessen Zustand unter :doc:`folders` auf **Referenz**.

Was bedeutet der Hinweis „(X verworfen)“ in der Statusleiste?
-------------------------------------------------------------

In manchen Fällen werden einzelne Treffer aus Sicherheitsgründen nicht in die endgültigen
Ergebnisse aufgenommen. Dazu ein Beispiel. Wir haben 3 Dateien: A, B und C. Wir scannen sie mit
einer niedrigen Filterschärfe. Der Scanner stellt fest, dass A mit B übereinstimmt, A mit C
übereinstimmt, B aber **nicht** mit C. Hier hat dupeGuru ein Problem. Es kann keine
Duplikatgruppe mit A, B und C bilden, weil nicht alle Dateien der Gruppe miteinander
übereinstimmen würden. Es könnte 2 Gruppen bilden: eine Gruppe A-B und eine Gruppe A-C, tut es
aber aus Sicherheitsgründen nicht. Überlegen wir: Wenn B nicht mit C übereinstimmt, bedeutet das
wahrscheinlich, dass B, C oder beide tatsächlich keine Duplikate sind. Gäbe es 2 Gruppen (A-B und
A-C), würden Sie am Ende sowohl B als auch C löschen. Und wenn eine davon kein Duplikat ist, ist
das wirklich nicht das, was Sie wollen, oder? Deshalb verwirft dupeGuru in einem solchen Fall den
Treffer A-C (und fügt einen Hinweis in der Statusleiste hinzu). Löschen Sie also B und führen
den Scan erneut aus, erhalten Sie in den nächsten Ergebnissen einen Treffer A-C.

Ich möchte alle Dateien aus einem bestimmten Ordner markieren. Was kann ich tun?
--------------------------------------------------------------------------------

Aktivieren Sie den Modus :doc:`Nur Duplikate <results>` und klicken Sie auf die Spalte „Ordner“,
um Ihre Duplikate nach Ordner zu sortieren. Dann ist es leicht, alle Duplikate aus demselben
Ordner auszuwählen und mit der Leertaste alle ausgewählten Duplikate zu markieren.

Ich möchte alle Dateien entfernen, die mehr als 300 KB von ihrer Referenzdatei abweichen. Was kann ich tun?
-----------------------------------------------------------------------------------------------------------

* Aktivieren Sie den Modus :doc:`Nur Duplikate <results>`.
* Aktivieren Sie den Modus **Delta-Werte**.
* Klicken Sie auf die Spalte „Größe“, um die Ergebnisse nach Größe zu sortieren.
* Wählen Sie alle Duplikate unterhalb von -300 aus.
* Klicken Sie auf **Ausgewählte aus Ergebnissen entfernen**.
* Wählen Sie alle Duplikate oberhalb von 300 aus.
* Klicken Sie auf **Ausgewählte aus Ergebnissen entfernen**.

Ich möchte meine zuletzt geänderten Dateien zu Referenzdateien machen. Was kann ich tun?
----------------------------------------------------------------------------------------

* Aktivieren Sie den Modus :doc:`Nur Duplikate <results>`.
* Aktivieren Sie den Modus **Delta-Werte**.
* Klicken Sie auf die Spalte „Änderung“, um die Ergebnisse nach Änderungsdatum zu sortieren.
* Klicken Sie erneut auf die Spalte „Änderung“, um die Sortierreihenfolge umzukehren.
* Wählen Sie alle Duplikate oberhalb von 0 aus.
* Klicken Sie auf **Ausgewählte zur Referenz machen**.

Ich möchte alle Duplikate markieren, die das Wort „copy“ enthalten. Wie mache ich das?
--------------------------------------------------------------------------------------

* Geben Sie „copy“ in das Feld „Filter“ oben rechts im Ergebnisfenster ein.
* Klicken Sie auf **Markieren --> Alle markieren**.

Ich möchte alle Songs entfernen, die mehr als 3 Sekunden von ihrer Referenzdatei abweichen. Was kann ich tun?
-------------------------------------------------------------------------------------------------------------

* Aktivieren Sie den Modus :doc:`Nur Duplikate <results>`.
* Aktivieren Sie den Modus **Delta-Werte**.
* Klicken Sie auf die Spalte „Zeit“, um die Ergebnisse nach Zeit zu sortieren.
* Wählen Sie alle Duplikate unterhalb von -00:03 aus.
* Klicken Sie auf **Ausgewählte aus Ergebnissen entfernen**.
* Wählen Sie alle Duplikate oberhalb von 00:03 aus.
* Klicken Sie auf **Ausgewählte aus Ergebnissen entfernen**.

Ich möchte meine Songs mit der höchsten Bitrate zu Referenzdateien machen. Was kann ich tun?
--------------------------------------------------------------------------------------------

* Aktivieren Sie den Modus :doc:`Nur Duplikate <results>`.
* Aktivieren Sie den Modus **Delta-Werte**.
* Klicken Sie auf die Spalte „Bitrate“, um die Ergebnisse nach Bitrate zu sortieren.
* Klicken Sie erneut auf die Spalte „Bitrate“, um die Sortierreihenfolge umzukehren.
* Wählen Sie alle Duplikate oberhalb von 0 aus.
* Klicken Sie auf **Ausgewählte zur Referenz machen**.

Ich möchte nicht, dass [Live]- und [Remix]-Versionen meiner Songs als Duplikate gelten. Wie mache ich das?
----------------------------------------------------------------------------------------------------------

Ist Ihr Vergleichsschwellenwert niedrig genug, enthalten Ihre Ergebnisse wahrscheinlich Live- und
Remix-Versionen Ihrer Songs. Das lässt sich nicht verhindern, aber Sie können sie nach dem Scan
leicht aus Ihren Ergebnissen entfernen: mit der Filterung nach dem Scan. Wenn Sie zum Beispiel
jeden Song entfernen möchten, in dessen Namen etwas in eckigen Klammern [] steht:

* Geben Sie „[*]“ in das Feld „Filter“ oben rechts im Ergebnisfenster ein.
* Klicken Sie auf **Markieren --> Alle markieren**.
* Klicken Sie auf **Aktionen --> Ausgewählte aus Ergebnissen entfernen**.

Der Schieberegler „Filterschärfe“ in den Einstellungen lässt sich nicht bewegen!
--------------------------------------------------------------------------------

Dieser Schieberegler ist nur für Scan-Typen relevant, die „Unschärfe“ unterstützen. Viele
Scan-Typen, wie etwa der Typ „Inhalt“, unterstützen nur exakte Übereinstimmungen. Wenn diese
Typen ausgewählt sind, ist der Schieberegler deaktiviert.

Bei manchen Betriebssystemen ist die Deaktivierung schwerer zu erkennen als bei anderen, aber
wenn Sie den Schieberegler nicht bewegen können, bedeutet das, dass diese Einstellung für Ihren
aktuellen Scan-Typ irrelevant ist.

Ich habe versucht, meine Duplikate in den Papierkorb zu verschieben, aber dupeGuru meldet, dass es nicht möglich ist. Warum? Was kann ich tun?
----------------------------------------------------------------------------------------------------------------------------------------------

Meistens liegt der Grund, warum dupeGuru Dateien nicht in den Papierkorb verschieben kann, an den
Dateiberechtigungen. Sie benötigen *Schreibrechte* für Dateien, die Sie in den Papierkorb
verschieben möchten.

Macht dupeGuru auch nach der Korrektur Ihrer Berechtigungen noch Probleme, versuchen Sie, die
Option „Dateien direkt löschen“ zu aktivieren, die Ihnen beim Aktivieren von „In den Papierkorb
verschieben“ angeboten wird. Dadurch werden Dateien nicht in den Papierkorb verschoben, sondern
sofort gelöscht. In manchen Fällen, zum Beispiel bei Netzwerkspeichern (NAS), hat sich gezeigt,
dass dies funktioniert, wenn das normale Löschen versagte.

Warum ist der Inhalts-Scan im Bildermodus so langsam?
-----------------------------------------------------

Diese Scan-Methode unterscheidet sich stark von den anderen Methoden. Sie kann doppelte Fotos
erkennen, auch wenn sie nicht exakt gleich sind. Diese sehr coole Fähigkeit hat ihren Preis:
Zeit. Jedes Bild muss einzeln und unscharf mit allen anderen verglichen werden, und das erfordert
viel CPU-Leistung.

Wenn Sie nur exakte Duplikate finden müssen, verwenden Sie einfach den Standardmodus von dupeGuru
mit der Scan-Methode „Inhalt“. Wenn Ihre Fotos EXIF-Tags haben, können Sie auch die Scan-Methode
„EXIF“ ausprobieren, die viel schneller ist.

Wo befinden sich die Benutzerdateien?
-------------------------------------

Aus irgendeinem Grund möchten Sie die Benutzerdateien von dupeGuru (Debug-Protokolle, Caches
usw.) entfernen oder bearbeiten. Wo sie liegen, hängt von Ihrer Plattform ab:

* Linux: ``~/.local/share/data/Hardcoded Software/dupeGuru``
* Mac OS X: ``~/Library/Application Support/dupeGuru``

Die Einstellungen werden an anderer Stelle gespeichert:

* Linux: ``~/.config/Hardcoded Software/dupeGuru.conf``
* Mac OS X: Im eingebauten ``defaults``-System, als ``com.hardcoded-software.dupeguru``

.. _GitHub: https://github.com/carlbyington2/dupeguru
.. _ein Issue eröffnen: https://github.com/carlbyington2/dupeguru/issues
