
Pinguine Plotten
================

.. figure:: penguin_heads.png

In der folgenden Übung kannst du einige typische ``pandas``-Befehle ausprobieren.

Aufgabe 1: Jupyter Notebooks
----------------------------

Installiere einige Bibliotheken:

::

    pip install polars seaborn
    pip install fastexcel xlsxwriter
    pip install pyarrow

Jupyter starten
---------------

Starte nun die interaktive Jupyter-Umgebung. Diese eignet sich für die Datenanalyse deutlich besser als ``.py``-Dateien.
Gib dazu im Terminal ein:

::

    jupyter notebook

Es sollte ein Browser-Fenster aufgehen.
Erstelle ein neues Notebook mit dem Knopf **New -> Python3**

Aufgabe 2: Der Pinguin-Datensatz
--------------------------------

Lade nun einen Datensatz über Pinguine aus der CSV-Datei :download:`penguins.csv`.
Füge folgenden Code in die oberste Zelle ein. Verwende den **Ausführen**-Knopf oder **Umschalt+Enter**:

.. code:: python3

   import seaborn as sns
   import polars as pl

   df = pl.read_csv("penguins.csv")
   df

Du solltest einen Auszug aus der Tabelle sehen.

Aufgabe 3: Dateninspektion
--------------------------

Probiere folgende Befehle *einzeln*:

.. code:: python3

   df.head()
   df.shape

Aufgabe 4: Speichern
--------------------

Speichere die Daten wieder ab:

.. code:: python3

   df.write_csv("pingus.csv")
   df.write_excel("pingus.xlsx") 

Aufgabe 5: Kategorien auszählen
-------------------------------

Eine Spalte enthält die Spezies der Pinguine, eine kategorische Variable:

.. code:: python3

   df["species"]

Schaue nach wie viele Pinguine jeder Art es im Datensatz gibt:

.. code:: python3

   df["species"].value_counts()
   
Solche kurzen Daten lassen sich gut als Balkendiagramm darstellen:

.. code:: python3
   
   count = df["species"].value_counts()
   sns.barplot(data=count, x="species", y="count")

Aufgabe 6: Pivot-Tabellen
-------------------------

Du kannst auch nach einer Kategorie **aggregieren**:

.. code:: python3

   df.group_by(by="species").mean()

Eine Aggregation nach zwei Kategorien nennt man eine **Pivot-Tabelle**:

.. code:: python3

   piv = df.pivot(on="species", index="sex", values="bill_length_mm", aggregate_function="mean")
   piv

Auch eine Pivot-Tabelle läßt sich plotten. Allerdings müssen wir die Daten dazu umsortieren:

.. code:: python3

   df_long = piv.unpivot(index="sex", variable_name="species", value_name="bill_length")
   df_long

und

.. code:: python3

   sns.barplot(data=df_long, x="sex", y="bill_length", hue="species")

Aufgabe 7: Weitere Diagramme
----------------------------

Hier sind zwei weitere typische Darstellungsformen:

.. code:: python3

   sns.scatterplot(data=df, x="bill_length_mm", y="bill_depth_mm", hue="species")
   
   sns.boxplot(data=df, y="body_mass_g", hue="species", gap=0.1)
