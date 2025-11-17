from tree import BinaryTree
from queue_ import Queue
from collections import defaultdict
from typing import List as TList, Dict, Any

# IMPORTA EL DATASET (queda en archivo aparte)
from pokemon_dataset_ejemplo import pokemons


# ============================================================
#                A) ARMADO DE LOS ÁRBOLES
# ============================================================

def build_trees(pokemons: TList[Dict[str, Any]]):
    tree_by_name = BinaryTree()
    tree_by_number = BinaryTree()
    tree_by_type = BinaryTree()

    for p in pokemons:
        tree_by_name.insert(p["name"], p)
        tree_by_number.insert(p["number"], p)

        for t in p.get("types", []):
            node = tree_by_type.search(t)
            if node is None:
                tree_by_type.insert(t, {"pokemons": [p]})
            else:
                node.other_values["pokemons"].append(p)

    return tree_by_name, tree_by_number, tree_by_type


# ============================================================
#                    B) BUSCAR POR NÚMERO
# ============================================================

def find_by_number(tree_by_number: BinaryTree, number: int):
    node = tree_by_number.search(number)
    return node.other_values if node else None


# ============================================================
#                    B) BUSCAR POR NOMBRE (PROXIMIDAD)
# ============================================================

def find_by_name_proximity(tree_by_name: BinaryTree, fragment: str):
    res = []
    frag = fragment.lower()

    def _rec(root):
        if root is None:
            return
        _rec(root.left)
        if frag in root.value.lower():
            res.append(root.other_values)
        _rec(root.right)

    if tree_by_name.root:
        _rec(tree_by_name.root)
    return res


# ============================================================
#                 C) POKÉMONS POR TIPOS
# ============================================================

def names_by_type(tree_by_type: BinaryTree, tipo: str):
    node = tree_by_type.search(tipo)
    if node:
        return [p["name"] for p in node.other_values.get("pokemons", [])]
    return []


# ============================================================
#                D) LISTADOS ORDENADOS
# ============================================================

def list_ascending_by_number(tree_by_number: BinaryTree):
    res = []

    def _in(root):
        if root:
            _in(root.left)
            res.append(root.other_values)
            _in(root.right)

    if tree_by_number.root:
        _in(tree_by_number.root)
    return res


def list_ascending_by_name(tree_by_name: BinaryTree):
    res = []

    def _in(root):
        if root:
            _in(root.left)
            res.append(root.other_values)
            _in(root.right)

    if tree_by_name.root:
        _in(tree_by_name.root)
    return res


def list_by_level_names(tree_by_name: BinaryTree):
    out = []
    q = Queue()

    if not tree_by_name.root:
        return out

    q.arrive(tree_by_name.root)
    while q.size() > 0:
        node = q.attention()
        out.append(node.value)
        if node.left:
            q.arrive(node.left)
        if node.right:
            q.arrive(node.right)

    return out


# ============================================================
#          E) POKÉMONS DÉBILES FRENTE A OTROS
# ============================================================

def pokemons_weak_to(pokemons: TList[Dict[str, Any]], targets: TList[str]):
    name_to_types = {p["name"]: set(p.get("types", [])) for p in pokemons}

    target_types = set()
    for t in targets:
        if t in name_to_types:
            target_types.update(name_to_types[t])

    result = []
    for p in pokemons:
        weaknesses = set(p.get("weaknesses", []))

        if weaknesses & target_types:
            result.append(p)
            continue

        if any(t in weaknesses for t in targets):
            result.append(p)

    return result


# ============================================================
#                 F) CONTEO POR TIPOS
# ============================================================

def count_by_type(pokemons: TList[Dict[str, Any]]):
    counter = defaultdict(int)
    for p in pokemons:
        for t in p.get("types", []):
            counter[t] += 1
    return dict(counter)


# ============================================================
#          G) MEGAEVOLUCIONES / H) GIGAMAX
# ============================================================

def count_megas_and_gigamax(pokemons: TList[Dict[str, Any]]):
    mega = sum(1 for p in pokemons if p.get("mega", False))
    gigamax = sum(1 for p in pokemons if p.get("gigamax", False))
    return mega, gigamax


# ============================================================
#                    EJECUCIÓN DEL PARCIAL
# ============================================================

def main():
    tree_by_name, tree_by_number, tree_by_type = build_trees(pokemons)

    print("===== B) BUSCAR POR NÚMERO Y NOMBRE =====")

    # Buscar por número
    num = 25
    print("\nDatos del Pokémon Nº 25:")
    print(find_by_number(tree_by_number, num))

    # Buscar por proximidad
    fragmento = "bul"
    print(f"\nPokémon cuyo nombre contiene '{fragmento}':")
    for p in find_by_name_proximity(tree_by_name, fragmento):
        print(" -", p["name"], "(Nº", p["number"], ")")

    print("\n===== C) POKÉMONS POR TIPO =====")
    for tipo in ["Fantasma", "Fuego", "Acero", "Eléctrico"]:
        print(f"\nTipo {tipo}:")
        for n in names_by_type(tree_by_type, tipo):
            print(" -", n)

    print("\n===== D) LISTADOS ORDENADOS =====")

    print("\nPor número:")
    for p in list_ascending_by_number(tree_by_number):
        print(" -", p["number"], p["name"])

    print("\nPor nombre:")
    for p in list_ascending_by_name(tree_by_name):
        print(" -", p["name"], "(Nº", p["number"], ")")

    print("\nPor niveles (BFS):")
    for name in list_by_level_names(tree_by_name):
        print(" -", name)

    print("\n===== E) DÉBILES FRENTE A JOLTEON, LYCANROC Y TYRANTRUM =====")

    objetivos = ["Jolteon", "Lycanroc", "Tyrantrum"]
    for p in pokemons_weak_to(pokemons, objetivos):
        print(" -", p["name"])

    print("\n===== F) CANTIDAD POR TIPO =====")
    for tipo, cant in count_by_type(pokemons).items():
        print(tipo, ":", cant)

    print("\n===== G) MEGAEVOLUCIONES =====")
    mega, giga = count_megas_and_gigamax(pokemons)
    print("Megaevoluciones:", mega)

    print("\n===== H) GIGAMAX =====")
    print("Gigamax:", giga)


# Ejecuta todo
if __name__ == "__main__":
    main()
