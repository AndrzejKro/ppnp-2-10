# krotka (tupla) - lista której sie nie zmienia
# zmienna niezmienna jeśli jednoelementowa

tupla = "radek"
print(len(tupla))  # liczba elementów
print(type(tupla))  #<class 'str'>

tupla1 ="przecinek", # musi mieć przecinek by mieć typ Tuple
print(type(tupla1)) # <class 'tuple'>

temp = 36.6
print(type(temp)) #<class 'float'>
print(temp) # 36.6

temp = 37, 7
print(type(temp)) # <class 'tuple'>
print(temp)  # (37, 7)

tupla3 = 43, 55, 22.34, 11, 200
print(type(tupla3))

print(tupla3.index(55))
print(tupla3.count(55))
# <class 'tuple'>
# 1
# 1

a, b = 1, 2
print(a)
print(b)
print(type((1,2)))
# 1
# 2
# <class 'tuple'>

# rozpakowanie tupli
a, *b = 1, 2, 3 # * - oznacza zmienną który jest workiem na pozostałe elementy
print(a)
print(b)
# 1
# [2, 3]

tupla2 = "Tomek", "Radek", "Zenek", "Jaś"
print(tupla2) #('Tomek', 'Radek', 'Zenek', 'Jaś')
imie1, *imie2, imie3 = tupla2
print(imie1)
print(imie2)
print(imie3)
# Tomek
# ['Radek', 'Zenek']
# Jaś

lista =list(tupla3) # rzutowanie tupli na listę kolekcję danych
print(lista) #[43, 55, 22.34, 11, 200]
print(type(lista))  # <class 'list'> zmieniliśmy tuplę na listę
lista.sort() # sotowanie danych z listy
print(lista) # [11, 22.34, 43, 55, 200]







