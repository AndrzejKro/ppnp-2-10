wiek = 47
rok = 2023
tem = 36.6  # float
wiek2 = 37.5

print(wiek)
print(type(wiek))  # <class 'float'>

print(5 * "wiek ")  # wynik: wiek wiek wiek wiek wiek
print(wiek * rok)  # wynik: 95081
print(wiek + rok)  # wynik: 2070
print(wiek - rok)  # wynik: -1976
print(wiek / rok)  # wynik: 0.023232822540781017 - wynikiem jest zawsze float
print(wiek // rok)  # wynik: 0.0 część całkowita z dzielenia
print(wiek % rok)  # wynik: 47 - modulo
print(5 % 2)  # wynik: 1  bo 2 * 2 = 4-5 = 1
print(wiek ** rok)  # potegowanie

print(0.2 + 0.8)  # wynik 1.0 float
print(0.2 + 0.7)  # wynik: 0.8999999999999999 - UWAGA!! błąd zaokraglenia
# w BANKACH stosuje się typ DECIMAL
# błąd zaokrąglenia
# float - przechowuje w pamięci jako mantysta i wykładnik

print((0.3 + 0.6 + 0.7))  # Wynik: 1.5999999999999999

# typ logiczny
# prawda lub fałsz
# True ore False

czy_znasz_pythona = False  # obowiązkowo z dużej litery
print(czy_znasz_pythona)  # Wynik: False
print(int(czy_znasz_pythona))  # wynik : 0

x = 1
print(bool(x))  # bool() - zamienia na typ logiczny, True

x = -10
print(bool(x))  # wszystko co różne od zera daje 0

x = 0
print(bool(x))  # wynik False bo jeśli jast dana to daje zawsze True
x=''
print(bool(x)) # wynik False

#  and znaczy i
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#  or znaczy lub
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# not - negacja
print(not True) # False
print(not False) # True

