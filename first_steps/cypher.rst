Cäsar-Chiffer
=============

.. image:: enigma.jpg

Foto von `Christian Lendl auf unsplash.com <https://unsplash.com/@dchris?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash>`__

In diesem Kapitel lernst du:
----------------------------

======= ======================================
Bereich Thema
======= ======================================
🚀      Text ver- und entschlüsseln
⚙       Positionen in Strings indizieren
⚙       über Strings iterieren
💡      die Methode ``str.find`` verwenden
🔀      strings zu verbinden
🔀      einen Index für zwei Strings verwenden
🐞      Indexfehler beheben
======= ======================================


Aufgabe 1: Cäsar-Chiffre
------------------------

Führe folgenden Code aus, der die **Cäsar-Chiffre** ausgibt:

.. code:: python3

   klartext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
   verschluesselt = "DEFGHIJKLMNOPQRSTUVWXYZABC "

   for i in range(26):
       print(klartext[i], " -> ", verschluesselt[i])

Erkläre was der Code tut.


Aufgabe 2: String-Methoden
--------------------------

Erkläre was die Ausdrücke mit dem Text in der Mitte tun.

.. figure:: strings.png

Aufgabe 3: Über Strings iterieren
---------------------------------

Das folgende Programm sollte die Positionen jedes Programms im Alphabet ausgeben.
Vervollständige es durch Einsetzen von ``buchstabe``, ``text``, ``alphabet`` und ``position``:

.. code:: python3

   alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
   text = "MEINE GEHEIMBOTSCHAFT"

   for buchstabe in ___:
       position = ___.find(___)
       print(buchstabe, "ist in Position", ___)

Warum ist das Leerzeichen am Ende von ``alphabet`` wichtig?

Aufgabe 4: Strings verbinden?
-----------------------------

Erkläre folgenden Code:

.. code:: python3

   chiffre = "DEFGHIJKLMNOPQRSTUVWXYZABC "

   s = ""
   s += chiffre[4]
   s += chiffre[1]
   s += chiffre[8]
   s += chiffre[8]
   s += chiffre[11]
   print(s)

Aufgabe 5: Verschlüsseln
------------------------

Schreibe ein Programm, welches:

1. ein Klartext-Alphabet und ein verschlüsseltes Alphabe als Strings mit 26 Zeichen + Leerzeichen definiert
2. eine Nachricht von der Tastatur einliest
3. einen leeren String als Ergebnis definiert
4. über jedes Zeichen der Nachricht iteriert
5. die Position des Zeichens im Klartext-Alphabet findet
6. die selbe Position im verschlüsselten Alphabet nachschlägt
7. alle verschlüsselten Zeichen an das Ergebnis anhängt
8. am Ende das Ergebnis ausgibt

.. hint::

   Du solltest nach jedem dieser Schritte in der Lage sein,
   das Programm auszuführen und zu prüfen was es schon kann.

Aufgabe 6
----------

Erkläre warum dieser Code das gleiche wie in Aufgabe 1 tut:

.. code:: python3

   klartext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   for i in range(26):
       print(klartext[i], " -> ", klartext[(i + 3) % 26])

Kannst du dieses Muster verwenden, um das Verschlüsselungsprogramm zu vereinfachen?

.. hint::

   Falls du nicht sicher bist was überhaupt passiert, gib den Wert von ``i`` in der Schleife aus.
   
Aufgabe 7
----------

Schreibe ein Programm, um den Text wieder zu **entschlüsseln**.

.. hint::

   Kannst du irgendwie dafür sorgen daß der Eingabestring nur aus Grossbuchstaben besteht?
   
Reflexionsfragen
----------------

-  was passiert wenn hinter einer Stringvariablen eckige Klammern stehen?
-  wie kannst du über alle Zeichen eines Strings iterieren?
-  was tut die Methode ``str.find()``?
-  wie kannst du Zeichen zu einem String hinzufügen?
