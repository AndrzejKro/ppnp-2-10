import pandas as pd # as pd oznacza mozliwość skrócenia zapisu zamiast Pandas piszemy pd
# pip install pandas

data = pd.read_csv('records.csv', delimiter=";")
print(data)
#     name branch  year    cgp
# 0  Radek    coe     3   9.10
# 1    Ala    cos     2   9.00
# 2   Leon    cod     3   9.90
# 3    Bob    cot     4   9.50
# 4    Tod    coe     5  12.56
# 5    Jaś    cod     2   8.90

print(data.columns)
print(data.values)
# Index(['name', 'branch', 'year', 'cgp'], dtype='object')
# [['Radek' 'coe' 3 9.1]
#  ['Ala' 'cos' 2 9.0]
#  ['Leon' 'cod' 3 9.9]
#  ['Bob' 'cot' 4 9.5]
#  ['Tod' 'coe' 5 12.56]
#  ['Jaś' 'cod' 2 8.9]]

print(type(data.values)) # inny typ danych <class 'numpy.ndarray'> nunpy
print(data.values[0]) # wyrzuca jedną linie (pierwszą) danych ['Radek' 'coe' 3 9.1]
print(data.items)
# <bound method DataFrame.items of     name branch  year    cgp
# 0  Radek    coe     3   9.10
# 1    Ala    cos     2   9.00
# 2   Leon    cod     3   9.90
# 3    Bob    cot     4   9.50
# 4    Tod    coe     5  12.56
# 5    Jaś    cod     2   8.90>
