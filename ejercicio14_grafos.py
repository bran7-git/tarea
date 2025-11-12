

import sys
import os
sys.path.append(os.path.dirname(__file__))
from graph import Graph


def construir_grafo_casa():
   
    g = Graph(is_directed=True)

    ambientes = [
        "Cocina", "Comedor", "Cochera", "Quincho", "Baño 1", "Baño 2",
        "Habitación 1", "Habitación 2", "Sala de estar", "Terraza", "Patio"
    ]

    
    for amb in ambientes:
        g.insert_vertex(amb)

    # Cargar aristas (distancias en metros)
    aristas = [
        ("Cocina", "Comedor", 4),
        ("Cocina", "Baño 1", 6),
        ("Cocina", "Patio", 5),
        ("Comedor", "Sala de estar", 3),
        ("Comedor", "Baño 1", 4),
        ("Comedor", "Terraza", 7),
        ("Cochera", "Patio", 8),
        ("Cochera", "Baño 2", 5),
        ("Cochera", "Habitación 1", 9),
        ("Quincho", "Patio", 4),
        ("Quincho", "Terraza", 6),
        ("Quincho", "Comedor", 10),
        ("Baño 1", "Habitación 1", 4),
        ("Baño 2", "Habitación 2", 3),
        ("Habitación 1", "Habitación 2", 5),
        ("Habitación 1", "Sala de estar", 6),
        ("Habitación 2", "Terraza", 8),
        ("Sala de estar", "Terraza", 4),
        ("Sala de estar", "Patio", 5),
        ("Terraza", "Patio", 7)
    ]

    # Cargar las aristas en el grafo
    for origen, destino, peso in aristas:
        g.insert_edge(origen, destino, peso)

    return g


def arbol_expansion_minima(g):
    print("\n=== (c) Árbol de expansión mínima (Kruskal) ===")
    resultado = g.kruskal("Cocina")
    print("Representación devuelta por kruskal():")
    print(resultado)

    # Calcular la suma de los pesos
    total = 0
    partes = resultado.split(";")
    for parte in partes:
        datos = parte.split("-")
        if len(datos) >= 3:
            try:
                total += int(datos[-1])
            except ValueError:
                pass
    print(f"\nTotal de metros de cable necesarios: {total} m")


def camino_mas_corto(g, origen, destino):
    print(f"\n=== (d) Camino más corto desde '{origen}' hasta '{destino}' ===")
    pila = g.dijkstra(origen)
    datos = []
    while pila.size() > 0:
        datos.append(pila.pop())

    dic = {v: (c, p) for v, c, p in datos}
    if destino not in dic:
        print("No existe camino.")
        return

    # Reconstruir camino
    camino = []
    actual = destino
    costo_total = dic[actual][0]
    while actual is not None:
        camino.append(actual)
        actual = dic[actual][1]
    camino.reverse()

    print(f"Camino: {' -> '.join(camino)}")
    print(f"Distancia total: {costo_total} m")


def main():
    print("=== Ejercicio 14: Conexión de ambientes de una casa ===")
    g = construir_grafo_casa()

    print("\nLista de adyacencia (conexiones entre ambientes):")
    g.show()

    # Punto (c): Árbol de expansión mínima
    arbol_expansion_minima(g)

    # Punto (d): Camino más corto entre Habitación 1 y Sala de estar
    camino_mas_corto(g, "Habitación 1", "Sala de estar")

    print("\n--- Ejecución finalizada correctamente ---")


if __name__ == "__main__":
    main()
