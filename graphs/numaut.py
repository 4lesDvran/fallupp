import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

# Por número de autores

#Valores
left = [1, 2, 3, 4, 5]
height = [4, 2, 0, 3, 2]

# labels for bars
tick_label = ['1', '2', '3', '4 o más', 'Corporativo']

# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.6, color = ['blue'])

# naming the x-axis
plt.xlabel('N. de autores', color = "green")
# naming the y-axis
plt.ylabel('N. de referencias', color = "red")
# plot title
plt.title('DIAGRAMA #2: REF. POR NÚMERO DE AUTORES', color = "blue", fontweight = 'bold')

# function to show the plot
plt.show()