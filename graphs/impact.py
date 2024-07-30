import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

# Impacto de las referencias

# valores
x = [1, 2, 3, 4, 5, 6 ,7 ,8, 9]
y = [3, 39, 37, 23, 386, 201, 121, 130, 135]

tick_label = ['Data Never Sleeps (1)', 'Economía del conocimiento (2)', 'Test-Driven Development (7)', 'Innovaciones sociales para territorios “inteligentes”(7)', 
              'The Age of Intelligent Cities (10)', 'Disputas por los territorios y los recursos naturales(14)', 'Los espacios invisibles(19)','La cultura científica y tecnológica (19)','Territorios rurales (21)']


# dibujado
fig, ax = plt.subplots()
width = 0.75
ind = np.arange(len(y))
ax.barh(ind, y, width, tick_label=tick_label, color = "blue")

for i, v in enumerate(y):
    ax.text(v + 3, i + .25, str(v), 
            color = 'green', fontweight = 'bold')

# grafica
plt.title('DIAGRAMA #1: IMPACTO DE LAS REFERENCIAS', color = "blue", fontweight = 'bold')
plt.xlabel('Citaciones externas', color="green") 
plt.ylabel('Referencias con su antiguedad (años)', color= "red")

plt.show()