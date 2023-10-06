# Rest API - GET, POST, PUT, DELETE [HEAD]
# odpowiednik w bazie danych SELECT, INSERT, UPDATA, DELETE
# CURD - create, read update, delete

import requests as re

waluta = input('Podaj jaki kurs waluty potrzebujesz usd/eur: ')

if waluta == 'usd':
    url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'
else:
    url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'

response = re.get(url) # pobranie tabeli
print(response) # <Response [200]>


table = response.json() # zapisanie tabeli
print(table) # {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD', 'rates': [{'no': '193/A/NBP/2023', 'effectiveDate': '2023-10-05', 'mid': 4.3768}]}

# wypisać wartości ze słownika
print(table['currency']) #dolar amerykański
print(table['rates'][0]['mid']) # 4.3768 - wartość waluty
print(table['rates'][0]['effectiveDate']) # 2023-10-05 - data notowania

