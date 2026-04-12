# Algoritmo de Kruskal

## 📌 Descripción General
El algoritmo de Kruskal es un método utilizado para encontrar el **Árbol Generador Mínimo (Minimum Spanning Tree, MST)** de un grafo no dirigido y ponderado.

Un árbol generador mínimo es un subconjunto de aristas que conecta todos los nodos del grafo sin formar ciclos y con el menor costo total posible.

---

## 🧠 Fundamento Teórico
Kruskal es un algoritmo de tipo voraz (greedy), el cual en cada paso selecciona la arista de menor peso disponible, siempre que no forme un ciclo con las aristas ya seleccionadas.

Para evitar ciclos, se utiliza una estructura de datos llamada **Union-Find (Disjoint Set)**.

---

## ⚙️ Funcionamiento
El algoritmo sigue los siguientes pasos:

1. Ordenar todas las aristas del grafo en orden ascendente según su peso.
2. Inicializar una estructura Union-Find para manejar conjuntos disjuntos.
3. Recorrer las aristas ordenadas:
   - Si la arista conecta dos componentes diferentes, se agrega al MST.
   - Si forma un ciclo, se descarta.
4. El proceso continúa hasta que el MST tenga (n - 1) aristas.

---

## 📊 Complejidad
- Tiempo: O(E log E)
- Espacio: O(V)

Donde:
- V = número de vértices
- E = número de aristas

---

## 🚀 Aplicaciones
- Diseño de redes eléctricas
- Construcción de carreteras
- Redes de telecomunicaciones
- Optimización de conexiones

---

## ▶️ Ejecución
```bash
python kruskal.py
