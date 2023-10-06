# KLASA - szblon do budowania obiektów- formularz do wypelnienia, wypełiony formulrz to Obiekt
# cechy - pola (zmienne)
# działania - funkcje
# obiekt - budowany na podstawie klasy (instancja klasy)

# definicja KLASY
# PEP8 - wskazuje że nazwa z dużej litery
class Human:
    """
    Klasa opisujaca człowieka w Pythonie
    """
    imie = ''
    wiek = None
    plec = 'k'

    def powitanie(self):
        print(self)
        print(f"Nazywam sie {self.imie}.")

    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat. ")

    def przedstawienie(self):
        print(f"Nazywam sie {self.imie}")
        print(f"Mam {self.wiek} lat. ")



print(Human.__doc__)  # wypisanie dokumntcji Klasy Human

print(print.__doc__)  # wypisanie dokumentacji print

cz1 = Human()
print(cz1)  # <__main__.Human object at 0x00000205713A1710> z adresem w pamięci, gdzie jest Obiekt

print(cz1.plec)
cz1.imie = 'Kasia'
cz1.wiek = 29

# sworzyć inny obiekt innej płci

cz2 = Human()
cz2.plec = 'm'
cz2.imie = 'Tomek'
cz2.wiek = 87

print(cz2.wiek, cz2.plec, cz2.imie)  # 87 m Tomek

cz1.powitanie()
# <__main__.Human object at 0x00000129FAF01D10>
# Nazywam sie Kasia
cz2.powitanie()
# <__main__.Human object at 0x00000129FAF01D50>
# Nazywam sie Tomek

cz2.wypisz_wiek() # Mam 87 lat.
cz1.przedstawienie() # Nazywam sie Kasia Mam 29 lat.


