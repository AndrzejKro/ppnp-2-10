lista = []  # definicja pustej listy
print(lista)  # []
print(type(lista))  # <class 'list'>

print(bool(lista))  # False

lista.append("radek")
print(lista)

lista.append("maciek")
lista.append("marek")
lista.append("zenak")
lista.append("jaś")
lista.append("staś")
print(lista)  # ['radek', 'maciek', 'marek', 'zenak', 'jaś', 'staś']
print(lista)  # ['0 (-5)', '1 (-4)', '2 (-3)', '3 (-2)', '4 (-1)']

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[5])

# radek
# maciek
# marek
# zenak
# jaś
# staś

print(len(lista))  # - długość listy 6

print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])
print(lista[-5])
print(lista[-6])

# staś
# jaś
# zenak
# marek
# maciek
# radek

print(lista[0:4])  # ['radek', 'maciek', 'marek', 'zenak']
print(lista[2:])  # ['marek', 'zenak', 'jaś', 'staś'] od 2 do końca wyłącznie z 2
print(lista[:3])  # ['radek', 'maciek', 'marek'] od 0 do 2 do końca łącznie z 2
print(lista[7:9])  # []
print(lista[1:3])  # ['maciek', 'marek'] 1 i 2

# nadpisanie elementu w liście
lista [2] = "MIKOŁAJ"
print(lista)  # ['radek', 'maciek', 'MIKOŁAJ', 'zenak', 'jaś', 'staś']

# rozszerzenie listy, wstawienie elementu w konkretne miejsce
lista.insert(1, "MARCIN")
print(lista)  # ['radek', 'MARCIN', 'maciek', 'MIKOŁAJ', 'zenak', 'jaś', 'staś']

# określenie indeksu elementu z listy
ind = lista.index("MIKOŁAJ")
print(ind) # 3

# usunięcie po indeksie
element = lista.pop(ind)
print(lista)
print(element)
# ['radek', 'MARCIN', 'maciek', 'zenak', 'jaś', 'staś']
# MIKOŁAJ

# usunięcie po wartości
element = lista.remove("MARCIN")
print(lista)
print(element)
# ['radek', 'maciek', 'zenak', 'jaś', 'staś']
# None
print(bool(None)) # False

lista2 = lista # kopiuje referencje - w lista2 mamy zapisany adres
print(lista)
print(lista2)

lista3 = lista.copy() # właściwe kopiowanie listy do drugiej listy3
lista.clear() # czyszczenie pamięci listy
print(lista)
print(lista2)
print(lista3)

print(id(lista))
print(id(lista2))
print(id(lista3))
# 1552777105408 - oznacza że mamy skopowany adres nie wartość
# 1552777105408
# 1552779567808 - inny adres oznacza że mamy zawartość

liczby =  [54, 999, 34, 22, 13.34, 687]
print(liczby)
liczby.sort()
print(liczby)
# [54, 999, 34, 22, 13.34, 687]
# [13.34, 22, 34, 54, 687, 999]

print(lista3)
lista3.sort()
print(lista3)
# ['radek', 'maciek', 'zenak', 'jaś', 'staś']
# ['jaś', 'maciek', 'radek', 'staś', 'zenak']

tekst = "Python"
lista_1 = list(tekst) # rozpakowanie sekwencji
print(lista_1)  # ['P', 'y', 't', 'h', 'o', 'n']

lista2 = [tekst]
print(lista2) # ['Python']

print(lista_1 + lista2) # ['P', 'y', 't', 'h', 'o', 'n', 'Python']
lista3 = lista_1.copy() + lista2.copy()
lista3.sort()
print(lista3)
lista3.reverse()
print(lista3)




