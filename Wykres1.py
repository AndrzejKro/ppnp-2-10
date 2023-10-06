import matplotlib.pyplot as plt

#dane do wykresu
# UWAGA!! musi byc ta sama ilość danych
x= [1,2,3,4,5,6,7]
y=[13,14,22,32,43,63,23]


plt.plot(x,y, color='red') # typ wykresu
plt.title("Wykres liniowy") # nazwa wykresa
plt.xlabel('Os X') # nazwa osi x
plt.ylabel('Oś Y')
plt.show() # pokazanie wykresu




