print()  # wypisz wydrukuj
print("Nazywam się Radek")  # wypisz wydrukuj
print('Nazywam się Radek')  # wypisz wydrukuj
print("wpiszę cytat \" Radek\"")  # wypisz wydrukuj
print('wpiszę cytat " Radek"')  # wypisz wydrukuj
# komentarz
# ctrl / - komentuje zaznaczony obszar
print(type(" Radek"))  # <class'str'> string
print(type(39))
print(5 * " 14")  # 14 14 14 14 14 -przykład kontanacji tekstów
print(5 * 14)  # 70
print("39" + "12")  # 3912 - kontanacja tekstów

# zmienna
# pudełko na dane
imie = "Andrzej"
print(imie)  # wpisuje zawartość zmiennej a nie słowo imie
print(type(imie))  # <class 'int'>

imie = 48
print(imie)  # wpisuje zawartość zmiennej a nie słowo imie
print(type(imie))  # <class 'int'>

wiek = 48
print(wiek)  # wpisuje zawartość zmiennej a nie słowo imie
print(type(wiek))

imie = 48
print(imie + wiek)  # wpisuje zawartość zmiennej a nie słowo imie

# print(5 + "4")  # przykład błedu
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\ppnp-2-10\pierwszy.py", line 31, in <module>
#     print(5 + "4")  # przykład błedu
#           ~~^~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

