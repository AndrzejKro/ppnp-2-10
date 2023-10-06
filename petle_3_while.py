# while - pętla sterowana warunkiem
# instrukcja sterowania programem
# dopóki warunek True petla sie wwykonuje


licznik = 0
while True:
    licznik += 1  # inkrementuje zwieksza o 1
    print(f'Komunikat!   ', licznik)
    if licznik > 10:
        break  # przerywa działanie petli
print('Dalsza część programu ;)')

while licznik < 11:
    print('Komunikat!!')
    licznik += 1

# sprawdza czy wcisnelismy cyfrę i jesli to nie jest cyfra to kończy działanie
lista = []
lista2 = []
while True:
    wej = input('Podaj liczbę: ')  # pobranie stringu
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))  # zamiana stringa na liczby

print(lista)  # wyświetla stringi ['233', '432', '5425', '44', '4', '5', '7', '2254']

print(lista2)  # Wyświetla liczby [233, 432, 5425, 44, 4, 5, 7, 2254]



