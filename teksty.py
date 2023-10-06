tekst = "Witaj Świecie !!"
print(tekst)
print(type(tekst))  # <class 'int'>

tekstW = tekst.upper()  # zamiana tekstu na wielkie litery
print(tekstW)
print(tekst)  # teksty w pythonie są immutable (niezmienne) niemutowalen

print(tekst.lower())  # witaj siwecie

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie !!"))  # Witaj
print(tekst.removesuffix("Świecie !!").upper())  # WITAJ

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9awiecie !!'
print(type(encoded_s))  # <class 'bytes'>

print(tekst[0])  # W
print(tekst.count("i"))  # 3
print(tekst.count("i", 0, 4))  # 1
print(tekst.count("j", 0, 4))  # 0

imie = "Radek"
tekst_format = f"Mam na imie {imie} i lupie Pythona"  # Mam na imie Radek i lupie Pythona
print(tekst_format)
# f - fstring - sformatowane stringi
# w {} umieszczamy nazwy zmiennych, tórych zawartość chcemy wyświetlić

tekst_format = f"\tMam na imie {imie}\n i lupie Pythona\b"  #
print(tekst_format)

# Mam na imie Radek
#  i lupie Python
#  \t tabulator
#  \s nowa linia
#  \b backspace


starszy = "Witaj %s"
#  %s - oznacza w to miejsce wstaw string
print(starszy % imie)  # Witaj Radek

print("""
    tekst 
wielolinijkowy""")
#     tekst
# wielolinijkowy - uruchamia się """ trzema lub ''' trzema tak samo się kończy


print("Witaj {}".format(imie))  # Witaj Radek
