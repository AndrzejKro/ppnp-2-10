import csv

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r', encoding='utf-8') as f:
    #wyszukanie automatyczne dla CSV separatora
    dialect = csv.Sniffer().sniff(f.read(10)) # wyszukuje separator automatycznie w 1024 pierwszych znakach
    print('Wykryty separator= ',dialect.delimiter)
    f.seek(0) # wyzerowanie licznika w plik był odczytywany
    # csvreader = csv.reader(f, delimiter=';') ręczne ustawienie separatora
    csvreader = csv.reader(f, delimiter=dialect.delimiter)

    print(csvreader)  # <_csv.reader object at 0x0000020C03EB7460>
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

print(fields) # ['name', 'branch', 'year', 'cgp']
print(rows) # [['Radek', 'coe', '3', '9.1'], ['Ala', 'cos', '2', '9'], ['Leon', 'cod', '3', '9.9'], ['Bob', 'cot', '4', '9.5'], ['Tod', 'coe', '5', '8.1'], ['Jaś', 'cod', '2', '8.9']]
print(type(rows)) # <class 'list'> lista z listami a w nich zapisane stringi ''
suma = 0
for i in rows:
    print(float(i[-1]))
    dane = float(i[-1]) # wyciągnięcie danych z listy rows i zamiana na dane typu float
    suma += dane

print(f'Średnia wynosi = {suma / len(rows)}') # wypisanie i obliczenienie sredniej



