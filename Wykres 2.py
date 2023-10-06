import matplotlib.pyplot as plt

import numpy as np

data  = np.random.normal(0,1,1000) # generowanie danych  przez nunpy
print(type(data)) # <class 'numpy.ndarray'> tablica z Numpy

plt.hist(data, bins=30)
plt.title("Histogram")
plt.ylabel("Częstość")
plt.xlabel("Wartość")
plt.savefig("Wykres.png") # zapisanie pliku png
plt.savefig("Wykres.pdf")

plt.show()

