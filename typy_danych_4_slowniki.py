# Słowiniki - para danych {klucz:wartość}
# odwzorowanie jsona w pythonie
# {"name":"Radek"}
# klucz nie może się powtarzać

dictionary = {}  # pusty słownik
print(dictionary)  # {}

dictionary['imie'] = 'Radek'
print(dictionary)
dictionary['wiek'] = 39
print(dictionary)  # {'imie': 'Radek', 'wiek': 39}

print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())
# dict_values(['Radek', 39])
# dict_keys(['imie', 'wiek'])
# dict_items([('imie', 'Radek'), ('wiek', 39)])

dictionary.update({'date': '12-21-2023'})  # dodanie kolejnej pary do słownika
print(dictionary)  # {'imie': 'Radek', 'wiek': 39, 'date': '12-21-2023'}

dictionary1 = {'x': 2}
dictionary1.update([('y', 3), ('z', 5)])
print(dictionary1)  # {'x': 2, 'y': 3, 'z': 5}
print(dictionary1['x'])  # 2 - wypisanie elementu ze słownika

# storzenie słownika polsko - angielski
# 3 klucze minimum

dict2 = {'imie': 'name', 'kot': 'cat', 'pies': 'dog'}
print(dict2['imie'])  # name

# wypiszyemy słowa jakie umie przetłumaczyć
print('Mam w słowniku', dict2.keys())
key = input('Podaj słówko do przetłumaczenia')
print(dict2[key.replace(" ", "").lower()])  # usunięcie spacji replace i zmiana na małe

# kalkulator
# pobrac od uzytkownika A i B (input)
# wypisać wynik np dodawanie (print)

print('Kalulator dodawania podaj cyfrę ')
A = input('A =')
B = input('B =')
C=float(A.replace(',','.'))+float(B) # rzutowanie stringa na liczby typu float
print(C)

