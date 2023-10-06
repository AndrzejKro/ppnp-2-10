# lambda - skrócony zapis funkcji

def odeejmij2(a, b):
    return a - b


odejmij = lambda a, b: a - b

v = odeejmij2(6, 2)
print(v)
print(odejmij(6, 2))

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100

print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))
print(odeejmij2(1000, 7))

wiek = lambda x: 'dzicko' if x < 10 else ('nastolatek' if x < 18 else 'dorosły')

print(wiek(8))
print(wiek(16))
print(wiek(28))

# przemnożenie listy razy 2

lista = [1, 2, 3, 4, 5, 667, 34]
l = []
for i in lista:
    l.append(i * 2)

print(l) # [2, 4, 6, 8, 10, 1334, 68]
print([i*2 for i in lista]) # [2, 4, 6, 8, 10, 1334, 68]

def zmien(x):
    return x*2

#map() - zmiana danych wg. wybranej funkcji do użycia tylko raz
print(f"Zastosowanie map():  {list(map(zmien,lista))}")  #Zastosowanie map():  [2, 4, 6, 8, 10, 1334, 68]
print(f"Zastosowanie map():  {list(map(lambda x: x*10,lista))}")  #Zastosowanie map():  [2, 4, 6, 8, 10, 1334, 68]

# filtorwanie danych
print(f"Zastosowanie map():  {list(filter(lambda x: x>10,lista))}") # Zastosowanie map():  [667, 34]
print(f"Zastosowanie map():  {list(filter(lambda x: x>2 and x<100,lista))}") # Zastosowanie map():  [667, 34]
print(f"Zastosowanie map():  {list(filter(lambda x: 2 < x < 100, lista))}") # Zastosowanie map():  [667, 34]

print(lista)





