📚 Ordenamiento por Selección - Visualización Interactiva
👥 Integrantes
Freddy Armando Che Fernández
Chacón Olvera Christian André
Gómez Ek Adolfo René
Chac Chay José Cristóbal
Adrián Mauricio Acuña Tejeda
José Natanael Canché Pech
Zyon Máximo Rodríguez González
📌 Descripción del Proyecto

Este proyecto consiste en una aplicación interactiva desarrollada en Python que permite visualizar paso a paso el funcionamiento del algoritmo de ordenamiento por selección (Selection Sort).

La aplicación utiliza una analogía del mundo real:
📖 organizar libros en una estantería según su año de publicación.

El sistema muestra gráficamente cómo el algoritmo:

Busca el elemento mínimo
Realiza comparaciones
Intercambia posiciones
Construye la lista ordenada progresivamente
🎯 Objetivo

Facilitar la comprensión del algoritmo de ordenamiento por selección mediante una representación visual dinámica que permita:

Analizar cada paso del algoritmo
Identificar comparaciones e intercambios
Comprender su funcionamiento en un contexto real
🧠 ¿Qué es el Ordenamiento por Selección?

El Selection Sort es un algoritmo de ordenamiento que:

Divide la lista en dos partes:
Parte ordenada
Parte desordenada
Busca el elemento más pequeño de la parte desordenada
Lo intercambia con el primer elemento no ordenado
Repite el proceso hasta ordenar toda la lista
📊 Complejidad
Caso	Complejidad
Mejor caso	O(n²)
Promedio	O(n²)
Peor caso	O(n²)

✔ No depende del estado inicial de la lista
✔ Realiza pocas operaciones de intercambio

⚙️ Tecnologías Utilizadas
🐍 Python 3
🖼 Tkinter (Interfaz gráfica)
📊 Matplotlib (Visualización)
🔢 NumPy (Manejo de datos)
🖥️ Funcionalidades
🎮 Interacción
▶ Siguiente paso: Avanza en el algoritmo
◀ Paso anterior: Retrocede
⏮ Inicio: Regresa al inicio
⏭ Fin: Va al final
🔄 Reiniciar: Reinicia la simulación
📊 Visualización

El gráfico de barras representa los datos (años de publicación):

🟢 Verde → Elementos ya ordenados
🟡 Dorado → Elemento mínimo actual
🟠 Naranja → Elemento en comparación
🔵 Azul → Elementos pendientes
💬 Información Dinámica
Muestra el paso actual
Explica lo que está ocurriendo en cada momento
Describe comparaciones e intercambios
🧪 Datos de Ejemplo
[2015, 2008, 2020, 2005, 2018, 2010, 2003, 2022, 1999, 2012]

Representan años de publicación de libros.

🚀 Cómo Ejecutar el Proyecto
1. Instalar dependencias
pip install matplotlib numpy

(Tkinter ya viene incluido en la mayoría de instalaciones de Python)

2. Ejecutar el programa
python nombre_del_archivo.py
🧩 Estructura del Código
Clase principal
OrdenamientoSeleccionApp
Métodos importantes:
generar_historial() → Ejecuta el algoritmo y guarda cada paso
mostrar_grafico() → Dibuja la visualización
actualizar_info() → Actualiza textos y estado
paso_siguiente() → Avanza
paso_anterior() → Retrocede
reiniciar() → Reinicia el proceso
🔍 Funcionamiento Interno

El programa no ejecuta el algoritmo en tiempo real, sino que:

Precalcula todos los pasos
Guarda cada estado en una lista (historial)
Permite navegar entre esos estados

Esto mejora:

Rendimiento
Control del usuario
Claridad visual
🌎 Aplicaciones en la Vida Real

Aunque no es el más eficiente para grandes volúmenes, el algoritmo de selección se utiliza en:

Sistemas educativos (visualización de algoritmos)
Procesamiento de listas pequeñas
Casos donde se minimizan intercambios
Sistemas embebidos con recursos limitados
⚖️ Ventajas y Desventajas
✅ Ventajas
Fácil de entender e implementar
Pocos intercambios
No requiere memoria adicional
❌ Desventajas
Ineficiente para grandes volúmenes
Siempre O(n²)
Más lento que otros algoritmos como QuickSort o MergeSort
📈 Conclusión

Este proyecto demuestra de forma clara y visual cómo funciona el algoritmo de ordenamiento por selección, facilitando su aprendizaje mediante:

Interacción directa
Representación gráfica
Explicación paso a paso

Es una herramienta ideal para estudiantes que están comenzando en estructuras de datos y algoritmos.

📚 Referencias
Cormen, T. H. et al. Introduction to Algorithms
Weiss, M. A. Data Structures and Algorithm Analysis
Documentación oficial de Python
Documentación de Matplotlib
🧑‍💻 Autoría

Proyecto académico desarrollado con fines educativos.
