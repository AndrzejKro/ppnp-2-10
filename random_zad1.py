import random

# importowanie bibliotaki random i generowania liczb pseudo losowych

print(random.randint(1, 100))  # int 1...100

print(random.random())  # losuje od 0 do 0.99999
print(random.random() * 6)  # losuje od 0 do 5.99999
# print(random.random(6))  # losuje int od 0 do 5 - bład!!
# print(random.random(1, 6))  # losuje int od 1 do 5

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))
print(" ")
lista2 = list(range(1, 50))  # generuje liczby w zakresie 1...49
# print(lista2)
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))

wyn = random.choice(lista2) # losuje liczbę
lista2.remove(wyn) # usuwa z listy wylosowaną liczbę
print(wyn) # wyświetla liczbę wylosowaną
wyn = random.choice(lista2) # losuje liczbę
lista2.remove(wyn) # usuwa z listy wylosowaną liczbę
print(wyn) # wyświetla liczbę wylosowaną
wyn = random.choice(lista2) # losuje liczbę
lista2.remove(wyn) # usuwa z listy wylosowaną liczbę
print(wyn) # wyświetla liczbę wylosowaną
wyn = random.choice(lista2) # losuje liczbę
lista2.remove(wyn) # usuwa z listy wylosowaną liczbę
print(wyn) # wyświetla liczbę wylosowaną

print(random.choices(lista2, k=6)) # losuje powtarzalne liczby

print(random.sample(lista2, 6)) # losuje niepowtarzalne liczby

