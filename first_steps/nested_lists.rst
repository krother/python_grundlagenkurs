Verschachtelte Listen
=====================

In diesem Kapitel lernst du:
----------------------------

======= ====================================================================
Bereich Thema
======= ====================================================================
⚙        eine Liste in einer Liste definieren
⚙        eine verschachtelte Liste indexieren
🔀       über eine verschachtelte Liste iterieren
🔀       eine verschachtelte Liste mit einer geschachtelten Schleife erzeugen
======= ====================================================================

Daten liegen häufig in Tabellenform vor.  
Um Tabellen in Python zu verarbeiten, können wir Listen in anderen Listen ablegen.  
Diese nennt man **verschachtelte Listen**:

.. code:: python3

   table = [
       ["Emma", 20799],
       ["Olivia", 19674],
       ["Sophia", 18490],
       ["Isabella", 16950],
       ["Ava", 15586],
       ["Mia", 13442],
       ["Emily", 12562],
   ]

Für verschachtelte Listen gelten im Allgemeinen dieselben Regeln wie für einfache Listen.
Zum Beispiel kannst du die dritte Zeile anzeigen mit:

.. code:: python3

   print(table[2])
  
Um auf ein einzelnes Element zuzugreifen, benötigst du zwei eckige Klammerpaare.  
Zum Beispiel für die zweite Spalte der dritten Zeile:

.. code:: python3

   print(table[2][1])

In diesem Kapitel wirst du verschachtelte Listen erzeugen und verarbeiten.


Aufgabe 1
---------

Gib alle Zeilen der obigen Tabelle mit einer ``for``-Schleife auf dem Bildschirm aus.

Vervollständige den Code:

.. code:: python3

   for ___ in table:
       print(___)


Aufgabe 2
---------

Ändere nun die Schleife so, dass nur die Namen ausgegeben werden.


Aufgabe 3
---------

Gib jede einzelne *Zelle* der Tabelle mit einer geschachtelten ``for``-Schleife aus.

Vervollständige den Code:

.. code:: python3

   for zeile in ___:
       ___ wert in zeile:
           print(___)


Aufgabe 4
---------

Erzeuge eine leere Tabelle mit 10 x 10 Zellen und fülle sie mit den Zahlen von 1 bis 100.
Sortiere dazu die Zeilen und rücke den Code korrekt ein:

.. code:: python3

   for x in range(10):
   for y in range(10):
   zahl = 1
   zahl += 1
   print(table)
   zeile = []
   zeile.append(zahl)
   table.append(zeile)
   table = []
