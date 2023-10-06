# pętle
# instrukcje sterowania przepływem (if i case oraz pętle)
import random
from itertools import zip_longest

# pętle iteracyjne for


for i in range(10):  # 0...9 wypisuje liczby od 0 do 9
    print(i + 1)

for i in range(10):  # 0...9 wypisuje liczby od 0 do 9
    pass  # nic nie robi

for _ in range(10):  # _ zmienna śmieciowa tzw niema zmienna
    pass
#    print(_)

lista2 = list(range(1, 50))
for i in range(6):
    wyn = random.choice(lista2)
    lista2.remove(wyn)
    print(f"    -", wyn)

for i in range(10):  # 0...9 wypisuje liczby od 0 do 9
    print(i * 2)

for i in range(10):  # 0...9 wypisuje liczby od 0 do 9
    if i % 2 == 0:
        print(i, 'Parzysta')
# 0 Parzysta
# 2 Parzysta
# 4 Parzysta
# 6 Parzysta
# 8 Parzysta


lista3 = [j for j in range(10) if j % 2 != 0]
print(lista3)  # wypisuje liczby nieparzyste [1, 3, 5, 7, 9]

lista4 = []  # robi to samo co dwie linijki powyżej
for j in range(20):
    if j % 2 == 0:
        lista4.append(j)

print(lista4)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

for c in lista4:
    if c == 2:
        c += 1  # c=c+1
print(c)

a = 1
a += 1  # a = a + 1
print(a)
a -= 1  # a = a - 1
print(a)
a *= 3  # a = a * 2
print(a)
a = 5
a %= 3  # reszta z dzielenia
print(a, 'Reszta z dzielenia')
a /= 2  # a = a / 2
print(a)
#
# imiona = ['radek', 'asia', 'zbyszek', 'karolina']
# for p in imiona:
#     print(imiona.index(p), p)
#
# imiona = ['radek', 'asia', 'zbyszek', 'karolina']
# for p in range(len(imiona)):
#     print(p, imiona.index[p])
#
# for p in enumerate(imiona):  # zwracca ponumerowane elementy kolekcji
#     print(p)
#
#     a, b = (0, 'radek')
#     print(a)
#     print(b)
#
#     for p, w in enumerate(imiona):
#         print(p, w, sep=";", end='')
#         print()


ludzie = ['radek', 'asia', 'zbyszek', 'karolina', 'Kasia']
wiek = [24, 23, 23, 45]

# wypisać osobę i wiek

# for p, o in enumerate(ludzie):
#     print(p, o, wiek[p])

# zip() łączy kolekcje

for k in zip(ludzie, wiek):
    print(k)

for o, w in zip(ludzie, wiek):
    print(o, w)

for p in enumerate(zip(ludzie, wiek)):
    print(p)
a, b = (3, ('Karolina', 32))  # ropakowanie krotki połączonej ponumerowanej
print(a, b)
c, d = b  # rozpakowanie krotki ludzie wiek
print(a, c, d)

for a, (c, d) in enumerate(zip(ludzie, wiek), start=1):  # enumerate rozpoczyna  numreowanie od 1 a nie od 0
    print(a, c, d)
# 1 radek 24
# 2 asia 23
# 3 zbyszek 23
# 4 karolina 45   NIE MA Kasi

jezyk = ['python', 'java'] #
zipped = zip_longest(ludzie, wiek, jezyk, fillvalue='Nan') # iterator
print(type(zipped))  # <class 'itertools.zip_longest'>
zipped_list = list(zipped)

for item in zipped_list:
    print(item)

# ('radek', 24, 'python')
# ('asia', 23, 'java')
# ('zbyszek', 23, 'Nan')
# ('karolina', 45, 'Nan')
# ('Kasia', 'Nan', 'Nan')

for o, w, j in zipped_list:
    print(o, w, j)

# radek 24 python
# asia 23 java
# zbyszek 23 Nan
# karolina 45 Nan
# Kasia Nan Nan


