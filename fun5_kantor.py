#funkcja kantor
#usd, eur


def kantor(waluta):
    print('uruchomienie kantoru')


    def usd():
        print('Wymieniam dolary')
        kwota_usd=float(input("ile dolarów wymieniasz: "))
        print(f"Wymieniam dolary: usd={kwota_usd} na pln ={kwota_usd*4.3} ")

    def eur():
        print('Wymieniam euro')
        kwota_eur=float(input("ile euro wymieniasz: "))
        print(f"Wymieniam euro: eur={kwota_eur} na pln ={kwota_eur*4.6} ")

    if waluta =='eur':
        return eur
    else:
        return usd

waluta = input("podaj co wymieniasz eur/usd: ")
wymieniam=kantor(waluta)
wymieniam()

# przerobić tak by funkcje wewnętrzne przyjmowały kwotę do wymiany