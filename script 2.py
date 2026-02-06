import matplotlib.pyplot as plt
import numpy as np

# 1. Tus Mejoras
mejoras = [
    'RBAC\n(Roles)', 
    'MFA\n(Doble Factor)', 
    'Auditoría\n(Logging)', 
    'Cifrado\n(Datos)'
]

# 2. Conversión de tus datos a escala numérica (1 a 10)
# Viabilidad: Alta = 9, Media = 5, Baja = 2
viabilidad = [9, 5, 9, 9] 

# Impacto: Alto = 9, Medio = 5, Bajo = 2
impacto = [9, 9, 9, 9]

x = np.arange(len(mejoras))
width = 0.35

# 3. Creación del Gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Barras de Viabilidad (Azul)
barras_viabilidad = ax.bar(x - width/2, viabilidad, width, label='Viabilidad Técnica', color='#3498db', alpha=0.9)

# Barras de Impacto (Naranja)
barras_impacto = ax.bar(x + width/2, impacto, width, label='Impacto en Calidad', color='#e67e22', alpha=0.9)

# 4. Configuración Visual
ax.set_ylabel('Escala de Valoración (1-10)', fontsize=12)
ax.set_title('Matriz de Priorización: Viabilidad vs. Impacto', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(mejoras, fontsize=11, fontweight='bold')
ax.set_ylim(0, 12)
ax.legend(loc='upper right')
ax.grid(axis='y', linestyle='--', alpha=0.3)

# Función para poner las etiquetas de texto (Alta/Media/Baja) sobre las barras
def etiquetar_barras(rects, tipo_dato):
    for rect, valor in zip(rects, tipo_dato):
        height = rect.get_height()
        # Decidimos el texto según el valor numérico
        texto = "ALTA" if valor >= 8 else ("MEDIA" if valor >= 5 else "BAJA")
        
        ax.annotate(texto,
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, fontweight='bold')

# Llamamos a la función usando tus datos originales para las etiquetas
etiquetar_barras(barras_viabilidad, viabilidad)
etiquetar_barras(barras_impacto, impacto)

# 5. Mostrar
plt.tight_layout()
print("Generando análisis de viabilidad...")
plt.show()