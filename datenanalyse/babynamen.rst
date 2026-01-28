
Babynamen in den USA
====================

Die US-Meldebehörden haben die Namen aller seit 1880 geborenen US-Staatsbürger registriert. Der Datensatz ist öffentlich unter `www.ssa.gov/oact/babynames/limits.html <http://www.ssa.gov/oact/babynames/limits.html>`__ zugänglich.
Aus Datenschutzgründen sind nur Namen, die mindestens 5 Mal verwendet wurden, im Datensatz aufgeführt.


Vorbereitungen
--------------

Lade den Datensatz der U.S.-Babynamen von `www.ssa.gov/oact/babynames/limits.html <https://www.ssa.gov/oact/babynames/limits.html>`__ herunter (die nationalen Daten).

Entpacke die Datei.

Aufgabe 1
---------

Lies die Datei **'yob2000.txt'** mit `polars`pandas ein:

.. code:: python3

   import polars as pl

   df = pl.read_csv("babynames/yob2000.txt",
                    has_header=False,
                    new_columns=["name", "geschlecht", "anzahl"]
                    )


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

Berechne die Anzahl Geburten insgesamt:

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

   f = df.filter(geschlecht="F")

Untersuche diese Teilmenge wie in Aufgabe 3.


Aufgabe 6
---------

Ermittle Namen die besonders häufig vorkommen:

.. code:: python3

   top = df.filter(pl.col("anzahl") > 10000)

Gib die Namen aus.


Aufgabe 7
---------

Finde einen bestimmten Namen in der Tabelle, z.B. deinen eigenen.

Aufgabe 8
---------

Erstelle eine neue Spalte mit dem Jahr:

.. code:: python3

   df = df.with_columns(jahr=2000)

Erstelle eine neue Spalte mit dem prozentualen Anteil für jeden Namen:

.. code:: python3

   df = df.with_columns(perc = 100 * df["anzahl"] / df["anzahl"].sum())

Sichte das Ergebnis.


Aufgabe 10
----------

Hier ist ein Stück Code, der alle Jahrgänge einliest:

.. code:: python3

   import os

   daten = []
   pfad = "daten/"
   for fn in os.listdir(pfad):
       if fn.startswith("yob"):
           df = pl.read_csv(pfad + fn,
                    has_header=False,
                    new_columns=["name", "geschlecht", "anzahl"]
                    )
           df = df.with_columns(jahr=int(fn[3:7]))
           daten.append(df)
   df = pl.concat(daten)

Du solltest eine riesige Tabelle mit den Daten aller Jahrgänge erhalten.
Prüfe die Anzahl Zeilen und Spalten mit ``df.shape``. Es sollten vier Spalten und über 2 Mio Zeilen sein.

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
Khaleesi        Berufsbezeichnung bei "Game of Thrones"
Wednesday       Wochentag
============== =========================================

Du kannst einen Teildatensatz mit folgenden Zeilen plotten.
Filtere dazu nach Name und ein Geschlecht.

.. code:: python3

   promi = df.filter(...)
   sns.lineplot(promi, x="jahr", y="anzahl")

Aufgabe 12
----------

Hier sind einige weitere Ideen.
Du kannst mit den zusätzlichen Spalten weitere Pivot-Tabellen generieren.

Der Anfangsbuchstabe als Spalte:
++++++++++++++++++++++++++++++++

.. code:: python3

   dd = dd.with_columns(first=dd["name"].str.slice(0, 1))
   
Länge des Namens
++++++++++++++++

.. code:: python3

   dd = dd.with_columns(length=dd["name"].str.len_chars())
   
Hier ist ein Beispiel für eine Längenstatistik:

.. code:: python3

   lengthstat = dd.pivot(on="geschlecht", index="length", values="anzahl", aggregate_function="len")
