
Balkendiagramme plotten
=======================

Schritt 1
---------

Lade die Datei :download:`gapminder_total_fertility.csv` in pandas.

.. code:: python3

    import pandas as pd

    df = pd.read_csv('gapminder_total_fertility.csv', index_col=0)

Sichte die Daten.

Schritt 2
---------

Wähle 3 Jahrgänge aus den Spalten des `DataFrame` aus, z.B.:

.. code:: python3

    jahre = df[['1950', '1955', '2000']]

Schritt 3
---------

Wähle 4 Länder aus dem Index des `DataFrame`aus, z.B.:

.. code:: python3

    laender = jahre.loc[['Germany', 'India', 'Bulgaria', 'Kenya']]

Schritt 4
---------

Zeichne ein Balkendiagramm mit den Jahren als Balkengruppen:

.. code:: python3

    from matplotlib import pyplot as plt

    laender.plot.bar()
    plt.savefig('balken.png')
