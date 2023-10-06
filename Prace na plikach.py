# praca z plikami
# kontekst manager (with)

# encoding='utf-8' - kodowanie pliku i polskich liter

with open('test.log', 'w', encoding='utf-8') as fh:  # filehendler
    fh.write('Powitanie\n dana 1 ść\n   dana 2 óą\n')
    fh.write('Kolejne\n dana 1 ż\n   dana 2 ę\n')
    fh.write('Zakończenie \n dana 1 ź\n   dana 2 ć\n')

# with open('test.log', 'w') as fh:  # kasuje plik i zapisuje nowe dane
#     fh.write('Powitanie\n dana 1\n   dana 2\n')

with open('test.log', 'a', encoding='utf-8') as fh:  # dopisywanie danych do plików
    fh.write('Dodanie danych\n dana 1\n   dana 2\n')

with open('test.log', 'r', encoding='utf-8') as file:
    lines=file.read()

print(lines)
print(type(lines)) # <class 'str'> typ danych odczytanych string

# Powitanie
#  dana 1
#    dana 2
# Kolejne
#  dana 1
#    dana 2
# Zakończenie
#  dana 1
#    dana 2
# Dodanie danych
#  dana 1
#    dana 2