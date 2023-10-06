# funkcje zwracajace wynik

def dodaj(a, b):
    return a + b  # zwraca wynik do miejsca wywołania funkccji przciwnie jak print


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


# wywołanie funkcji - uruchomienie
print(dodaj(4, 5))
wyn = dodaj(3, 4)
print(wyn)

print(dodaj(3, 4) + dodaj(3, 34))

print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))
print(oblicz_vat(vat=14, cena=7))

zm = oblicz_vat(1000)
if zm == 1230:
    print('działa cena z Vat to 1230 PLN')


