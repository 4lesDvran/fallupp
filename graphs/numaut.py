import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

# Por número de autores

#Valores
left = [1, 2, 3, 4, 5]
height = [4, 2, 0, 3, 2]
tick_label = ['1', '2', '3', '4 o más', 'Corporativo']

# dibujado
plt.bar(left, height, tick_label = tick_label,
        width = 0.6, color = ['blue'])

# grafica
plt.xlabel('N. de autores', color = "green")
plt.ylabel('N. de referencias', color = "red")
plt.title('DIAGRAMA #2: REF. POR NÚMERO DE AUTORES', color = "blue", fontweight = 'bold')

plt.show()
