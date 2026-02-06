import matplotlib.pyplot as plt
import numpy as np


categorias = ['Control de Acceso', 'Auditoría/Trazabilidad', 'Cifrado de Datos']


riesgo_actual = [9, 10, 8] 


riesgo_propuesto = [2, 1, 2]

x = np.arange(len(categorias)) 
width = 0.35 


fig, ax = plt.subplots(figsize=(10, 6))

rects1 = ax.bar(x - width/2, riesgo_actual, width, label='Situación Actual (Alto Riesgo)', color='#ff4d4d', alpha=0.8)


rects2 = ax.bar(x + width/2, riesgo_propuesto, width, label='Con Mejoras de Seguridad', color='#2ecc71', alpha=0.9)

ax.set_ylabel('Nivel de Exposición al Riesgo (0-10)', fontsize=12)
ax.set_title('Matriz de Reducción de Riesgos de Seguridad', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categorias, fontsize=11)
ax.set_ylim(0, 12) 
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.3)


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}/10',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontweight='bold')

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
print("Generando Matriz de Riesgos...")
plt.show()