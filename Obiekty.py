# waszystko jest w Python obiektem
class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
 #   print (2/0)
    raise MyException("Wystąpił wyjatek ") # wrzucamy wyjatek do obsłużenia
except MyException:
    print("wystapił wyjątek MyException") # komunikat po wyrzuceniu błedu

except Exception as e:
    print('Błąd', e) # pozostałe błędy