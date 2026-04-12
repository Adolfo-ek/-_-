# Algoritmo de Dijkstra

## 📌 Descripción General
El algoritmo de Dijkstra es un método utilizado para encontrar las rutas más cortas desde un nodo origen hacia todos los demás nodos en un grafo ponderado, siempre que los pesos sean no negativos.

Este algoritmo es ampliamente utilizado en problemas de optimización de rutas, redes y sistemas de navegación.

---

## 🧠 Fundamento Teórico
Dijkstra se basa en una estrategia voraz (greedy), en la que en cada iteración se selecciona el nodo con la menor distancia acumulada conocida, garantizando que dicha distancia es óptima.

---

## ⚙️ Funcionamiento
1. Se asigna distancia infinita a todos los nodos excepto al nodo inicial.
2. Se utiliza una cola de prioridad para seleccionar el nodo más cercano.
3. Se actualizan las distancias de los nodos vecinos.
4. El proceso se repite hasta recorrer todos los nodos.

---

## 📊 Complejidad
- Tiempo: O((V + E) log V)
- Espacio: O(V)

---

## 🚀 Aplicaciones
- Sistemas GPS
- Redes de computadoras
- Optimización de rutas logísticas

---

## ▶️ Ejecución
```bash
python dijkstra.py
