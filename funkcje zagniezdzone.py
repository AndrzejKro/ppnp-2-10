# funkcje zagnniezdzone

def fun1():
    print('to jest fun1')

    def fun2():
        print('to jest fun2')
    return fun2 # zwracamy adres fun 2

x=fun1() # zapisanie adresu do fun2
x() # uruchomienie fun2 poprzez adres zapisany w zmiennej x inaczej nie ma do fun2 odwołania

fun1()


