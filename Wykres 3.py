import matplotlib.pyplot as plt

import mpld3


labels =['jabłka','banany', 'winogrona', 'pomarańcze']
sizes =[30,25,20,45]
colors = ['red','blue', 'purple', 'yellow']

plt.pie(sizes, labels=labels, colors=colors, shadow=True, #cień
        startangle=90,
        explode=(0.1, 0, 0, 0), # wycięcie pierwszej danej
        autopct='%1.1f%%') # autopct określa jak ma wyglądać opis liczbowy

plt.title('Wykres kołowy')
plt.axis ('equal') # określa wielkość osi
html = mpld3.fig_to_html(plt.gcf()) # konwersja na html

plt.show()

with open('pie.html', 'w') as f:
    f.write(html)

