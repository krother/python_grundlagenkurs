
# Arabische Zahlen

**🎯 Schreibe eine Funktion `arabic2roman()`, die eine arabische in eine römische Zahl umwandelt.**

## Tests

Der folgende Code hilft beim Prüfen der Ergebnisse:

    def test_arabic(self):
        assert arabic2roman(1) == "I"
        assert arabic2roman(11) == "XI"
        assert arabic2roman(9) == "IX"
        assert arabic2roman(151) == "CLI"
        assert arabic2roman(93) == "XCIII"
        assert arabic2roman(294) == "CCXCIV"
        assert arabic2roman(1900) == "MCM"
        assert arabic2roman(1001) == "MI"

## Hinweise

* Du mußt nur Zahlen von 1-5000 berücksichtigen
* Welche Datenstruktur eignet sich zum Nachschlagen der Zahlenwerte der römischen Ziffern?

## Zusatzaufgabe

* schreibe eine Funktion, die römische Zahlen in arabische umwandelt
* verwende die Umkehrfunktion zum Testen
