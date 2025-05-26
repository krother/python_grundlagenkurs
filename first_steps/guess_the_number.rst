Zahlenraten
===========

In diesem Kapitel lernst du:
----------------------------

======= ==============================================
Bereich Thema
======= ==============================================
🚀      ein Zahlenratespiel schreiben
💡      den Datentyp *string* verwenden
⚙       eine bedingte Schleife implementieren
🐞      Endlosschleifen debuggen
======= ==============================================


Aufgabe 1: Bedingte Schleifen
-----------------------------

In diesem Kapitel lernst Du eine neue Möglichkeit, den *Ablauf* eines Programms (den **Kontrollfluß**) zu steuern: Die bedingte Schleife mit ``while``.
Hier sind drei unvollständige Beispiele für ``while``-Schleifen:

.. code:: python3

   x = 5
   while ___:
       x = x -1
       print("A", x)

   x = 1
   while ___:
       x = 2 * x
       print("B", x)

   x = 0
   while ___:
       x = x + 5
       print("C", x)


Setze die folgenden Ausdrücke ein, so dass jede ``while``-Schleife genau fünf Mal durchlaufen wird:

* ``x <= 20``
* ``x != 0``
* ``x < 30``

.. hint::

   ``print``-Befehle an verschiedenen Stellen sind eine gute Möglichkeit, zu untersuchen, was Dein Programm gerade tut.

Aufgabe 2: Syntax
-----------------

Welche der folgenden `while`-Befehle sind korrekt?

.. code:: python3

   while a = 1:
      ...

   while b == 1
      ...

   while a + 7:
      ...

   while a and (b-2 == c):
      ...


Aufgabe 3: Quadratzahlen
------------------------

Das folgende Programm soll Quadratzahlen ausgeben.
Es landet jedoch in einer **Endlosschleife**.
Finde heraus, wie du das Programm unterbrechen kannst. Behebe den Fehler.

.. code:: python3

   zahl = 1
   while zahl <= 10:
       print(zahl ** 2)


Aufgabe 4: Wiederholung
-----------------------

Mit einer Schleife kannst Du Vorgänge **wiederholen**. Dabei kann ein Schleifendurchlauf das Ergebnis des vorherigen verwenden.
Das folgende Programm verwendet eine **Zählvariable** und ein **Zwischenergebnis**, um Ziffern auszugeben:

.. code:: python3

   ergebnis = ""
   durchlauf = 1
   while durchlauf < 10:
       ergebnis = ergebnis + str(durchlauf)
       durchlauf = durchlauf + 1
   print(ergebnis)

Ändere das Programm, so dass es folgendes:

- starte mit einem Reiskorn auf dem ersten Feld eines Schachbretts
- verdopple die Anzahl Reiskörner auf dem nächsten Feld
- verfahre so für alle 64 Felder
- gib die Anzahl Reiskörner auf dem letzten Feld aus

Aufgabe 5: Zahlenraten
----------------------

Im Spiel **Zahlenraten** versucht der Spieler eine Zahl zu erraten, die sich der Computer ausgedacht hat.
Schreibe das Spiel.

1. Das Programm *"würfelt"* eine Zahl zwischen 1 und 100 aus.
2. Gib die Zahl **nicht** aus.
3. Der Spieler gibt eine Zahl ein.
4. Das Program sagt, ob die Zahl zu groß oder zu klein ist.
5. Wiederhole Schritte 3-5 bis die richtige Zahl erraten wurde.

Verwende folgenden Code zum Auswürfeln der Zahl:

.. code:: python3

   import random

   zahl = random.randint(1, 100)

Beispielausgabe:
----------------

::

   Ich habe mir eine Zahl gemerkt.
   Versuche sie zu erraten.

   Gib eine Zahl ein (1-100): 33
   Meine Zahl ist kleiner.

   Gib eine Zahl ein (1-100): 22
   Meine Zahl ist kleiner.

   Gib eine Zahl ein (1-100): 11
   Meine Zahl ist größer.

   Gib eine Zahl ein (1-100): 17
   Meine Zahl ist kleiner.

   Gib eine Zahl ein (1-100): 14
   Meine Zahl ist kleiner.

   Gib eine Zahl ein (1-100): 13
   Gefunden!
