class Car:
    """
    Klasa samochód

    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0 #__pole prywatne HERMETYZACJA

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10


car1 = Car('Fiat', 2023)
car1.gaz()  # samochód zwieksza prędkość o 10
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
#  AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
#  print(car1.__predkosc) # 50 - odczyt prędkości samochodu
#  nie odcztamy bo zostało oznaczone jako prywatne

car1.licznik()  # Prędkość wynosi 50 km/h
car1.hamuj()
car1.hamuj()  # samochód zmniejsza prędkość o 10
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()  # Prędkość wynosi 0 km/h
car1.__predkosc = 100  # możliwość zmiany z programu zostało ograniczone jako pole prywatne poprzez dodanie "__"

car1.licznik()  # Prędkość wynosi 100 km/h po zmianie "__"HERMETYZACJE wtedy Prędkość wynosi 0 km/h
