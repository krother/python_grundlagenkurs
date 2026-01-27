
Balkendiagramme plotten
=======================

Schritt 1
---------

Lade die Datei :download:`gapminder_total_fertility.csv` in pandas.

.. code:: python3

    import polars as pl

    df = pd.read_csv('gapminder_total_fertility.csv', index_col=0)

Sichte die Daten.

Schritt 2
---------

Benenne die erste Spalte um:

.. code:: python3
    
   df = df.rename({"Total fertility rate": "land"})

Sortiere die Daten in ein **langes Format** um:

.. code:: python3

   df = df.unpivot(index="Total fertility rate", variable_name="jahr", value_name="fruchtbarkeit")

Wandle das Jahr in Zahlen um:

.. code:: python3

   df = df.with_columns(jahr=df["jahr"].cast(int))

Schliesslich werfen wir noch alle leeren Werte aus der Tabelle:

.. code:: python3

   df = df.drop_nulls()

Schritt 3
---------

Wähle 4 Länder aus dem `DataFrame`aus:

.. code:: python3

    laender = df.filter(pl.col("land").is_in(["Germany", "Kenya", "India", "Brazil"]))

Damit kannst du schon eine Zeitreihe plotten:

.. code:: python3

   sns.lineplot(data=laender, x="jahr", y="fruchtbarkeit", hue="land")

Schritt 3
---------

Wähle 3 Jahrgänge aus dem `DataFrame` aus, z.B.:

.. code:: python3

    jahre = laender.filter(...)

Schritt 4
---------

Zeichne ein Balkendiagramm mit mehreren Gruppen.
Setze Spaltennamen in die Lücken ein:

.. code:: python3

    from matplotlib import pyplot as plt

    sns.barplot(jahre, x="...", y="...", hue="...")
    plt.savefig('balken.png')
