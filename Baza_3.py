# relacyjna baza danych sql
# sqlite - mała baza danych ksiegowa w jednym pliku



import sqlite3

try: # przechwycenie komunikatów
    sql_connection = sqlite3.connect('sqlite_python.db') # utworzenie ZMIENNEJ Z KOMENDĄ sql
    insert_sql = "INSERT INTO software (id, name, price) VALUES (1, 'Python', '1434351354');"
    query = '''
    CREATE TABLE developers (
    id INTIGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_data DATATIME,
    salary REAL NOT NULL);
    '''
    with open('tables.sql', 'r') as file: # uruchomienie komend SQL z pliku
        sql_script = file.read()


    cursor = sql_connection.cursor()
    print('Baza danych została podłaczona')

    # cursor.execute(query) # uruchomienie komendy
    # sql_connection.commit() # zapisanie zmian
    cursor.executescript(insert_sql) # wykonanie komend z SQL z pliku
    sql_connection.commit()

except sqlite3.Erroras as e:
    print("bład podłaczeneni do bazy danych ", e)

finally: #wykonanie jeśli nie został przechwycony żaben błąd
    if sql_connection:
        sql_connection.close()
        print("Baza danych została zamnięta")