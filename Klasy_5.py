# Klas aabstrakcyjna z której nie mozna zrobić obiektu doadanie (ABC)
from abc import ABC, abstractmethod  # biblioteka do tworzenia klas abstrakcyjnej



class Ptak (ABC):
    """
    Klasa opisujaca ptaka w pythonie - klasa abstrakcyjna
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print('Tu ', self.gatunek, ' lecę z szybkością', self.szybkosc)

    @abstractmethod #dekorator  - wyklucza klasę z użycia
    def wydaj_odglos(self):
        pass


class Kura(Ptak):  # dziedziczenie po Ptaku
    """
    Kura
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # inicjacja prędkości 0
        self.gatunek = gatunek

    def latam(self):
        print(f'Tu ', self.gatunek, "ja nia latam")

    def wydaj_odglos(self):
        print('ko ok ok ko ko ko')


class Orzel(Ptak):
    """
    Orzeł po ptaku
    """

    def wydaj_odglos(self):
        print(f'kiiiijjjjjjaaaa')

# Nie możemy użyć klasy PTAK bo jest abstrakcyjną i dodaną ma bibliotekę ABC oraz dekorator @abstractmethod
# pt1 = Ptak('orzeł', 20)
# pt1.latam()  # Tu  orzeł  lecę z szybkością 20
#
# pt2 = Ptak('kura', 0)
# pt2.latam()  # Tu  kura  lecę z szybkością 0
# pt2.wydaj_odglos()

pt3 = Kura("Kura")
pt3.latam()  # Tu  Kura  lecę z szybkością 0

pt4 = Orzel('Orzeł przedni', 34)
pt4.latam()
pt4.wydaj_odglos()

pt5 = Orzel('Orzeł stepowy', 36)
pt5.latam()
pt5.wydaj_odglos()


