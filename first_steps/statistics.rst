Statistik
=========

Wenn man alle Anweisungen in ein einzigen Anweisungsblock schreibt, entstehen Programme, die schwer zu verstehen und zu debuggen sind.
In diesem Kapitel lernst du, den Code in **Funktionen**, also kleinere Einheiten aufzuteilen.

In diesem Kapitel lernst du:
----------------------------

======= ==============================================
Bereich Thema
======= ==============================================
🚀       Statistiken berechnen
⚙        eine Funktion implementieren
⚙        eine selbst definierte Funktion aufrufen
💡       das Modul ``math`` verwenden
💡       die Funktion ``sum`` verwenden
🔀       eine rekursive Funktion nutzen
======= ==============================================


Aufgabe 1: Aufsummieren
-----------------------

Schreibe eine Funktion, die die Summe einer Liste von Zahlen berechnet. Füge in die Lücken ein: ``zahlen``, ``daten``, ``def``, ``return``, ``calc_sum``, ``+=``

.. code:: python3

   ____ calc_sum(daten):
       total = 0
       for n in ____:
           total ____ n
       ____ total

   zahlen = [12562, 2178, 342, 129, 384, 208, 164, 82, 41]
   s = ____(____)
   print(s)


Aufgabe 2: Mittelwert
---------------------

Schreibe eine Funktion, die den arithmetischen Mittelwert der folgenden Zahlen berechnet:

.. code:: python3

   def mean(data):
       ...

   numbers = [12562, 2178, 342, 129, 384, 208, 164, 82, 41]

   ...

Vergiss den ``return``-Befehl nicht.


Aufgabe 3: Abkürzung
--------------------

Vereinfache die Mittelwertfunktion, indem du die Funktion ``sum()`` verwendest.

Du kannst deine eigene oder die eingebaute ``sum()``-Funktion verwenden.


Aufgabe 4: Standardabweichung
-----------------------------

Das folgende Programm berechnet die Standardabweichung einer Zahlenliste.  
Du möchtest den Code verallgemeinern, sodass er mit anderen Datensätzen funktioniert.  
Verpacke den Berechnungsteil – aber nicht die Daten – in eine Funktion.

.. code:: python3

   import math

   data = [12562, 2178, 342, 129, 384, 208, 164, 82, 41]

   mittelwert = mean(data)

   summe = 0.0
   for n in data:
       summe += (n - mittelwert) ** 2
   varianz = summe / len(data)
   stabw = math.sqrt(varianz)

   print(f"Standardabweichung: {stabw:8.2f}")


Aufgabe 5: Optionale Parameter
------------------------------

Erkläre das Programm:

.. code:: python3

   def add(a=2, b=2):
       return a + b

   print(add(3, 3))
   print(add(3))
   print(add())
   print(add(b=4))


Aufgabe 6: Rekursion
--------------------

Erkläre den folgenden Code:

.. code:: python3

   def factorial(n):
       """Berechnet die Fakultät der angegebenen Zahl."""
       if n > 1:
           return n * factorial(n - 1)
       else:
           return 1

   x = int(input('Bitte gib eine Zahl ein: '))
   y = factorial(x)
   print(f"Das Ergebnis ist:\n{x}! = {y}")


Reflexionsfragen
----------------

-  Warum ist es sinnvoll, Funktionen zu schreiben?
-  Was muss in einer Funktionsdefinition stehen?
-  Wie ruft man eine Funktion auf?
-  Was macht die ``return``-Anweisung?
