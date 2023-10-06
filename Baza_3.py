# relacyjna baza danych sql
# sqlite - mała baza danych ksiegowa w jednym pliku



import sqlite3

try: # przechwycenie komunikatów
    sql_connection = sqlite3.connect('sqlite_python.db') # utworzenie ZMIENNEJ Z KOMENDĄ sql
    insert_sql = "INSERT INTO software (id, name, price) VALUES (1, 'Python', '1434351354');"
    select = '''
     SELECT * FROM software;
    '''
    update = '''
    UPDATE software SET price = 200
    WHERE id=1;
    '''
    delete = '''
     DELETE FROM software 
     WHERE id=1;
     '''
    # with open('tables.sql', 'r') as file: # uruchomienie komend SQL z pliku
    #     sql_script = file.read()


    cursor = sql_connection.cursor()
    print('Baza danych została podłaczona')

    # cursor.execute(query) # uruchomienie komendy
    # sql_connection.commit() # zapisanie zmian
    # cursor.executescript(insert_sql) # wykonanie komend z SQL z pliku z wczytaniem danych
    # sql_connection.commit()
    for row in cursor.execute(select): # odczytanie danych z bazy danych i wrzucenie do krotki
        print (row)
    # cursor.execute(update) # (1, 'Python', 200.0)  - zaktualizowanno cenę na 200
    # sql_connection.commit()
    # cursor.execute(delete) # usunięto dane z software
    # sql_connection.commit()

except sqlite3.Erroras as e:
    print("bład podłaczeneni do bazy danych ", e)

finally: #wykonanie jeśli nie został przechwycony żaben błąd
    if sql_connection:
        sql_connection.close()
        print("Baza danych została zamnięta")