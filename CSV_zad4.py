import csv

lista = []
city =[]

with open('dane.csv', 'r') as file: # otworzenie pliku
    reader = csv.reader(file)
    print(reader)  #adres do odczytach danych

    for i in reader: # zapisanie danych w liście
        lista.append(i)
        city.append(i[-1])


print(lista) # [['SN', ' Name', ' City'], ['1', ' Michael', ' New Jersey'], ['2', ' Jack', ' California']] lista w liście
print(city) # [' City', ' New Jersey', ' California']

lista[1][1] =' Kasia'
print(lista)

with open('dane2.csv', 'w', newline='') as file: # otworzenie pliku
    writer = csv.writer(file)
    writer.writerows(lista)