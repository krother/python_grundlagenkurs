Schere-Stein-Papier
===================

|image0|

`Bild von Enzoklop, CC BY-SA
3.0 <https://commons.wikimedia.org/w/index.php?curid=27958795>`__


In diesem Kapitel lernst du:
----------------------------

======= =============================================
Bereich Thema
======= =============================================
🚀      ein *Schere-Stein-Papier*-Spiel programmieren
⚙       Verzweigungen mit `if` schreiben
⚙       Vergleichsoperatoren benutzen
💡      den Datentyp `bool` verwenden
🔀      eine Zustandsvariable einsetzen
🐞      Einrückungsfehler erkennen
======= =============================================

Ein wichtiges Strukturelement in einem Programm ist das *Treffen von Entscheidungen*.
In Python entscheidet die Anweisung `if`, welche Anweisung als Nächstes ausgeführt wird.

Aufgabe 1: Entscheidung
-----------------------

Mit der `if`-Anweisung kannst Du im Programm Entscheidungen treffen.

Teste das folgende Programm mit unterschiedlichen Eingaben:

.. code:: python3

   spieler = input("Bitte gib R, P oder S ein (für [R]ock, [P]aper, [S]cissors): ")
   computer = "P"
   
   if spieler == computer:
       print("Unentschieden")

Aufgabe 2: Alternative Entscheidungen
-------------------------------------

Füge `if`, `elif` und `else` an den richtigen Stellen im Code ein, damit er funktioniert:

.. code:: python3

   import random
   
   spieler = input("Bitte gib R, P oder S ein (für [R]ock, [P]aper, [S]cissors): ")
   computer = random.choice('RPS')
   
   ___ spieler == 'R' and computer == 'P':
       print("Computer gewinnt")
   ___ spieler == 'R' and computer == 'S':
       print("Spieler gewinnt")
   ___:
       print("Unentschieden")


Aufgabe 3: Papier
-----------------

Erweitere das Programm so, dass es auch funktioniert, wenn der Spieler *Papier* wählt.

Aufgabe 4: Debugging
--------------------

Behebe jeweils einen Fehler in jedem der folgenden Entscheidungsblöcke:

.. code:: python3

   elif spieler.upper() not in 'RPS':
       print('Ungültige Eingabe. Bitte gib R, P oder S ein.')
   
   elif spieler == computer
       print('Du hast das Gleiche gewählt wie ich.')
   
   if spieler = 'S':
       print('Du hast "Schere" gewählt.')
   
   else:
   print('Du hast etwas anderes als "Schere" gewählt.')


Aufgabe 5: Ausdrücke
--------------------

Welche der folgenden booleschen Ausdrücke ergeben den Wert `True`?

.. code:: python3

   a = 3
   b = 4
   c = 7
   
   print(a + b < c)
   
   print(a + b == 5 + 2)
   
   print(a * b == 12 and b * c == 28)
   
   print(a + b * c >= 28)
   
   print(a + b == "7")


Aufgabe 6: Zustandsvariablen
----------------------------

Das folgende Programm speichert das Ergebnis eines Vergleichs in einer `bool`-Variablen.
Vervollständige den Code:

.. code:: python3

   spieler_gewinnt = (
                    (spieler == "R" and computer == "S")     or
                    (spieler == "P" and ___) or
                    (___)
                  )

    if spieler_gewinnt:
        print('Du hast gewonnen!')


Aufgabe 7: Verschachtelte if-Anweisungen
----------------------------------------

Vervollständige das Programm so, dass es alle möglichen Situationen abdeckt:

.. code:: python3

   winner = 'Unentschieden'
   
   if spieler == "S":
       if computer == "P":
           winner = "Spieler"
       elif computer == "R":
           winner = "Computer"
   
   elif spieler == "P":
       ___
   
   print("Der Gewinner ist:", winner)
   

.. hint::

   Ein *verschachteltes if* ist ein `if` innerhalb eines anderen `if`-Blocks.

Aufgabe 8: Schere-Stein-Papier
------------------------------

Vervollständige das Schere-Stein-Papier-Spiel.

Optionale Ziele:
----------------

* berücksichtige Unentschieden als Möglichkeit
* sowohl Gross- als auch Kleinbuchstaben sind als Eingabe möglich
* verwende einen einzigen `if..elif..else` Block
* erweitere das Spiel durch [Eidechse und Spock](https://en.wikipedia.org/wiki/Rock_paper_scissors#Additional_weapons)
* verwende Zustandsvariablen, so dass nur eine oder zwei `if`-Anweisungen (ohne `elif` oder `else`) übrig bleiben

Reflexionsfragen
----------------

* In welcher Reihenfolge müssen die Teile einer `if`-Anweisung stehen?
* Welche Teile einer `if`-Anweisung sind optional?
* Was ist eine *Einrückung*?
* Welche *Vergleichsoperatoren* kennst du bereits?

.. |image0| image:: rock_paper_scissors.svg
