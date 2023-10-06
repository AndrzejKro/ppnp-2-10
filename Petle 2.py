diction1 =  {'imie':'radek', 'nazwisko':'kowalski'}


# wypisuje klucze
for k in diction1:
    print(k)
# imie
# nazwisko

for k in diction1.keys():
    print(k)
# imie
# nazwisko

for k in diction1.items(): # wyciąga pary kluczy i wartości - krotki
    print(k)

# ('imie', 'radek')
# ('nazwisko', 'kowalski')

for k in diction1.values(): # wyrzuca tylko wartości
    print(k)
# radek
# kowalski

for k, w in diction1.items(): # rozpakowuje pary z krotki
    print(k,"->", w)

# imie -> radek
# nazwisko -> kowalski


diction2 = {'imie':'radek', 'nazwisko':'kowalski', 'company':'rozne'}
print({value: key for key, value in diction2.items()})
# {'radek': 'imie', 'kowalski': 'nazwisko', 'rozne': 'company'}

# to co wyżej na piechotę
d2={}
for key, value in diction2.items():
    d2[value]=key
print(d2)
# {'radek': 'imie', 'kowalski': 'nazwisko', 'rozne': 'company'}

