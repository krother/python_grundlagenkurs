Römische Zahlen
===============

In diesem Kapitel lernst du:
----------------------------

======= ====================================
Bereich Thema
======= ====================================
⚙       ein Dictionary anlegen
⚙       Werte im Dictionary nachschlagen
🔀      Listen als Werte verwenden
🐞      Indexfehler beheben
======= ====================================

Aufgabe 1: Nachschlagen
-----------------------

Wir möchten römische Ziffern in arabische Ziffern umwandeln. Dazu eignet sich ein **Dictionary**, eine neue Datenstruktur.

Führe folgenden Code aus:

.. code:: python3

   werte = {
      "I": 1,
      "V": 5,
      "X": 10,
   }
   print(werte["V"])

Wie unterscheidet sich das Dictionary von einer Liste?

Aufgabe 2: Erkunden
-------------------

Finde heraus, was jeder der Ausdrücke mit dem Dictionary in der Mitte anstellt.

.. figure:: dicts.png
   :alt: dict Übung


Aufgabe 3: Längere Zahlen
-------------------------

Diesmal hast du mehrere Ziffern in der String-Variable `roman`.
Du möchtest den Gesamtwert aller Ziffern berechnen.
Dazu müssen Strings und Dictionaries zusammenarbeiten.
Sortiere die Codezeilen und rücke sie ein:

.. code:: python3

   print(gesamt)
   gesamt += werte[ziffer]
   roman = "XVII"
   for ziffer in roman:
   gesamt = 0
   werte = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
   }


Aufgabe 4: größere Zahlen
-------------------------

Füge dem Dictionary Werte für die übrigen römischen Ziffern hinzu (C, D, M).

Aufgabe 5: die schwierigen Zahlen
---------------------------------

Einige römische Zahlen haben es in sich, weil die Reihenfolge eine Rolle spielt.
So steht `IV` für 4 (fünf minus eins) oder `XC` für 90.
Sorge dafür, dass auch diese Ziffern korrekt umgewandelt werden.
Implementiere den folgenden Algorithmus:

1. Setze den Gesamtwert auf 0
2. Setze die letze betrachtete Ziffer auf `""`
3. Gehe die römischen Ziffern von hinten nach vorne durch
4. Ist die Ziffer größer als die letzte, addiere sie zum Gesamtwert
5. Ist die Ziffer kleiner als dier letzte, ziehe sie vom Gesamtwert arabische
6. Aktualisiere die letzte betrachtete Ziffer

Teste dein Programm mit unterschiedlichen römischen Zahlen.

Aufgabe 6: Navigation
---------------------

Das folgende Programm erlaubt dir von einer Stadt in die nächste zu reisen.
Es sind leider **fünf Bugs** enthalten.
Finde und behebe sie.

.. code:: python3

   staedte = {
       "New York": ["Tokyo", "Delhi", "London"],
       "Poznan": ["London", "Berlin"],
       "London": ["New York", "Poznan"]
       "Berlin": ["Tokyo", "Poznan"],
       "Tokyo": ["New York" "Berlin"],
       "Delhi": ["Katmandu"]
       }

   standort = "Berlin"
   print "\nZiel: fliege nach Katmandu\n"

   while standort in staedte and standort == 'Katmandu':
       print(f"Du bist in {standort}")

   print("Es gibt Verbindungen nach ", staedte["standort"])
   standort = input("Wohin möchtest du reisen?")

   print("Du hast dein Ziel erreicht.")


Reflexionsfragen
----------------

-  Wie kannst du ein Dictionary erstellen?
-  Welche Datentypen funktionieren als Schlüssel?
-  Welche Datentypen funktionieren als Werte?
-  Wie kannst Du Werte in einem Dictionary verändern?
-  Kannst Du eine for-Schleife über ein Dictionary laufen lasssen?
