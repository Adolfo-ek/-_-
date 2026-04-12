MyGraph - Implementación de Grafos
📌 Descripción
Este proyecto consiste en la implementación de un Grafo en Python, como parte de la actividad:

ACT Clase - GRAFO
Unidad 4 - Estructuras No-Lineales

El objetivo es comprender el manejo de estructuras no lineales y sus operaciones básicas.

🧠 Concepto
Un grafo es una estructura de datos compuesta por:

Nodos (vértices)
Conexiones (aristas)
Puede representar redes, caminos, relaciones, etc.

🏗️ Estructura
MyGraph: Clase principal
Representación mediante diccionario (lista de adyacencia)
⚙️ Funcionalidades
✔ Agregar vértices
✔ Agregar aristas
✔ Eliminar aristas
✔ Eliminar nodos
✔ Recorrido BFS (anchura)
✔ Recorrido DFS (profundidad)
✔ Mostrar grafo

🚀 Ejemplo
g = MyGraph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")

g.display()
