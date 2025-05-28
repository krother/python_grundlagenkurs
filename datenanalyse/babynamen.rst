
Babynamen in den USA
====================

Die US-Meldebehörden haben die Namen aller seit 1880 geborenen US-Staatsbürger registriert. Der Datensatz ist öffentlich unter `www.ssa.gov/oact/babynames/limits.html <http://www.ssa.gov/oact/babynames/limits.html>`__ zugänglich.
Aus Datenschutzgründen sind nur Namen, die mindestens 5 Mal verwendet wurden, im Datensatz aufgeführt.


Vorbereitungen
--------------

Lade den Datensatz der U.S.-Babynamen von [www.ssa.gov/oact/babynames/limits.html](https://www.ssa.gov/oact/babynames/limits.html) herunter (die nationalen Daten).

Entpacke die Datei

Aufgabe 1
---------

Lies die Datei **'yob2000.txt'** mit pandas ein:

.. code:: python3

   import pandas as pd

   df = pd.read_csv("yob2000.txt", columns=["name", "geschlect", "anzahl"])

Aufgabe 2
---------

Inspiziere die Daten mit:

.. code:: python3

   df.shape

und

.. code:: python3

   df.head()


Aufgabe 3
---------

Berechne die Summe der dritten Spalte:

.. code:: python3

   df["anzahl"].sum()

Probiere statt `sum()` auch die Funktionen `mean()`, `std()` und `describe()`


Aufgabe 4
---------

Zähle die Anzahl unterschiedlicher Jungen- und Mädchennamen:

.. code:: python3

   df["geschlecht"].value_counts()


Aufgabe 5
---------

Wähle die Mädchennamen aus:

.. code:: python3

   f = df[df["geschlecht"] == "F"]

Untersuche diese Teilmenge wie in Aufgabe 3.


Aufgabe 6
---------

Ermittle Namen die besonders häufig vorkommen:

.. code:: python3

   top = df[df["anzahl"] > 10000]

Gib die Namen aus.


Aufgabe 7
---------

Finde einen bestimmten Namen in der Tabelle, z.B. deinen eigenen.

Aufgabe 8
---------

Erstelle eine neue Spalte mit dem prozentualen Anteil für jeden Namen:

.. code:: python3

   df["prozent"] = 100 * df["anzahl] / df["anzahl"].sum()

Sichte das Ergebnis.


Aufgabe 10
----------

Hier ist ein Stück Code, der alle Jahrgänge einliest:

.. code:: python3

   import os
   import pandas as pd

   daten = []
   pfad = "daten/"
   for fn in os.listdir(pfad):
       if fn.startswith("yob"):
           df = pd.read_csv(pfad + fn, columns=["name", "geschlect", "anzahl"])
           df["jahr"] = int(fn[3:7])
           daten.append(df)
   df = pd.concat(daten)

Du solltest eine riesige Tabelle mit den Daten aller Jahrgänge erhalten.
Prüfe die Anzahl Zeilen und Spalten mit ``df.shape``. Es sollten vier Spalten und über 1 Mio Zeilen sein.

Aufgabe 11
----------

Untersuche die Beliebtheit der Vornamen einiger US-Promis im Verlauf der letzten 130 Jahre.
Gib Übereinstimmungen für einen Namen mit *Jahr* und *Anzahl* auf dem Bildschirm aus.

Folgende Promis könnten interessant sein:

============== =========================================
Name            Kommentar                     
============== =========================================
Lance           Mensch auf dem Mond
Madonna         Hitsingle "Like a Prayer"
Barack          Präsident
Katrina         Hurrikan in New Orleans
Luke            Jedi
Frida           Malerin, Biographie als Broadway-Musical
Arielle         Meerjungfrau, Biographie von Walt Disney verfilmt
Harley          Motorrad
Wednesday       Wochentag
============== =========================================

Du kannst einen Teildatensatz mit folgenden Zeilen plotten.
Dazu sollte nur ein Name und ein Geschlecht vorliegen.

.. code:: python3

   s = df.set_index("jahr")
   s["anzahl"].plot()


Aufgabe 12
----------

Hier sind einige weitere Ideen:

Der Anfangsbuchstabe als Spalte:
++++++++++++++++++++++++++++++++

.. code:: python3

   df["erster"] = df["name"].str[0]

Länge des Namens
++++++++++++++++

.. code:: python3

   df["laenge"] = df["name"].length

