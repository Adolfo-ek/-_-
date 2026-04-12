# ==========================================
# ALGORITMO DE DIJKSTRA
# ==========================================

import heapq


class Grafo:
    def __init__(self):
        """
        Representación del grafo mediante lista de adyacencia.
        Cada nodo tiene un diccionario de vecinos con sus respectivos pesos.
        """
        self.grafo = {}

    def agregar_arista(self, origen, destino, peso):
        """
        Agrega una arista bidireccional con peso.
        """
        if origen not in self.grafo:
            self.grafo[origen] = {}
        if destino not in self.grafo:
            self.grafo[destino] = {}

        self.grafo[origen][destino] = peso
        self.grafo[destino][origen] = peso

    def dijkstra(self, inicio):
        """
        Implementación del algoritmo de Dijkstra.
        Retorna un diccionario con las distancias mínimas desde el nodo inicial.
        """
        distancias = {nodo: float('inf') for nodo in self.grafo}
        distancias[inicio] = 0

        cola_prioridad = [(0, inicio)]

        while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

            for vecino, peso in self.grafo[nodo_actual].items():
                nueva_distancia = distancia_actual + peso

                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

        return distancias


# =========================
# EJEMPLO
# =========================
if __name__ == "__main__":
    g = Grafo()

    g.agregar_arista("A", "B", 4)
    g.agregar_arista("A", "C", 2)
    g.agregar_arista("B", "C", 1)
    g.agregar_arista("B", "D", 5)
    g.agregar_arista("C", "D", 8)

    print("Distancias mínimas desde A:")
    print(g.dijkstra("A"))
