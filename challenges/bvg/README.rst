
Fahrpläne
=========

**🎯 Lade aktuelle Fahrzeiten vom BVG-Server und gib sie aus.**

Die BVG Transport API
---------------------

Die **Berliner Verkehrsbetriebe (BVG)** stellen eine öffentliche Schnittstelle zur Verfügung, auf der sich Stationen und Abfahrtszeiten ermitteln lassen.
Die Daten sind über eine **REST API** abrufbar. Diese ist auf `https://v6.bvg.transport.rest/ <https://v6.bvg.transport.rest/>`__ dokumentiert.

In dieser Aufgabe schreibst du ein Python Programm, das aktuelle Daten von dort abruft.
Dazu verwenden wir die Bibliothek ``httpx``.
Installiere diese aus dem Terminal mit:

::

    pip install httpx


Stationen ermitteln
-------------------

Das folgende Programm verbindet sich mit der BVG API und sucht Stationen nach deren Namen.
Es gibt die IDs der ähnlichsten Treffer aus.

.. literalinclude:: bvg_stationen.py

Finde die IDs einer Station, die Dich interessiert.
Ermittle sie aus der Ausgabe (dem Dictionary) und gib sie aus.

Abfahrten ermitteln:
--------------------

Um mit Hilfe einer Stations-ID die Abfahrten zu ermitteln benötigst du eine andere Web-Adresse.
Verwende dazu:

::

    url = "https://v6.bvg.transport.rest/stops/xxxxx/departures"

Setze für ``xxxxx`` die gefundene ID ein.
Als Parameter brauchst du nur die Anzahl der gewünschten Abfahrten anzugeben, z.B.:

.. code:: python3

   params = {
       "results": 5,
   }

Verwende das Feld ``departures`` aus der JSON-Ausgabe.
Dieses enthält immer noch recht viele (größtenteils nutzlose) Informationen.
Grenze diese auf wenige Felder ein und gib sie aus.

Datum formatieren
-----------------

In der Antwort befinden sich unter anderem **Zeitstempel**.
Diese werden als Strings zurück gegeben. 
Mit dem Standardmodul ``datetime`` kannst du die Zeitstempel parsen und bequemer auf einzelne Felder zugreifen.
Verwende folgendes Beispiel:

.. code:: python3

   from datetime import datetime
   
   s = '2025-05-24T19:24:00+02:00'
   d = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S+%f:00")
   print(d.hour)
   print(d.minute)

Erzeuge eine übersichtliche Ausgabe der aktuellen Abfahrtszeiten.

Karte zeichnen
--------------

Die gefundenen Stationen enthalten auch Koordinaten mit Längen- und Breitengrad.
Stelle diese auf einer Karte grafisch dar. Verwende dazu die Bibliothek ``folium``:

::

    pip install folium

Hier ist ein Beispiel 

.. literalinclude:: karte.py

Zeichne einige Bahnhöfe auf der Karte ein.

U-Bahn Linie 7
--------------

In der Textdatei :download:`u7.txt` findest du eine Liste aller Bahnhöfe der U7.

- Lade die Namen aus der Textdatei
- Ermittle die Koordinaten aller Bahnhöfe
- Speichere die Koordinaten in einer Textdatei
- zeichne die Koordinaten in der Karte ein

.. warning::

    Die API der BVG hat eine Begrenzung auf 100 API-Zugriffe pro Minute.
    Um den Server nicht zu sehr zu beanspruchen, solltest du:

    - deinen Code mit einer geringen Anzahl Einträge testen (z.B. 3)
    - eine Verzögerung einbauen (``time.sleep(10)``)

    **Dies ist eine Art von Höflichkeit.**
