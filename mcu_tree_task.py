
from tree import BinaryTree
from super_heroes_data import superheroes



def find_node_by_prefix(tree: BinaryTree, prefix: str):
    """Devuelve el nodo (objeto interno) cuyo valor (nombre) empieza con prefix, o None."""
    result = None

    def _search(root):
        nonlocal result
        if root is None or result is not None:
            return
        if isinstance(root.value, str) and root.value.startswith(prefix):
            result = root
            return
        _search(root.left)
        _search(root.right)

    if tree.root is not None:
        _search(tree.root)
    return result


def count_nodes(tree: BinaryTree):
    """Cuenta todos los nodos de un árbol."""
    def _count(root):
        if root is None:
            return 0
        return 1 + _count(root.left) + _count(root.right)

    return _count(tree.root)


def print_descending(tree: BinaryTree):
    """Imprime los nombres en orden alfabético descendente (Z -> A)."""
    def _desc(root):
        if root is None:
            return
        _desc(root.right)
        print(root.value)
        _desc(root.left)

    _desc(tree.root)


# ---------- Construcción del árbol principal ----------

mcu_tree = BinaryTree()

# Insertamos manteniendo compatibilidad con el `tree.py` del profesor.
# - el dataset trae 'is_villain' (True si es villano). La consigna pide un campo booleano
#   que indique si es héroe (True) o villano (False). Vamos a añadir ambos campos:
#   'is_hero' (True/False según consigna) y mantener 'is_villain' para métodos existentes.

for item in superheroes:
    node_data = item.copy()
    # Añadimos is_hero (True si NO es villano)
    node_data['is_hero'] = not bool(item.get('is_villain', False))
    # Mantenemos is_villain para compatibilidad con tree.villain_in_order y count_heroes
    node_data['is_villain'] = bool(item.get('is_villain', False))
    # Guardamos tambien el nombre dentro de other_values para facilitar actualizaciones
    node_data['name'] = item['name']
    mcu_tree.insert(item['name'], node_data)

# ---------- b) listar los villanos ordenados alfabéticamente ----------
print('--- b) Villanos ordenados (A -> Z) ---')
# El tree.py ya tiene villain_in_order que hace in-order y filtra por other_values['is_villain']
mcu_tree.villain_in_order()
print()

# ---------- c) mostrar todos los superhéroes que empiezan con C ----------
print("--- c) Superhéroes que empiezan con 'C' ---")
# Podemos usar proximity_search que ya imprime coincidencias por prefijo.
# Para evitar que aparezcan villanos con C, hacemos un in-order y filtramos por is_hero.

def heroes_starting_with(tree: BinaryTree, prefix: str):
    matches = []
    def _in(root):
        if root is None:
            return
        _in(root.left)
        if root.other_values.get('is_hero') and root.value.startswith(prefix):
            matches.append(root.value)
        _in(root.right)
    _in(tree.root)
    return matches

matches_c = heroes_starting_with(mcu_tree, 'C')
for name in matches_c:
    print(name)
print()

# ---------- d) determinar cuántos superhéroes hay en el árbol ----------
print('--- d) Cantidad de superhéroes en el árbol ---')
# El tree.py incluye count_heroes que cuenta donde other_values['is_villain'] is False
heroes_count = mcu_tree.count_heroes()
print(f'Total héroes: {heroes_count}\n')

# ---------- e) Doctor Strange está mal cargado: buscar por proximidad y modificar su nombre ----------
print('--- e) Corregir Doctor Strange mediante búsqueda por proximidad ---')
# Buscamos nodos cuyo nombre empiece con 'Dr' o que contengan 'Strange' mal escrito.
# Primero intentamos con prefijo 'Dr'
node_dr = find_node_by_prefix(mcu_tree, 'Dr')
if node_dr is None:
    print('No se encontró ningún nodo que empiece con "Dr".')
else:
    print('Nodo encontrado (valor actual):', node_dr.value)
    # Ejemplo de corrección: cambiamos el nombre al correcto 'Dr Strange'
    old_name = node_dr.value
    other = node_dr.other_values.copy()
    # actualizamos el campo name dentro de other_values
    other['name'] = 'Dr Strange'
    # borramos el nodo viejo y re-insertamos con el nuevo nombre
    deleted_value, deleted_other = mcu_tree.delete(old_name)
    if deleted_value is not None:
        mcu_tree.insert('Dr Strange', other)
        print(f'Nombre corregido: "{old_name}" -> "Dr Strange"')
    else:
        print('No se pudo eliminar el nodo antiguo para corregir el nombre.')

print()

# Verificamos que ahora exista 'Dr Strange'
pos = mcu_tree.search('Dr Strange')
if pos is not None:
    print('Verificación: encontrado ->', pos.value, pos.other_values)
else:
    print('Verificación: Dr Strange NO encontrado.')
print()

# ---------- f) listar los superhéroes ordenados de manera descendente (Z -> A) ----------
print('--- f) Héroes ordenados descendente (Z -> A) ---')
# Queremos sólo héroes y en orden descendente.

def print_heroes_descending(tree: BinaryTree):
    def _desc(root):
        if root is None:
            return
        _desc(root.right)
        if root.other_values.get('is_hero'):
            print(root.value)
        _desc(root.left)
    _desc(tree.root)

print_heroes_descending(mcu_tree)
print()

# ---------- g) generar bosque: un árbol de héroes y otro de villanos ----------
print('--- g) Generar bosque (árbol héroes y árbol villanos) ---')
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

# Usamos la función divide_tree provista en tree.py (espera is_villain en other_values)
mcu_tree.divide_tree(arbol_heroes, arbol_villanos)

# I. determinar cuántos nodos tiene cada árbol
heroes_nodes = count_nodes(arbol_heroes)
villains_nodes = count_nodes(arbol_villanos)
print(f'Nodos en árbol de héroes: {heroes_nodes}')
print(f'Nodos en árbol de villanos: {villains_nodes}\n')

# II. barrido ordenado alfabéticamente de cada árbol
print('Árbol de héroes (A -> Z):')
arbol_heroes.in_order()
print('\nÁrbol de villanos (A -> Z):')
arbol_villanos.in_order()

print('\n--- Fin de la ejecución ---')
