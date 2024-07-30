import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

# Por disciplina

#valores
field = ['IT', 'Sociología', 'Economía', 'Desarrollo Urbano', 'Filosofia']
slic = [3, 3, 2, 2, 1]
lang = ['Español: 54,54%', 'Inglés: 45.45%']

# colores
colour = ['r', 'b', 'g', 'y', 'gray']
col = ['r', 'b']

# dibujo
plt.pie(slic, labels = field, colors=colour, 
        startangle=90, shadow = True, explode = (0.1, 0.1, 0.05, 0.05, 0),
        radius = 0.6, autopct = '%1.1f%%')

plt.legend(title = 'Idiomas', labels = lang, loc="best")
plt.title('DIAGRAMA #3: DISTRIBUCIÓN POR CAMPO DISCIPLINARIO', color = "blue", fontweight = 'bold')

# showing the plot
plt.show()