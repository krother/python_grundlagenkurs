Ada Lovelace
============

.. figure:: ada.jpg
   :alt: Ada Lovelace

`Ada Lovelace, image by Alfred Edward Chalon - public
domain <https://commons.wikimedia.org/w/index.php?curid=25519820>`__

**Ada Lovelace** was the first human to write a computer program.
This was quite an achievement, given that Ada had to imagine a computer first!


In this chapter you will:
-------------------------

==== =================================
area topic
==== =================================
🚀   calculate the age of Ada Lovelace
⚙    distinguish data types
💡    use the data type ``float``
💡    convert data types
🐞    recognize bugs at runtime
==== =================================


Exercise 1: Ada Lovelace
------------------------

Insert the following pieces into the gaps, so that all instructions are
executed correctly: ``age``, ``int(age)``, ``name``, ``str(born)``,
``1815``

.. code:: python3

   name = "Ada Lovelace"
   born = ...
   ...  = "37"

   text = ... + " was born in the year " + ... + "."
   year = born + ...
   print(text)
   print(year)

.. hint::

   Python contains many functions for **type conversion**.
   With the functions ``int()``, ``float()`` and ``str()`` you can convert
   numbers and strings into each other.


Exercise 2: Nine plus nine
--------------------------

Insert ``int()`` or ``str()`` into the instructions,
so that all of them run without an error.

.. code:: python3

   9 + 9
   9 + "9"
   "9" + "9"
   9 * "9"


Exercise 3: Output
------------------

Which ``print`` statements work?

.. code:: python3

   print("9" + "9")
   print "nine"
   print(str(9) + "nine")
   print(9 + 9)
   print(9 + int("9"))
   print(nine)
   print(float("9") + int(9.0))


Exercise 4: Debugging
---------------------

The following code should calculate the age of Ada in a year entered by
the user. It contains three bugs. Find and fix them.

.. code:: python3

   year_of_birth = 1815
   year = input('Which year is it? ')
   age = year_of_birth - year

   print("Today, Ada Lovelace would be " + age + " years old.")    


Exercise 5: Age Calculator
--------------------------

Write a program where you can enter the year in which you were born.
The program should calculate your age on January 1st of this year.

Use the following code to calculate the current year:

.. code:: python3

   import time

   time.time() // (365 * 24 * 60 * 60) + 1970

.. hint::

   ``time`` is a Python module. It contains useful functions.

   ``time.time()`` is a function in that module.
   It returns the number of seconds since January 1st, 1970
   (called the Unix Epoch, the 0 AD of computers).


Reflection Questions
--------------------

* which variable types have you seen so far?
* what does a type conversion function do?
* what is a ``TypeError``?


Hier ist die vollständige deutsche Übersetzung deines Textes:

---

Ada Lovelace
============

.. figure:: ada.jpg
   :alt: Ada Lovelace

`Ada Lovelace, Bild von Alfred Edward Chalon – gemeinfrei <https://commons.wikimedia.org/w/index.php?curid=25519820>`

**Ada Lovelace** war der erste Mensch, der ein Computerprogramm geschrieben hat.
Das war eine erstaunliche Leistung – vor allem, weil Ada sich erst einmal einen Computer vorstellen musste!

In diesem Kapitel lernst du:
----------------------------

======= ===========================================
Bereich Thema
======= ===========================================
🚀     das Alter von Ada Lovelace berechnen
⚙      Datentypen unterscheiden
💡     den Datentyp `float` verwenden
💡     Datentypen ineinander umwandeln
🐞     Laufzeitfehler erkennen
======= ===========================================


Aufgabe 1: Ada Lovelace
-----------------------

Setze die folgenden Teile in die Lücken ein, so dass alle Befehle korrekt ausgeführt werden:
`age`, `int(age)`, `name`, `str(born)`, `1815`

.. code:: python3

   name = "Ada Lovelace"
   born = ___
   ___ = "37"
   
   text = ___ + " wurde im Jahr " + ___ + " geboren."
   year = born + ___
   print(text)
   print(year)

.. hint::

   Python enthält viele Funktionen zur **Typumwandlung**.
   Mit den Funktionen `int()`, `float()` und `str()` kannst du Zahlen und Zeichenketten (Strings) ineinander umwandeln.

Aufgabe 2: Neun plus neun
-------------------------

Füge `int()` oder `str()` in die Anweisungen ein, sodass sie fehlerfrei ausgeführt werden können.

.. code:: python3

   9 + 9
   9 + "9"
   "9" + "9"
   9 * "9"


Aufgabe 3: Ausgabe
------------------

Welche der folgenden `print`-Anweisungen funktionieren?

.. code:: python3

   print("9" + "9")
   print "neun"
   print(str(9) + "neun")
   print(9 + 9)
   print(9 + int("9"))
   print(neun)
   print(float("9") + int(9.0))

Aufgabe 4: Debugging
--------------------

Der folgende Code soll das Alter von Ada in einem vom Benutzer eingegebenen Jahr berechnen.
Er enthält **drei Fehler**. Finde und korrigiere sie.

.. code:: python3

   geburtsjahr = 1815
   jahr = input('Welches Jahr schreiben wir? ')
   alter = geburtsjahr - jahr
   
   print("Heute wäre Ada Lovelace " + alter + " Jahre alt.")


Aufgabe 5: Altersrechner
------------------------

Schreibe ein Programm, bei dem du das Jahr deiner Geburt eingeben kannst.
Das Programm soll dann dein Alter zum 1. Januar dieses Jahres berechnen.

Du kannst folgenden Code verwenden, um das aktuelle Jahr zu berechnen:

.. code:: python3

   import time
   
   jahr = time.time() // (365 * 24 * 60 * 60) + 1970

.. hint::

   `time` ist ein Python-Modul. Es enthält viele    nützliche Funktionen.
   
   `time.time()` ist eine Funktion in diesem Modul.
   Sie gibt die Anzahl der Sekunden zurück, die seit dem    1. Januar 1970 vergangen sind
   (dieses Datum wird auch „Unix-Epoche“ genannt – so  etwas wie das Jahr 0 für Computer).

Reflexionsfragen
----------------

* Welche Datentypen hast du bisher kennengelernt?
* Was macht eine Typumwandlungsfunktion?
* Was ist ein `TypeError`?
