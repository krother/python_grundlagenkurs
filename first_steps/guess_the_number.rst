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


Aufgabe 1: Bedingte Schleifen Loops
----------------------------

In diesem Kapitel lernst Du eine neue Möglichkeit, den *Ablauf* eines Programms (den **Kontrollfluß**) zu steuern: Die bedingte Schleife mit `while`.

Sortiere die Ausdrücke ein, so dass die ``while``-Schleifen die entsprechende Anzahl von Durchläufen haben.

.. figure:: ../images/while.png
   :alt: while Aufgabe

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

   while len(c) > 10:
      ...

   while a and (b-2 == c):
      ...

   while s.find('c') >= 0:
      ...


Aufgabe 3: Zahlenraten
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
