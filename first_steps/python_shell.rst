Python als Taschenrechner
======================

|image0|

`Foto von Charles Deluvio auf
Unsplash <https://unsplash.com/@charlesdeluvio>`__


In diesem Kapitel lernst du:
----------------------------

======= =========================================
Bereich Thema
======= =========================================
🚀      Python als Taschenrechner verwenden
💡      die Datentypen *int* und *float*
⚙       Arithmetische Operatoren verwenden
⚙       Zahlen in Variablen speichern
⚙       Variablen verändern
🔧      den Inhalt von Variablen prüfen
======= =========================================


Arithmetics
-----------

In diesem Kapitel werden wir die Python-Kommandozeile als Taschenrechner verwenden.
Öffne ein Terminal und gib ein:

:: 

   python

Du solltest folgende Eingabeaufforderung im Konsolenfenster sehen:

::

   >>>


Aufgabe 1: Grundrechenarten
----------------------------

Führe einige Berechnungen in Python durch.
Setze die fehlenden Zeichen in die Lücken ein:

::

   >>> 1 + ___
   3

   >>> 12 ___ 8
   4

   >>> ___ * 5
   20

   >>> 21 / 7
   ___

   >>> ___ ** 2
   81

Gib die Befehle in die Konsole ein ein und beobachte was passiert.

.. hint::

   Gib den ersten Teil (`>>>`) **nicht** ein, dieser erscheint automatisch.

Aufgabe 2: Divisionen
---------------------

Was ist der Unterschied zwischen folgenden Anweisungen?

.. code:: python3

   >>> 10 / 4
   >>> 10.0 / 4
   >>> 10.0 / 4.0
   >>> 10 // 4
   >>> 10 * 0.25

Gib sie in der Konsole ein und untersuche das Ergebnis.

Aufgabe 3: Operatoren
---------------------

Welche Berechnungen haben 8 als Ergebnis?

.. code:: python3

   >>> 4 - -4
   >>> 65 // 8
   >>> 17 % 9
   >>> 64 ** 0.5

Gib die Anweisungen ein und untersuche das Ergebnis.


Aufgabe 4: Variablen
---------------------

Um Zahlen und Rechenergebnisse für spätere Berechnungen aufzuheben, kannst Du sie in **Variablen** speichern.

Fülle die Lücken:

.. code:: python3

   >>> aepfel = 25
   >>> bananen = 7
   >>> kirschen = 5
   >>> aepfel
   ___
   >>> bananen + 1
   ___
   >>> 3 * kirschen
   ___


Aufgabe 5: Variablen verändern
------------------------------

Die erste Anweisung verändert den Inhalt einer Variablen aus Aufgabe 4. Setze Werte und Variablen ein, so dass das Ergebnis stimmt:

.. code:: python3

   >>> aepfel = aepfel + 1
   >>> aepfel
   ___

   >>> obst = ___ + ___ + ___
   >>> obst
   38

.. hint::

   Wenn du im interatkiven Modus nur den Namen einer Variable eingibst, kannst du den Inhalt sehen.


Aufgabe 6: Zuweisungen
----------------------

Welche Zuweisungen an Variablen sind korrekt?

.. code:: python3

   a = 1 * 2
   2 = 1 + 1
   5 + 6 = y
   sieben = 3 * 4


Aufgabe 7: Kaninchen-Multiplikation
-----------------------------------

Im April hast Du 10 Kaninchen:

.. code:: python3

   kaninchen = 10

Die Kaninchen vermehren sich ständig.
Jeden Monat kommen 20% neue Kaninchen dazu, so dass Du im Mai schon 12 hast.

**Wie viele Kaninchen sind es im Dezember?**

Es sterben keine Kaninchen.
Rechne mit ganzen Zahlen oder Kommazahlen.
Verwende Python um die Aufgabe zu lösen.


.. hint::
   
   Du kannst gerne die gleiche Anweisung mehrfach schreiben.

.. |image0| image:: calculator.png


Reflection Questions
--------------------

* Welche arithmetischen Operatoren kennt Python?
* Was ist eine Variable?
* Was tut der Operator ``=`` ?
* Wie kannst du den Wert zweier Variablen vertauschen?
