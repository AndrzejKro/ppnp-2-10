# relacyjna baza danych sql
# sqlite - mała baza danych ksiegowa w jednym pliku



import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print('Baza danych została podłaczona')
except sqlite3.Erroras as e:
    print("bład podłaczeneni do bazy danych ")

finally: #wykonanie jeśli nie został przechwycony żaben błąd
    if sql_connection:
        sql_connection.close()
        print("Baza danych została zamnięta")



