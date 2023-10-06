import sys

user = "Tomek"  # string
wiek = 39  # int
wersja = 3.2980983  # float - liczby zmiennoprzecinkowe
liczba = 123344556787878  # int
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#               sizeof_digit=4,
#               default_max_str_digits=4300,
#               str_digits_check_threshold=640)

print(sys.float_info)
#  sys.float_info(max=1.7976931348623157e+308,
#               max_exp=1024,
#               max_10_exp=308,
#               min=2.2250738585072014e-308,
#               min_exp=-1021,
#               min_10_exp=-307,
#               dig=15,
#               mant_dig=53,
#               epsilon=2.220446049250313e-16,
#               radix=2,
#               rounds=1)


print("Witaj %s masz teraz %d lat" % (user, wiek))  # Witaj Tomek masz teraz 39 lat
# print("Witaj %s masz teraz %d lat"% (wiek, user)) - weryfikuje typ danych dla %d w tym przypadku
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\ppnp-2-10\formaty.py", line 28, in <module>
#     print("Witaj %s masz teraz %d lat"% (wiek, user))
#           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~
# TypeError: %d format: a real number is required, not str
# %s - string
# %d - digit - liczby
# przy konwencji z % python weryfikuje typ danych

print("Witaj %(user)s masz teraz %(age)d lat" % {"user": user, "age": wiek})
# Witaj Tomek masz teraz 39 lat

print("Witaj {} masz teraz {} lat.".format(user, wiek))  # typ przejściowy
print(f"Witaj {user} masz teraz {wiek} lat!")  # najnowszy sposób
# f - fstring - tekst sformatowany  {} dla zmiennych

print("Używamy wersji Pytchona %i" % 3)  # Używamy wersji Pytchona 3
print("Używamy wersji Pytchona %f" % 3.11)  # Używamy wersji Pytchona 3.110000
print("Używamy wersji Pytchona %.1f" % 3.11)  # Używamy wersji Pytchona 3.1
print("Używamy wersji Pytchona %.2f" % 3.11)  # Używamy wersji Pytchona 3.11
print("Używamy wersji Pytchona %.0f" % 3.11)  # Używamy wersji Pytchona 3
print("Używamy wersji Pytchona %.f" % 3.9)  # Używamy wersji Pytchona 4 - zaokrągla do wyświetlania

x = 3.14
print("Zero miejsc po przecinku %.f" % x)
print("orginalny x=", x)
# Zero miejsc po przecinku 3
# orginalny x= 3.14

print(
    f"używamy f do wyświetlania znaków np. wersja Pythona {wersja}")  # używamy f do wyświetlania znaków np. wersja Pythona 3.2980983
print(
    f"używamy f do wyświetlania znaków np. wersja Pythona {wersja:.1f}")  # używamy f do wyświetlania znaków np. wersja Pythona 3.3
print(
    f"używamy f do wyświetlania znaków np. wersja Pythona {wersja:.0f}")  # używamy f do wyświetlania znaków np. wersja Pythona 3

print(f"{user:>10}")  # Tomek - uzupełnia spacjami l zewiej strony do 10 znaków
print(f"{user:>20}")  # Tomek - uzupełnia spacjami l zewiej strony do 20 znaków
print(f"{user:<30}")  # Tomek                - uzupełnia spacjami z prawej  strony do 30 znaków
print(f"{user:^30}")  # Tomek           - uzupełnia spacjami z prawej i lewej strony do 30 znaków

print(liczba)  # 123344556787878
print("Nasza duża liczba {:,}".format(liczba))  # Nasza duża liczba 123,344,556,787,878

print(f"Nasza duża liczba: {liczba:,}".replace(",", " "))  # Nasza duża liczba: 123 344 556 787 878
print(f"Nasza duża liczba: {liczba:,}")  # Nasza duża liczba: 123,344,556,787,878


