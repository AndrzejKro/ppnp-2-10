# napisz funkcję obliczajacą średnią

def srednia(i=0, *cyfry):  # tworzy dowolnej wielkości worek
    print(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c
        count = len(cyfry)
        avg = suma / count

    except Exception as e:
        print('bład: ', e)
    else:
        print(f"średnia dla uczniów {i} wynosi {avg}")


srednia()
srednia(1, 2, 3, 4, 5, 6, 7)
srednia(2, 3, 4, 5)
srednia('Ala', 1,2,3,4,5,6,2,3)
