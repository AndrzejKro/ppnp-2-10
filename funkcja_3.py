a = 12231
b = 10

def dodaj():
    a = 6 # zmienne lokalne nie zmienią wartości funkcji globalnie
    b = 7 # zmienne lokalne nie zmienią wartości funkcji globalnie
    print(a + b)

def dodaj2():

    print(a + b)

def dodaj3():
    global a
    a = 6 # zmienne lokalne została zmieniona na zmienną globalnę NIEBEZPIECZNE!
    b = 7
    print(a + b)



print("Zmienna globalna", a)
dodaj()
print("Zmienna globalna", a)
dodaj2()
print("Zmienna globalna", a)
dodaj3()
print("Zmienna globalna", a)
dodaj2()