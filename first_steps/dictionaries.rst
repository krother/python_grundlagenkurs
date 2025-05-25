Preise nachschlagen
===================

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

Wir möchten Einkaufspreise für Obst nachschlagen. Dazu eignet sich ein **Dictionary**, eine neue Datenstruktur.

Führe folgenden Code aus:

.. code:: python3

   preise = {
      "Apfel": 0.50,
      "Banane": 1.00,
      "Orange": 1.50,
      "Kirschen": 3.00,
   }
   print(preise["Banane"])

Wie unterscheidet sich das Dictionary von einer Liste?

Aufgabe 2: Erkunden
-------------------

Finde heraus, was jeder der Ausdrücke mit dem Dictionary in der Mitte anstellt.

.. figure:: dicts.png
   :alt: dict Übung


Aufgabe 3: Listenverarbeitung
-----------------------------

Diesmal hast du eine Liste von Einkäufen in der Variable `einkauf`.
Du möchtest den Gesamtpreis berechnen.
Dazu müssen Listen und Dictionaries zusammenarbeiten.
Sortiere die Codezeilen und rücke sie ein:

.. code:: python3

   print(gesamt)
   gesamt += preise[frucht]
   einkauf = ["Banane", "Banane", "Kirschen", "Apfel", "Apfel", "Banane"]
   for frucht in einkauf:
   gesamt = 0
   preise = {
      "Apfel": 0.50,
      "Banane": 1.00,
      "Orange": 1.50,
      "Kirschen": 3.00,
   }


Aufgabe 4: Navigation
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
