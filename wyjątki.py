# wyjątki

# napisać kalkulator
# główna petla programu while

# pobrac rodzaj operacji, w - wyjście z proramu
# pobrac liczby
# wyswietlić wynik

A = 0
B = 0


while True:
    print(f"""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. dzielenie
    5. Wyjście""")

    odp = input('Podaj rodzaj operacji: ')  # pobranie stringu

    if odp > '4': # porównujemy ze stringiem
        break

    try:  # przechwytywanie błędów

        A = float(input('Podaj liczbę A: '))  # pobranie stringu
        B = float(input('Podaj liczbę B: '))  # pobranie stringu

        if odp == '1':
            print('Wynik ', A + B)

        elif odp == '2':
            print('Wynik ', A - B)

        elif odp == '3':
            print('Wynik ', A * B)

        elif odp == '4':
            print('Wynik ', A / B)

        else:
            print('Nie znam takiego działania')

    except ZeroDivisionError: # dzielenia przez zero
        print('Nie dziel przez ZERO')
    except ValueError: # wpisanie litery
        print('Błąd wartości')
    except Exception as e: # inne błędy worek
        print('błąd', e)
    else: # wykonuje sie gdy nie ma błedu
        print('Gdy nie ma błędu')
    finally:
        print('Koniec obliczeń --------------')
