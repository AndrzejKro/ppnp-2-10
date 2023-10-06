# funkcja - wydzielony kod programu który mozna wykonywac wielokrotnie

# zmienne globale
a = 6
b = 7


# definicja funkcji - ona w tym miejscu się nie wykonuje

def dodaj():  #fukcja bezargumentowa
    print(a + b)

def dodaj2(a, b):  # funkcja z dwoma argumentami które musimy przekazać
    print(a + b)

def odejmij(a=0, b=0, c=0): #funkcja z argumentai domyślnymi
    print(a-b-c)

def odejmij2(liczba1, liczba2):
    print('Wynik odejmowania: ',liczba1 - liczba2)

# wywołanie funkcji (uruchomienie)

dodaj()  # 13

# dodaj2()   #IndentationError: expected an indented block after function definition on line 14

dodaj2(343,24323)

odejmij(10,2)
odejmij(1, 3 ,3) # przekazywanie argumentów w pozycji
odejmij(b=2, c=1)  # przekazywanie argumentów po nazwie
odejmij2(4, 5)
odejmij2(liczba2=100, liczba1=20)

# z funkcji nie zwraca wyniku funkcji
# print(dodaj() + dodaj2(23, 3)) TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
print(dodaj()) #None - funkcja nie zwraca do programu wyniku działania dlatego "None"

