
# ** oznaczają argumenty słownikowe

def connect(**opcje):
    print(opcje)
    print(type(opcje))   # <class 'dict'>
    connect_param = {
        'host':'127.0.0.7',
        'port':'9090'
    }
    connect_param['pwd'] = opcje
    print(connect_param)
    print(connect_param['pwd']['klucz']) # wartosc


# connect() # {} słownik

connect(klucz='wartośc') # {'a1': '22', 'klucz': 'wartośc', 'a': 98}
connect(a1='22',klucz='wartośc') #{'host': '127.0.0.7', 'port': '9090', 'pwd': {'klucz': 'wartośc'}}
connect(a1='22',klucz='wartośc', a=98)  # {'host': '127.0.0.7', 'port': '9090', 'pwd': {'a1': '22', 'klucz': 'wartośc', 'a': 98}}
