# pliki csv
# pliki tekstowe gdzie dane odzielone są separatorem np: , ; " "
# Radek, Maciek, Zenek
import csv

# imoprt csv  # bibliotyka do plików CSV

row = ['Radek', 'coe', 3, '9.1']
fields = ['name', 'branch', 'year', 'cgp']
dist2 = dict(zip(fields, row))  # tworzymy słownik
print(dist2)  # {'name': 'Radek', 'branch': 'coe', 'year': 3, 'cgp': '9.1'}

dict_x = [
    {'name': 'Radek', 'branch': 'coe', 'year': 3, 'cgp': '9.1'},
    {'name': 'Ala', 'branch': 'cos', 'year': 2, 'cgp': '9'},
    {'name': 'Leon', 'branch': 'cod', 'year': 3, 'cgp': '9.9'},
    {'name': 'Bob', 'branch': 'cot', 'year': 4, 'cgp': '9.5'},
    {'name': 'Tod', 'branch': 'coe', 'year': 5, 'cgp': '8.1'},
    {'name': 'Jaś', 'branch': 'cod', 'year': 2, 'cgp': '8.9'},

]

filename = 'records.csv'

with open(filename, 'w', encoding='utf-8', newline='') as csv_f: # newline = '' powoduje że dane nie mają pustego wiersza przerwy
    #csvwriter = csv.writer(csv_f)
    #csvwriter.writerow(row)
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=';')  # delimiter=';' separator zmieniony na ;
    csvwriter.writeheader()
    csvwriter.writerows(dict_x)