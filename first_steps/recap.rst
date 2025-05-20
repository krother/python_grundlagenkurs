Aufgabe 3: Suche
----------------

Die folgende `for`-Schleife sucht nach der Zahl `33` in den Daten.
Ändere den Code, so dass stattdessen `while` verwendet wird.

.. code:: python3

   data = [5, 7, 33, 12, 4, 3, 18]

   gefunden = False
   for n in data:
       if n == 33:
           gefunden = True

   print(f"Der Wert 33 wurde gefunden: {gefunden}")


Aufgabe 4: Zählen
-----------------

Die folgende `while`-Schleife zählt Zahlen über 10.
Ändere den Code, so dass eine `for`-Schleife verwendet wird.

.. code:: python3

   data = [4, 7, 11, 1, 3,  15]

   i = 0
   ergebnis = 0
   while i < len(data):
       if data[i] > 10:
           ergebnis += 1
       i += 1

   print(f"Es gibt {ergebnis} Werte über 10.")


Aufgabe 6: Endlosschleifen
--------------------------

Welche der folgenden Schleifen beenden von selbst?

.. code:: python3

   count = 0
   while count > 0:
       print count
       count += 1


   text = "a"
   while "z" not in text:
       text += "a"


   n = 0
   while n * 5 != n ** 2:
       n += 2
