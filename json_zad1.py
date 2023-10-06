# json - {"name":"Radek", "dana":null}
# obiekt typu klucz wartość

import json

peros_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(peros_dict))  # <class 'dict'>

dict_json = json.dumps(peros_dict) # tworzenie pliku json
print(dict_json)  # {"name": "Radek", "age": 40, "czy_pali": null} zamienia '' na "" i None na null
print(type(dict_json)) # <class 'str'>

with open('nasze_dane.json', 'w') as f: # tworzenie pliku json
    json.dump(peros_dict, f, indent=4, sort_keys=True)

with open('nasze_dane.json', 'r') as f: # odczytanie pliku json
    data = json.load(f)

print(data) # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data)) # <class 'dict'>

print(data.keys())
print(data.values())
print(data.items())
# dict_keys(['age', 'czy_pali', 'name'])
# dict_values([40, None, 'Radek'])
# dict_items([('age', 40), ('czy_pali', None), ('name', 'Radek')])

print(data['name']) # Radek po kluczu
