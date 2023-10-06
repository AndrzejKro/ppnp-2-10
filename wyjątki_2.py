# kalkulator na match case

a = 0
b = 0

while True:
    print(f"""
    +. Dodawanie
    -. Odejmowanie
    *. Mnożenie
    /. dzielenie
    5. Wyjście""")

    odp = input('Podaj rodzaj operacji: ')  # pobranie stringu

    try:  # przechwytywanie błędów

        a = float(input('Podaj liczbę A: '))  # pobranie stringu
        b = float(input('Podaj liczbę B: '))  # pobranie stringu

        match odp:
            case "5":
                break

            case '+':
                print('Wynik ', a + b)

            case '-':
                print('Wynik odejmowania', a - b)

            case '*':
                print('Wynik mnożenia', a * b)

            case '/':
                print('Wynik dzielenia', a / b)

            case _:
                print('Nie znam takiego działania')

    except ZeroDivisionError:  # dzielenia przez zero
        print('Nie dziel przez ZERO')
    except ValueError:  # wpisanie litery
        print('Błąd wartości')
    except Exception as e:  # inne błędy worek
        print('błąd', e)
    else:  # wykonuje sie gdy nie ma błedu
        print('Gdy nie ma błędu')
    finally:
        print('Koniec obliczeń --------------')
