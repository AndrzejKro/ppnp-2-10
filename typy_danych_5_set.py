# SET - po polsku zbiór - ma cechę przechowywania niepowtarzajace się dane
# druga cecha - tracimy kolejność przy dodawaniu

lista = [44, 55,66,777, 33,22,11,33,11,22]
zbior = set(lista)
print(zbior) # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior)) # <class 'set'> - typ danych set

zb_stary = set() # pusty zbior danych
print(zb_stary) # set()

zbior.add(999) # add dodawanie danych do zbioru
zbior.add(18) # add dodawanie danych do zbioru
zbior.add(18) # add dodawanie danych do zbioru
print(zbior) # {33, 66, 999, 777, 11, 44, 18, 22, 55}

zbior.remove(55) # usunięcie po elemenice
print(zbior) # {33, 66, 999, 777, 11, 44, 18, 22}

print(zbior.pop()) # usuniecie pierwszego elementu z listy 33
print(len(zbior)) # liczenie  elementów zbioru 7 elementów

zbior.pop()
zbior.pop()
print(zbior) # usunął elementy {777, 11, 44, 18, 22} 66 i 999

lista2 = list(zbior) # rzutowanie zbioru na listę
print(lista2.sort())  # {777, 11, 44, 18, 22} wrzucił posortowane dane z listy

zbior2 = {33, 66, 999, 777, 777, 11, 44, 18, 22, 55, 55} # deklarowanie zbioru
print(zbior2) # {33, 66, 999, 777, 11, 44, 18, 22, 55}
print(type(zbior2))  # <class 'set'>

# porównywanie zbiorów
print(zbior | zbior2) # suma zbiorów {33, 66, 999, 777, 11, 44, 18, 22, 55}
print(zbior & zbior2) # część wspólna zbiorów {777, 11, 44, 18, 22}
print(zbior - zbior2) # róznica zbiorów set()
print(zbior2 - zbior) # róznica zbiorów {33, 66, 55, 999}

print(zbior.difference(zbior2)) # róznica zbiorów set()
print(zbior2.difference(zbior))  # róznica zbiorów {33, 66, 55, 999}
print(zbior) #{777, 11, 44, 18, 22}
print(zbior2) #{33, 66, 999, 777, 11, 44, 18, 22, 55}

# {777, 11, 44, 18, 22} - {33, 66, 999, 777, 11, 44, 18, 22, 55} = set()






