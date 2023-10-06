# praca na katalogach

import shutil
from pathlib import Path

base_path = Path('ops_example')
base_path2 = Path('ops_example/D')

print(base_path)  # ops_example
print(base_path2)  # ops_example\D

if base_path.exists() and base_path.is_dir():  # sprawdzamy czy taka ścieżka i katalog istnieją jeśli istnieja to usuwamu katalog i scieżkę
    shutil.rmtree(base_path)  # usunięcie

base_path.mkdir()

path_b = base_path / 'A' / 'B'
path_c = base_path / 'A' / 'C'
path_d = base_path / 'A' / 'D'

path_b.mkdir(parents=True)
path_c.mkdir()  # tworzenie katalogu C

for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt',):
    with open(path_b / filename, 'w', encoding='utf-8') as f:
        f.write(f"jakas treść pliku {filename}")

# przeniesienie pliku to innego katalogu
shutil.move(path_b, path_d) # przeniesienie pliku do katalogu D
ex1 = path_d / 'ex1.txt'
ex1.rename(ex1.parent / 'ex1zmienioa.log') #  zmiana nazwy pliku ex1
print(base_path.absolute()) #  C:\Users\CSComarch\PycharmProjects\ppnp-2-10\ops_example
print(base_path2.absolute())  # C:\Users\CSComarch\PycharmProjects\ppnp-2-10\ops_example\D
