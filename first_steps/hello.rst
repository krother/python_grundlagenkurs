
Hello World
===========

In diesem Kapitel lernst du:
----------------------------

======= ===============================================
Bereich Thema
======= ===============================================
🚀      ein „Hello World“-Programm in Python schreiben
💡      den Datentyp *String* verwenden
💡      die Funktionen `print()` und `input()` aufrufen
⚙       Text in einer String-Variablen speichern
🔧      Befehle eingeben
🔧      Befehle ändern
🐞      Syntaxfehler finden
======= ===============================================

Aufgabe 1: Dein erstes Programm
-------------------------------

Erstelle eine neue Datei im **Editor-Fenster** und gib folgende Anweisungen ein:

.. code:: python3

   name = input("Wie heißt du? ")
   print("Hallo", name)

Führe das Programm aus, indem du auf den **„Ausführen“**-Knopf rechts oben klickst. Was passiert?

Aufgabe 2: Mache das Programm kaputt!
-------------------------------------

Beim Programmieren ist es unvermeidlich, dass man Fehler macht. Fehler können einfache Tippfehler sein oder komplizierte logische Fehler. Eine der wichtigsten Fähigkeiten beim Programmieren ist es, die Ursache eines Fehlers im Programm zu finden und ihn zu beheben. Du kannst das üben, indem du das Programm absichtlich kaputt machst und beobachtest, was passiert.

Probiere die folgenden fehlerhaften Programme nacheinander aus und versuche die Fehlermeldung zu verstehen:

.. code:: python3

   name = input("Wie heißt du? ")
   pront("Hallo", name)
   
   name = input("Wie heißt du? "
   print("Hallo", name)
   
   name = input("Wie heißt du? ")
   print(Hello , name)

Wie kannst du herausfinden, was passiert ist?

Aufgabe 3: input
----------------

Welche der folgenden `input`-Befehle funktionieren? Probiere sie nacheinander aus (z.B. in der Python-Kommandozeile).

.. code:: python3

   name input("Gib deinen Namen ein: ")
   
   name = input("Gib eine Zahl ein: ")
   
   name = input(git deinen Namen ein)
   
   name = input()

Aufgabe 4: Variablennamen
-------------------------

Probiere aus, welche der folgenden Variablennamen in Python verwendet werden können:

.. code:: python3

   YODA = 'jedi'

   darth vader = 'sith'
   
   luke99 = 'jedi' = 'sith'
   
   2000imperator = 'sith'
   
   obi_wan_kenobi = 'jedi'
   
   darth.maul = 'sith'

Aufgabe 5: Drei Fehler
----------------------

Das folgende Programm soll eine Begrüßung ausgeben.
Es enthält drei Fehler.
Kopiere den Code in deinen Editor.
Dann finde und behebe die Fehler.

.. code:: python3

   teil1 = "Herzlich willkommen,"
   teil2 = "menschlicher Benutzer."
   teil3 = ich wünsche dir viel Erfolg

   text = "teil1 + teil2 + teil3"
   print(text

Aufgabe 6: Begrüßungsprogramm
-----------------------------

Schreibe ein Programm, das nach deinem Vor- und Nachnamen fragt und beides ausgibt.

Reflexionsfragen
----------------

* Woran erkennst du eine Funktion?
* Was kannst du in die Klammern der ``print()``-Funktion schreiben?
* Was für Variablennamen sind erlaubt/nicht erlaubt?
* Was kannst du tun, wenn das Programm nicht funktioniert?
