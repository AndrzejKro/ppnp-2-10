import os

for root, dirs, files in os.walk(".."):
    abs_root = os.path.abspath(root)
    # print (abs_root) - wypisanie ścieżek do katalogów

    if dirs: # katalogi
        print("Directories")
        for dir_ in dirs:
            print(dir_)

    if files: # wypisuje listę plików
        print("Files:")
        for filename in files:
            print(filename)

for root, dirs, files in os.walk("../ppnp-2-10"): #wyszukuje pliku
    for file in files:
        if file == 'api_NBP_to_xml.py': # szukany plik
            file_patch = os.path.join(root, file)
            print(file_patch) #../ppnp-2-10\api_NBP_to_xml.py wynik wyszukania pliku