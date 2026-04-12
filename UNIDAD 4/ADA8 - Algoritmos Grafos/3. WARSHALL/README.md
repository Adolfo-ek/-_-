# Algoritmo de Warshall

## 📌 Descripción General
El algoritmo de Warshall es una técnica utilizada para determinar la conectividad entre todos los pares de nodos en un grafo dirigido.

A diferencia de otros algoritmos como Dijkstra o Floyd, Warshall no calcula distancias, sino que indica si existe o no un camino entre dos nodos.

---

## 🧠 Fundamento Teórico
El algoritmo se basa en el concepto de **cierre transitivo**, el cual permite identificar si un nodo puede alcanzar a otro mediante uno o más caminos intermedios.

Se apoya en programación dinámica, evaluando si un nodo intermedio permite conectar dos nodos previamente no conectados.

---

## ⚙️ Funcionamiento
1. Se parte de una matriz de adyacencia (0 y 1).
2. Se toma cada nodo como intermedio.
3. Se verifica si existe un camino indirecto entre pares de nodos.
4. Se actualiza la matriz de alcanzabilidad.

---

## 📊 Complejidad
- Tiempo: O(n³)
- Espacio: O(n²)

---

## 🚀 Aplicaciones
- Análisis de conectividad en redes
- Sistemas de dependencias (software, bases de datos)
- Grafos de relaciones
- Verificación de accesibilidad entre nodos

---

## ▶️ Ejecución
```bash
python warshall.py
