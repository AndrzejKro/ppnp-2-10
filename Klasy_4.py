class Dom:
    """
    klasa opisująca dom
    """

    def __init__(self, metraz, kolor, liczba_okien):  # __init__ konstruktor
        # uzupełnić konstruktor

        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    # stworzyć metody dczytujące tr  pola mam_kolro

    def mam_kolor(self):
        print(f"Kolor domu to: {self.__kolor}")

    def mam_metraz(self):
        print(f"Mam metraz {self.__metraz}")

    def mam_okna(self):
        print(f"Mam {self.__liczba_okien} okna")

    def zmien_kolor(self):
        wybor = input('Podaj nowy kolor')
        self.__kolor = wybor
        self.mam_kolor()
        self.__farba()

    def zmien_metraz(self):
        wybor = float(input('Podaj nowy metraz'))
        self.__metraz = wybor
        self.mam_metraz()

    def __farba(self):
        print('skończyła się farba')


dom1 = Dom(150, 'biały', 10)
dom1.mam_kolor()
dom1.mam_metraz()
dom1.mam_okna()
dom1.zmien_kolor()
dom1.zmien_metraz()
# Kolor domu to: biały
# Mam metraz 150
# Mam 10 okna
# Podaj nowy kolorafd
# Kolor domu to: afd
# skończyła się farba
# Podaj nowy metraz12434.24545
# Mam metraz 12434.24545