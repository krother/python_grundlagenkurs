Zwanzig Fragen
===============

In diesem Kapitel lernst du:
----------------------------

======= ==============================================
Bereich Thema
======= ==============================================
🚀       das Frage-Antwort-Spiel zum Laufen bringen
💡       eine JSON-Datei laden
🔧       mit einer minimalen Eingabedatei arbeiten
🐞       Code auf Fehler überprüfen
🐞       Fehlermeldungen lesen
🐞       diagnostische ``print``-Anweisungen einfügen
======= ==============================================

Aufgabe 1: Programm ausführen
-----------------------------

Unten findest du den Code für das Spiel **Zwanzig Fragen**.
Bei diesem Spiel denkst du an ein Tier.
Der Computer versucht es zu erraten – nur mit Ja-/Nein-Fragen.

So startest du:

- Lade den Code herunter: :download:`twenty_questions.py`
- Lade die Fragen herunter: :download:`questions.json`
- Lege beides im selben Ordner ab
- Führe das Programm aus

Was passiert?

Hier ist der vollständige Code:

.. literalinclude:: twenty_questions.py

Aufgabe 2: Code lesen
---------------------

Die einfachste Art von Fehlern sind **Syntaxfehler**.
Ein Syntaxfehler bedeutet meist, dass der Code für den Python-Interpreter unverständlich ist,
sodass er die Ausführung verweigert.

Diese Art von Fehler ist am leichtesten zu beheben.
Tatsächlich sollte dein Editor alle Syntaxfehler automatisch erkennen.

Finde und behebe sie.

Aufgabe 3: Fehlermeldungen lesen
--------------------------------

Sobald alle Syntaxfehler behoben sind, beginnt Python mit der Ausführung des Codes.
Die nächste Fehlerart sind Fehler, die *während* der Programmlaufzeit auftreten.
Diese heißen **Laufzeitfehler (Exceptions)**.
Das Programm bricht ab und du siehst eine Fehlermeldung – so weißt du, dass es einen Fehler gibt.

Was kannst du aus einer Fehlermeldung lernen?
Versuche, die Fehler so gut wie möglich zu beheben.

.. hint::

   Eine gute Vorgehensweise beim Debuggen von Python-Code ist:
   **Fehlermeldungen von unten nach oben lesen.**


Aufgabe 4: Diagnostische print-Befehle
--------------------------------------

Viele Fehler führen zu keiner Fehlermeldung.
Für Python sieht alles in Ordnung aus.
Aber du merkst, dass das Programm nicht das tut, was es soll.
Diese Kategorie heißt **semantische Fehler**.
Sie sind schwerer zu finden, weil du erst herausfinden musst, *dass* etwas falsch läuft
und dann *was* genau schiefläuft.

Bei einem semantischen Fehler hilft es, zusätzliche ``print``-Anweisungen einzufügen,
um herauszufinden, was im Programm geschieht.
Ein solcher **diagnostischer print-Befehl** könnte so aussehen:

.. code:: python3

   print("Punkt AAA erreicht")

oder den Inhalt einer Variablen anzeigen:

.. code:: python3

   print(finished)

Untersuche den nächsten Fehler mithilfe eines zusätzlichen ``print``.
Entferne den ``print``-Befehl wieder, sobald du den Fehler behoben hast.


Aufgabe 5: Minimale Eingabedaten
--------------------------------

Wenn dein Programm mit vielen Daten arbeitet, ist das Debuggen schwieriger.
Ein Problem bei dem Spiel ist, dass die Datei ``questions.json``
mehrere Tausend Fragen enthält.

Verwenden wir eine einfachere Variante.

Erstelle eine Datei namens ``mini_questions.json`` und nutze sie im Programm,
indem du den Dateinamen anpasst.
Der Inhalt sollte folgendermaßen aussehen:

::

    {
      "text": "ist es eine Schlange?",
      "yes": {
               "text": "es ist eine Python!"
               },
      "no": {
               "text": "es ist ein anderes Tier."
               }
    }

Wenn du das Spiel mit diesen Daten zum Laufen bekommst,
wechsle wieder zur großen Datei.

**Viel Erfolg!**

Reflexionsfragen
----------------

* Welche Arten von Fehlern kennst du?
* Welche Techniken zum Auffinden von Fehlern kennst du?
* Warum passieren Programmierfehler überhaupt?

.. seealso:: 

    - `Kristians Debugging-Tutorial bei der PyData 2017 <https://www.youtube.com/watch?v=04paHt9xG9U>`__
    - Daten von: `github.com/knkeniston/TwentyQuestions <https://github.com/knkeniston/TwentyQuestions/>`__
