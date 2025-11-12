

import sys
import os
sys.path.append(os.path.dirname(__file__))  # usa la carpeta actual
from graph import Graph


def build_graph():
    g = Graph(is_directed=True)  # usar True para que la implementación agregue aristas recíprocas
    nodes = {
        'Parrot': 'pc',
        'Manjaro': 'pc',
        'Fedora': 'pc',
        'Ubuntu': 'pc',
        'Mint': 'pc',
        'Red Hat': 'notebook',
        'Debian': 'notebook',
        'Arch': 'notebook',
        'MongoDB': 'servidor',
        'Guaraní': 'servidor',
        'Impresora': 'impresora',
        'Switch 1': 'switch',
        'Switch 2': 'switch',
        'Router 1': 'router',
        'Router 2': 'router',
        'Router 3': 'router'
    }
    for name, tipo in nodes.items():
        g.insert_vertex(name)
        pos = g.search(name, 'value')
        if pos is not None:
            g[pos].other_values = tipo

    edges = [
        ('Switch 1', 'Router 1', 29),
        ('Switch 1', 'Debian', 17),
        ('Switch 1', 'Ubuntu', 18),
        ('Switch 1', 'Mint', 80),
        ('Switch 1', 'Impresora', 22),

        ('Router 2', 'Guaraní', 9),

        ('Router 3', 'Switch 2', 61),

        ('Router 1', 'Router 2', 37),
        ('Router 1', 'Router 3', 43),

        ('Router 2', 'Red Hat', 25),
        ('Router 2', 'Router 3', 50),

        ('Switch 2', 'Manjaro', 40),
        ('Switch 2', 'Parrot', 12),
        ('Switch 2', 'MongoDB', 5),
        ('Switch 2', 'Arch', 56),
        ('Switch 2', 'Fedora', 3)
    ]
    for o, d, w in edges:
        g.insert_edge(o, d, w)
    return g

def run_depth_and_breadth(g, starts):
    print("=== (b) BARRIDOS EN PROFUNDIDAD (DFS) ===")
    for s in starts:
        print(f"\n-- Desde (DFS): {s} --")
        g.deep_sweep(s)
    print("\n=== (b) BARRIDOS EN AMPLITUD (BFS) ===")
    for s in starts:
        print(f"\n-- Desde (BFS): {s} --")
        g.amplitude_sweep(s)

def dijkstra_to_dict(g, source):
    stack = g.dijkstra(source)
    result = {}
    temp = []
    while stack.size() > 0:
        temp.append(stack.pop())
    for name, cost, pred in temp:
        result[name] = (cost, pred)
    return result

def reconstruct_path(dijkstra_dict, target):
    if target not in dijkstra_dict:
        return None, None
    cost, pred = dijkstra_dict[target]
    if cost is None or cost == float('inf'):
        return None, None
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        _, cur = dijkstra_dict.get(cur, (None, None))
    path.reverse()
    return path, cost

def shortest_path_to_printer(g, sources, printer_name='Impresora'):
    print("\n=== (c) CAMINO MÁS CORTO hacia la impresora ===")
    for src in sources:
        print(f"\nDesde {src} hasta {printer_name}:")
        d = dijkstra_to_dict(g, src)
        path, cost = reconstruct_path(d, printer_name)
        if path is None:
            print("  No hay camino disponible.")
        else:
            print(f"  Camino: {' -> '.join(path)}  |  Costo total = {cost}")

def minimal_spanning_tree(g, origin_vertex):
    print("\n=== (d) ÁRBOL DE EXPANSIÓN MÍNIMA (KRUSKAL) ===")
    forest_repr = g.kruskal(origin_vertex)
    print("Representación interna devuelta por kruskal():", forest_repr)
    try:
        parts = forest_repr.split(';')
        total = 0
        edges = []
        for part in parts:
            subparts = part.split('-')
            if len(subparts) >= 3:
                peso = int(subparts[-1])
                total += peso
                edges.append(part)
        if edges:
            print("Aristas en el árbol (fragmentos):")
            for e in edges:
                print(" ", e)
            print("Peso total aproximado (sumando últimos números después de '-'): ", total)
    except Exception as ex:
        print("No se pudo calcular el peso total automáticamente:", ex)

def best_pc_to_server(g, server_name='Guaraní'):
    print(f"\n=== (e) PC (no notebook) con CAMINO MÁS CORTO a {server_name} ===")
    best = None
    best_cost = float('inf')
    for v in g:
        tipo = getattr(v, 'other_values', None)
        name = v.value
        if tipo == 'pc':
            d = dijkstra_to_dict(g, name)
            _, cost = reconstruct_path(d, server_name)
            if cost is not None and cost < best_cost:
                best_cost = cost
                best = name
    if best is None:
        print("  No se encontró ninguna PC (no notebook) con camino a", server_name)
    else:
        print(f"  Mejor PC: {best} con costo {best_cost}")

def best_from_switch1_to_mongodb(g, switch_name='Switch 1', target_server='MongoDB'):
    print(f"\n=== (f) Mejor computadora del {switch_name} hacia {target_server} ===")
    pos = g.search(switch_name, 'value')
    if pos is None:
        print("Switch no encontrado.")
        return
    neighbors = [edge.value for edge in g[pos].edges]
    best = None
    best_cost = float('inf')
    for nb in neighbors:
        d = dijkstra_to_dict(g, nb)
        _, cost = reconstruct_path(d, target_server)
        if cost is not None and cost < best_cost:
            best_cost = cost
            best = nb
    if best is None:
        print("  Ningún vecino del switch tiene camino a", target_server)
    else:
        print(f"  Mejor desde {best} con costo {best_cost}")

def reconnect_printer_and_repeat(g):
    print("\n=== (g) RECONEXIÓN: impresora ahora conectada a Router 2 ===")
    deleted = g.delete_edge('Switch 1', 'Impresora', 'value')
    print("  Arista Switch1-Impresora eliminada?:", deleted is not None)
    g.insert_edge('Router 2', 'Impresora', 22)
    print("\nRe-ejecutando barridos desde Red Hat, Debian y Arch:")
    run_depth_and_breadth(g, ['Red Hat', 'Debian', 'Arch'])

def main():
    g = build_graph()
    print("GRAFO CARGADO: Vértices y sus tipos\n----------------------------------")
    for v in g:
        print(f"{v.value}  (tipo: {v.other_values})")
    print("\nConexiones (lista de adyacencia):\n---------------------------------")
    g.show()

    run_depth_and_breadth(g, ['Red Hat', 'Debian', 'Arch'])
    shortest_path_to_printer(g, ['Manjaro', 'Red Hat', 'Fedora'], 'Impresora')
    minimal_spanning_tree(g, 'Manjaro')
    best_pc_to_server(g, 'Guaraní')
    best_from_switch1_to_mongodb(g, 'Switch 1', 'MongoDB')
    reconnect_printer_and_repeat(g)

if __name__ == '__main__':
    main()
