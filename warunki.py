# WARUNKI
# Instrukcje warunkowe - instrukcja sterowanie przepływem programu

# if
# sterowana warunkiem, jeżeli warunek jest True to wykonuje działania z drugiego bloku

odp = False
if odp:
    print('Brawo - True')  # obowiązkowo wcięcie (4 spacje), zo najmniej jedna komenda we wcięciu

print('działam dalej')  # działanie w przypadku przejścia IF

odp2 = not odp
if odp2:
    print('Brawo - True')  # obowiązkowo wcięcie (4 spacje), zo najmniej jedna komenda we wcięciu
else:  # w przeciwnym przypadku
    print('Musisz się dalej uczyć! - False')
print('działam dalej')  # działanie w przypadku przejścia IF

# podatek = 0.0
# zarobki = int(input('Podaj dochód'))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.6
#
# print(podatek)
# print(f'Podatek wynosi {zarobki * podatek}')

# dodać kolejny podatek (0.2) dla zarobków pomiędzy 10000 a 29999
# kolejność ma znaczenie
# podatek = 0.0
# zarobki = int(input('Podaj dochód'))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000: # kolejne warunki jeżeli nie to...
#     podatek = 0.2
# elif zarobki < 100000: # coś w rodzaju sit sortujących po kolei wielkość piasku
#     podatek = 0.4
# else:
#     podatek = 0.6
#
# print(podatek)
# print(f'Podatek wynosi {zarobki * podatek}')

suma_zam = 250
if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0

print(f"rabat wynosi: {rabacik}")  # f - wpisanie stringu w komunikat

# jednolinijkowa instrukcja IF
rabacik = 25 if suma_zam > 150 else 0
print(f"jedna linijka rabat wynosi: {rabacik}")  # f - wpisanie stringu w komunikat

# symulacja przepływu programu
lista_bledow = []  # pusta lista
alert_system = 'email'
error = 'medium'
error_message = 'Stało się coś strasznego!'

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    lista_bledow.append("email")
    if error == 'medium':
        lista_bledow.append('ostrzeżenie')
    elif error == 'critical':
        lista_bledow.append('krytyczny')
    else:
        lista_bledow.append("inny błąd")
else:
    print("System nieznazny")
# dodać błąd inny, wpisać do listy "inny błąd"
print(lista_bledow)

a = 14
b = 3
print(f'Wynik porównania {a}>{b}, {a>b}')
print(f'Wynik porównania {a}<>>{b}, {a<b}')
print(f'Wynik porównania {a}>={b}, {a>=b}')
print(f'Wynik porównania {a}<={b}, {a<=b}')
print(f'Wynik porównania {a}=={b}, {a==b}') # porównanie
print(f'Wynik porównania {a}!={b}, {a!=b}') # różne

# Wynik porównania 14>3, True
# Wynik porównania 14<>>3, False
# Wynik porównania 14>=3, True
# Wynik porównania 14<=3, False
# Wynik porównania 14==3, False
# Wynik porównania 14!=3, True

#napisać test z historii, geografii, czegokolwiek
# wyświetelić pytanie (print)
# pobrać pytanie (input)
# sprawdzić odpowiedź i wpisać wynik (if else)

# print('czy Polska lezy w Europie ? t/n')
odpowiedz = input('czy Polska lezy w Europie ? t/n/niewiem') # pytanie można podać odrazu w input
if odpowiedz == 't':
    print('dobra odpowiedź!')
elif odpowiedz == 'niewiem':
    print('odpowiedź poszukaj na mapie')
else:
    print('Spróbuj jeszcze raz')




