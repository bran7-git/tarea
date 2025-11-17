from graph import Graph

# ----------------------------------------
# CARGA DEL GRAFO
# ----------------------------------------

g = Graph(is_directed=False)

personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO",
    "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]

# Insertar vértices
for p in personajes:
    g.insert_vertex(p)

# ----------------------------------------
# ARISTAS (cantidad de episodios compartidos)

# ----------------------------------------

g.insert_edge("Luke Skywalker", "Darth Vader", 4)
g.insert_edge("Luke Skywalker", "Yoda", 3)
g.insert_edge("Luke Skywalker", "Leia", 6)
g.insert_edge("Luke Skywalker", "Han Solo", 5)
g.insert_edge("Luke Skywalker", "R2-D2", 7)

g.insert_edge("Darth Vader", "Leia", 4)
g.insert_edge("Darth Vader", "Kylo Ren", 2)

g.insert_edge("Yoda", "Luke Skywalker", 3)
g.insert_edge("Yoda", "C-3PO", 2)
g.insert_edge("Yoda", "Rey", 1)

g.insert_edge("C-3PO", "R2-D2", 9)
g.insert_edge("C-3PO", "Leia", 7)
g.insert_edge("C-3PO", "Han Solo", 4)

g.insert_edge("Han Solo", "Chewbacca", 9)
g.insert_edge("Han Solo", "Leia", 6)
g.insert_edge("Han Solo", "Kylo Ren", 1)

g.insert_edge("Rey", "BB-8", 3)
g.insert_edge("Rey", "Kylo Ren", 3)

g.insert_edge("Kylo Ren", "Darth Vader", 2)
g.insert_edge("BB-8", "R2-D2", 1)

# ----------------------------------------
# (b) Árbol de expansión mínimo desde C-3PO, Yoda y Leia
# ----------------------------------------

print("\n==== Árbol de expansión mínimo desde C-3PO ====")
print(g.kruskal("C-3PO"))

print("\n==== Árbol de expansión mínimo desde Yoda ====")
print(g.kruskal("Yoda"))

print("\n==== Árbol de expansión mínimo desde Leia ====")
print(g.kruskal("Leia"))

# ----------------------------------------
# (c) Número máximo de episodios compartidos entre dos personajes
# ----------------------------------------

print("\n==== Máxima relación entre personajes ====")

maximo = 0
pares = []

for vertex in g:
    for edge in vertex.edges:
        if edge.weight > maximo:
            maximo = edge.weight
            pares = [(vertex.value, edge.value)]
        elif edge.weight == maximo:
            pares.append((vertex.value, edge.value))

print(f"Mayor cantidad de episodios compartidos: {maximo}")
print("Pares con ese valor:")
for p in set(pares):
    print(p)

# ----------------------------------------
# (e) Camino más corto: Dijkstra
# ----------------------------------------

def mostrar_camino(origen, destino):
    path = g.dijkstra(origen)
    recorrido = []
    costo = None

    while path.size() > 0:
        dato = path.pop()
        if dato[0] == destino:
            if costo is None:
                costo = dato[1]
            recorrido.append(dato[0])
            destino = dato[2]

    recorrido.reverse()
    print(f"\nCamino más corto desde {origen}: {' -> '.join(recorrido)} (costo: {costo})")


mostrar_camino("C-3PO", "R2-D2")
mostrar_camino("Yoda", "Darth Vader")

# ----------------------------------------
# (f) Personajes que aparecieron en los 9 episodios
# ----------------------------------------

print("\n==== Personajes que aparecieron en los 9 episodios ====")

personajes_9 = ["C-3PO", "R2-D2"]  

for p in personajes_9:
    print(p)
