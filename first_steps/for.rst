Quadratzahlen
=============

|image0|

`Bild von travelnow.or.crylater auf
Unsplash <https://unsplash.com/@travelnow_or_crylater?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText>`__

In diesem Kapitel lernst du:
----------------------------

======= =================================
Bereich Thema
======= =================================
🚀      calculate square numbers
⚙       `for`-Schleifen verwenden
⚙       Anweisungen einrücken
💡      Die Funktion `range()` verwenden
💡      Das Modul `time` verwenden
🐞      Laufzeitfehler erkennen
======= =================================


Aufgabe 1: Motivationsübung
---------------------------

Führe das folgende Programm aus. Was passiert?

.. code:: python3

    import time

    for i in range(5):
        print("Du kannst schon super programmieren!")
        time.sleep(5)


Aufgabe 2: for-Schleife
-----------------------

Was tut das folgende Programm?

.. code:: python3
    
    for zahl in range(1, 7):
        print(zahl)

.. question::

   Warum ist die `for`-Anweisung besser als einfach sieben Mal `print()` zu schreiben?

Aufgabe 3: Einrückung
---------------------

Erkläre den Unterschied zwischen folgenden zwei Programmen:

.. code:: python3
    
    x = 1
    for i in range(10):
        x = x * 2
        print(x)

und

.. code:: python3
    
    x = 1
    for i in range(10):
        x = x * 2
    print(x)


Aufgabe 4: Quadrate
-------------------

Schreibe eine Schleife mit `for`, welche folgende Ausgabe produziert:

::

    1
    4
    9
    16
    25
    36
    49


Aufgabe 6: Sequenzen
--------------------

Probiere folgende Schleifen aus.
Erkläre was passiert.

.. code:: python3
    
    for buchstabe in "ABCD":
        print(buchstabe)

    for i in range(10):
        print(i)

    for zahl in [4, 9, 16, 25]:
        print(zahl)

    kaninchen = 10
    for i in range(9):
         kaninchen = kaninchen + kaninchen // 5
         print(kaninchen)

.. |image0| image:: squares.jpg
