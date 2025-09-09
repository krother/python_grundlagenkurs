
Substitutionschiffre
====================

In der Datei :download:`code.txt` findest du einen deutschsprachigen Text.
Er wurde mit einer Substitutionschiffre verschlüsselt
(jeder Buchstabe wurde mit einem anderen ersetzt).

Lade die Datei
--------------

.. code:: python

    text = open("code.txt").read()
    print(text)

Erstelle eine Ersetzungstabelle
-------------------------------

Zum Entschlüsseln benötigst du ein Dictionary, in dem alle Buchstaben des kodierten Texts als Schlüssel und die Buchstaben im Klartext als Werte vorhanden sind.

.. code:: python

   kodiert  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   klartext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

   chiffre = dict(zip(kodiert, klartext))
   print(chiffre) 

Die Buchstaben im Klartext stimmen natürlich noch nicht, aber wir müssen ja irgendwo anfangen.

Ersetze Buchstaben
------------------

Schreibe eine Schleife, die den Text Buchstabe für Buchstabe ersetzt.
Ignoriere Sonderzeichen (hier Leerzeichen und Zeilenumbrüche).

.. code:: python

   klartext = ""
   for char in text:
       ...

Statistischer Angriff
---------------------

Eine Substitutionschiffre ist über die Buchstabenhäufigkeiten angreifbar.
Mit folgendem Code kannst du sie ermitteln:

.. code:: python

    from collections import Counter

    c = Counter(text)
    print(c)

Vergleiche die Häufigkeiten im Text mit denen eines Referenztextes (z.B. einer Wikipedia-Seite).
Die folgende Zeile wirft alles ausser Buchstaben aus einem String heraus, so dass du sie besser zaehlen kannst:

.. code:: python

   import re
   buchstaben = ''.join(re.findall("[A-Z]", text.upper()))


Knacke den Code
---------------

Probiere unterschiedliche Buchstaben aus.