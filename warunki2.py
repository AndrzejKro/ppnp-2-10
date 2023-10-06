

lista = []
lang = input('Podaj język który znasz: ')

match lang.lower().replace(' ', ''):
    case "python":
        lista.append(lang)
    case "c++":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case _: # wartość domyślna (odpowiednik else)
        print("nie znanam języka")

        print(lista)


        # trzeba dokończyć