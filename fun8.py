def allparams(a, b, /, c=42, *args, d=256, **kwargs):  # / - oddziela argumenty pozycyjne od pozostałych
    print("a,b", a, b)  # argumenty a i b mogą być tylko po kolejności podane
    print("c,d", c, d)
    print("args", args)
    print("kwargsy", kwargs)


allparams(1, 2)
allparams(1, 2, c=12)
allparams(1, 2, 1, 2, 3, 4, 5, 6, 7, 7, d=12, )
allparams(1, 2, 1, 2, 3, 4, 5, 6, 7, 7, d=12, a = 'ala', b = 'tak', r = 'nie')

# a,b 1 2
# c,d 42 256
# args ()
# kwargsy {}
# a,b 1 2
# c,d 12 256
# args ()
# kwargsy {}
# a,b 1 2
# c,d 1 12
# args (2, 3, 4, 5, 6, 7, 7)
# kwargsy {}
# a,b 1 2
# c,d 1 12
# args (2, 3, 4, 5, 6, 7, 7)
# kwargsy {'a': 'ala', 'b': 'tak', 'r': 'nie'}