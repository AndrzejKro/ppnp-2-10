class Human:
    """
    Klasa opisujaca człowieka w Pythonie
    """

 #  konstruktor (inicjalizator)


    def __init__(self, imie, wiek, wzrost, plec ='k'):
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

# metody obiektu
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat. ")

    def powitanie(self):
        print(f"Nazywam sie {self.imie}.")

    def moj_wzrost(self):
        print(f"Mam ", self.wzrost, "cm wysokości.")

    def ruszaj(self):
        if self.plec =='k':
            print("Ruszyłam w drogę.")
        else:
            print("Ruszyłem w drogę.")



cz1 = Human('Aga', 29, '178')

cz1.moj_wzrost()

# drugi obiekt z dodatkowymi parametrami

cz2 = Human('Jan', 45, '175', 'm')

cz2.powitanie()
cz2.moj_wzrost()
cz2.ruszaj()
# Mam  178 cm wysokości.
# Nazywam sie Jan.
# Mam  175 cm wysokości.
# Ruszyłem w drogę.