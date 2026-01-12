Python installieren
===================

.. figure:: ../images/schlangen.jpg

In diesem Kapitel lernst Du:
----------------------------

======= ==============================================
Bereich Thema
======= ==============================================
🔧       Python installieren
🔧       Visual Studio Code starten
💼       eine Python-Anweisung ausführen  
======= ==============================================

Der erste Schritt in die Welt des Programmierens ist, `Python <https://www.python.org>`__  auf Deinem Computer zu installieren.
Für diesen Kurs müssen zwei Programme installiert werden: **Python** und der Editor **Visual Studio Code**.
Unten findest du eine Anleitung zur Installation dieser Programme unter Windows.
Unter Linux und MacOS ist es etwas einfacher.


Python – Standarddistribution
-----------------------------
Verwende die Standarddistribution von Python:

1. Lade **Python 3.13** von `https://www.python.org/downloads/ <https://www.python.org/downloads/>`__ (oben auf der Seite) herunter
2. Starte das Installationsprogramm. Achte darauf, das Häkchen bei **“Add Python to PATH”** zu aktivieren. 

.. figure:: path.png

Installation testen
+++++++++++++++++++

1. Öffne eine PowerShell oder die Eingabeaufforderung.
2. Gib ein:

::

    python
    
Die Python-Eingabeaufforderung

::

    >>>
    
sollte erscheinen – fertig.


Visual Studio Code (VS Code)
----------------------------
Visual Studio Code ist ein leichtgewichtiger, aber leistungsstarker Editor mit Unterstützung für Debugging, Syntaxhervorhebung und Erweiterungen – einschließlich Python.

1. Lade VS Code von `https://code.visualstudio.com/download <https://code.visualstudio.com/download>`__ herunter
2. Starte das Installationsprogramm und verwende die Standardoptionen.
3. Installiere die Python-Erweiterung. Öffne dazu VS Code.
4. Drücke Ctrl+Shift+X, um den Erweiterungsbereich zu öffnen (oder klicke auf das Symbol mit den vier Quadraten).
5. Suche nach Python und installiere die offizielle Erweiterung von Microsoft.

Wenn Python korrekt erkannt wurde, sollte eine Python-Version (z. B. 3.13.3) unten rechts im Fenster angezeigt werden. Eventuell mußt du auf das Feld rechts unten klicken, um die Python-Version auszuwählen. VS Code sollte das installierte Python selbst finden.

.. figure:: vscode.png
   :caption: Visual Studio Code

Python in VS Code testen
++++++++++++++++++++++++

Zuletzt solltest du ausprobieren ob Python wirklich funktioniert.

1. Erstelle eine neue Datei (mit Strg-n) und speichere sie unter dem Namen ``hello.py``. Achte darauf, dass nach der Endung .py nichts weiter folgt.
2. Füge die Codezeile ``print("hello world")`` ein
3. Klicke auf die Ausführen-Schaltfläche (▶️) oben rechts.

Wenn ``hello world`` im Terminal unten ausgegeben wird, funktioniert alles korrekt. Herzlichen Glückwunsch!
