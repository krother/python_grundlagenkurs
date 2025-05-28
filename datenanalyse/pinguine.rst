
Pinguine Plotten
================

.. figure:: penguin_heads.png

In der folgenden Übung kannst du einige typische ``pandas``-Befehle ausprobieren.

Aufgabe 1: Jupyter Notebooks
----------------------------

Installiere einige Bibliotheken:

::

    pip install pandas seaborn
    pip install openpyxl
    pip install jupyter

Starte nun die interaktive Jupyter-Umgebung. Diese eignet sich für die Datenanalyse deutlich besser als ``.py``-Dateien.

::

    jupyter notebook

Erstelle ein neues Notebook mit dem Knopf **New -> Python3**

Aufgabe 2: Der Pinguin-Datensatz
--------------------------------

Füge folgenden Code in die oberste Zelle ein. Verwende den **Ausführen**-Knopf oder **Umschalt+Enter**:

.. code:: python3

   import seaborn as sns
   import pandas as pd

   df = sns.load_dataset("penguins")
   df

Du solltest einen Auszug aus der Tabelle sehen.

Aufgabe 3: Dateninspektion
--------------------------

Probiere folgende Befehle einzeln:

.. code:: python3

   df.head()
   df.shape
   df.info()

Aufgabe 4: Speichern
--------------------

Speichere die Daten wieder ab:

.. code:: python3

   df.to_csv("pinguine.csv")
   df.to_excel("pinguine.xlsx") 

Aufgabe 5: Kategorien auszählen
-------------------------------

Schaue nach wie viele Pinguine jeder Art es im Datensatz gibt:

.. code:: python3

   df["species"].value_counts()
   
Solche kurzen Daten lassen sich gut als Plot darstellen:

.. code:: python3
   
   df["species"].value_counts().plot.bar()

Aufgabe 6: Pivot-Tabellen
-------------------------

Du kannst nach einer oder mehreren Kategorien auch gruppieren. 
Dies nennt man eine **Pivot-Tabelle**:

.. code:: python3

   pd.pivot_table(data=df, index="species", values="bill_length_mm", aggfunc="mean")
   pd.pivot_table(data=df, index="species", columns="sex", 
                  values="bill_length_mm", aggfunc="mean")

Auch eine Pivot-Tabelle läßt sich gut plotten:

.. code:: python3

   pivot = pd.pivot_table(data=df, index="species", columns="sex", 
                          values="bill_length_mm", aggfunc="mean")
   pivot.plot.bar()

Aufgabe 7: Weitere Diagramme
----------------------------

Hier sind zwei weitere typische Darstellungsformen:

.. code:: python3

   sns.scatterplot(data=df, x="bill_length_mm", y="bill_depth_mm", hue="species")
   
   sns.boxplot(data=df, y="body_mass_g", hue="species", gap=0.1)
