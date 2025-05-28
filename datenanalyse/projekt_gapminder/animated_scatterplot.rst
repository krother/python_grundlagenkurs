
Animierter Scatterplot
======================

In dieser Übung werden wir den Zusammenhang von Lebenserwartung und Fruchtbarkeit untersuchen.
Dazu werden wir die berühmte Animation von **Hans Rosling** nachstellen (siehe `Hans Rosling - Global population growth, box by box <https://www.youtube.com/watch?v=fTznEIZRkLg>`__.


Schritt 1
---------

Lade die Datei :download:`daten/demographie.csv` in pandas.

.. code:: python3

    import pandas as pd
    import seaborn as sns
    from matplotlib import pyplot as plt

    fert = pd.read_csv('gapminder_total_fertility.csv')

Inspiziere die Daten.

Schritt 2
---------

Erstelle einen Scatterplot, z.B.:

.. code:: python3

   sns.scatterplot(data=d, x="fruchtbarkeit", y="lebenserwartung", 
                   hue="land", legend=False)


Schritt 3
---------

Wähle einen Teildatensatz aus, z.B.:

.. code:: python3

    de = df[df["land"] == "Germany"]

Plotte die Daten erneut.

Schritt 4
---------

Möchtest du die Größe der Kreise nach der Bevölkerung einstellen, sind folgende Schritte nötig:

.. code:: python3

   df = df.dropna()   # leere Zeilen raus
   x = ...            # Skalierungsfaktor
   sns.scatterplot(s=df["bevoelkerung"] * x)

Finde einen sinnvollen Wert für x.

Schritt 5
---------

Du kannst die Darstellung auch etwas präzisieren.
Füge folgende Anweisungen zum Plot-Befehl hinzu:

.. code:: python3

   plt.figure(figsize=(7, 5))
   sns.scatterplot(...)
   plt.xlim(0, 8)
   plt.ylim(30, 80)
   plt.title("mein plot")
   plt.savefig("plot.png", dpi=100)

Schritt 6
---------

Erstelle nun eine Serie von Scatterplots, einen für jeden Jahrgang ab 1960.

Schritt 7
---------

Installiere das Python-Modul `imageio`, indem Du auf der Kommandozeile eingibst:

.. code:: python3

    pip install imageio

Passe das folgende Skript an und führe es aus:

.. code:: python3

    import imageio

    images = []

    for i in range(0, 100):
        filename = f'plot_{}.png'
        images.append(imageio.imread(filename))

    imageio.mimsave('output.gif', images, fps=20)
