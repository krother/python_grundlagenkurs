Babynamen
=========

In diesem Kapitel lernst du:
----------------------------

======= =======================================================================
Bereich Thema
======= =======================================================================
🚀       Geburtenstatistiken analysieren
💡       Dateien mit der Funktion ``open`` lesen und schreiben
💡       mit dem Modul ``os`` durch ein Verzeichnis iterieren
🔀       Komma-separierte Dateien (CSV) einlesen
🐞       Fehler vom Typ ``FileNotFoundError`` beheben
======= =======================================================================

Der Datensatz der US-Babynamen
------------------------------

.. figure:: ../images/baby.png
   :alt: Babynamen

Für dieses Kapitel musst du einen Datensatz mit Babynamen herunterladen.
Die Behörden der Vereinigten Staaten haben die Vornamen aller seit 1880 geborenen US-Bürger:innen aufgezeichnet.
Der Datensatz ist öffentlich zugänglich unter:
`www.ssa.gov/oact/babynames/limits.html <http://www.ssa.gov/oact/babynames/limits.html>`__

Lade das kleinere Archiv mit Babynamen herunter (nicht nach Bundesstaaten gruppiert).

.. note::

   Zum Schutz der Privatsphäre werden nur Namen aufgeführt,
   die mindestens 5-mal vergeben wurden.

Aufgabe 1: Eine Datei lesen
---------------------------

Entpacke das heruntergeladene Archiv und platziere den Ordner neben deinem Python-Programm.
Lies eine der Dateien, indem du ``zeile``, ``zeile``, ``open`` und ``print`` in die Lücken einfügst.

.. code:: python3

   for ___ in ___(r"names/yob2022.txt"):
       if "Maria" in ___:
           ___(zeile)

.. hint::

   Eventuell musst den vollständigen Pfad zur Datei angeben statt ` `names/`.
   Unter Windows ist das Präfix `r` wichtig, damit Python Backslashes korrekt interpretiert.

Aufgabe 2: Unterschiedliche Namen
---------------------------------

Wie viele verschiedene *Mädchennamen* gab es im Jahr 2022?

**Sortiere** die folgenden Codezeilen und **rücke sie korrekt ein**:

.. code:: python3

   namen = 0
   if "B" in line:
   print(namen)
   if ",F," in line:
   for line in open(r"names/yob2022.txt"):
   namen += 1

Aufgabe 3: Jungennamen
----------------------

Erweitere das Programm aus der vorherigen Aufgabe so, dass Jungen- und Mädchennamen getrennt gezählt werden.

Aufgabe 4: Häufige Namen
------------------------

Das folgende Programm sammelt Namen in einer Liste, die mindestens 10000 Mal vorkommen.
Leider enthält das Programm **vier Fehler**. Finde und korrigiere sie.

.. code:: python3

   top = []
   
   for line in open(r"names/yob2022.txt"):
       columns = line.strip().split(",")
       name = colums[1]
       if int(columns[3]) >= 10000
           top.append(name)
   
   print(top)

Aufgabe 5: Anzahl Babys
-----------------------

Schreibe ein Programm, das die Gesamtzahl der Babys im Jahr 2023 berechnet und auf dem Bildschirm ausgibt.
Vergleiche diese Zahl mit dem Jahr 1923.

Aufgabe 6: Eine Datei schreiben
-------------------------------

Führe das folgende Programm aus. Erkläre, was passiert.

.. code:: python3

   namen = ["Ada", "Bob", "Charlie", "Dorothy"]
   
   with open(r"names.txt", "w") as f:
       for name in names:
       f.write(name + "\n")

.. hint::

   Was passiert, wenn du das `\n` im Programm entfernst?

Aufgabe 7: f-Strings
--------------------

Probiere die folgenden Befehle in einer Python-Konsole aus:

.. code:: python3

   name = "Ada"
   number = 42
   pi = 3.14159
   
   print(f"{name}")
   print(f"{name:>10}")
   print(f"{number:5d}")
   print(f"{number:05d}")
   print(f"{pi:4.1f}")
   print(f"{pi:6.3f}")
   print(f"name: {name}    number: {number}    pi: {pi:6.3f}")

Aufgabe 8: Verzeichnisse:
-------------------------

Um größere Datenmengen zu verarbeiten, musst du mit mehr als einer Datei arbeiten.
Manchmal kennst du die Namen der Dateien nicht im Voraus.
Das Modul ``os`` ist sehr nützlich, wenn du mit vielen Dateien und Verzeichnissen arbeiten möchtest. Insbesondere die Funktion ``os.listdir()`` ist wichtig.

Erkläre den folgenden Code:

.. code:: python3

   import os
   
   for dirname in os.listdir(r"names/"):
       print(dirname)


Reflexionsfragen
----------------

* Woran erkennst du, dass ein Dateipfad in einem Programm falsch ist?
* Was musst du überprüfen, wenn ein Dateipfad in einem Programm nicht funktioniert?
* Wie kann man alle Dateinamen in einem Ordner ausgeben?
