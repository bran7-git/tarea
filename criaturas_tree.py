

from tree import BinaryTree

# ---------------- Datos: tabla de criaturas ----------------
# Nota: en la tabla '-' significa que no hay registro de quien la derrotó (None).
# Los nombres se copian según la imagen provista; si tenés correcciones ortográficas
# las aplico cuando me digas.

creatures_data = [
    # columna izquierda
    ("Ceto", None),
    ("Tifón", "Zeus"),
    ("Equidna", "Argos Panoptes"),
    ("Dino", None),
    ("Pefredo", None),
    ("Enio", None),
    ("Escila", None),
    ("Caribdis", None),
    ("Euríale", None),
    ("Esteno", None),
    ("Medusa", "Perseo"),
    ("Ladón", "Heracles"),
    ("Águila del Cáucaso", None),
    ("Quimera", "Belerofonte"),
    ("Hidra de Lerna", "Heracles"),
    ("León de Nemea", "Heracles"),
    ("Esfinge", "Edipo"),
    ("Dragón de la Cólquida", None),
    ("Cerbero", None),
    # columna derecha
    ("Cerda de Cromión", "Teseo"),
    ("Ortro", "Heracles"),
    ("Toro de Creta", "Teseo"),
    ("Jabalí de Calidón", "Atalanta"),
    ("Carcinos", None),
    ("Gerión", "Heracles"),
    ("Cloto", None),
    ("Láquesis", None),
    ("Átropos", None),
    ("Minotauro de Creta", "Teseo"),
    ("Harpías", None),
    ("Talos", "Medea"),
    ("Sirenas", None),
    ("Pitón", "Apolo"),
    ("Cierva de Cerinea", None),
    ("Basilisco", None),
    ("Jabalí de Erimanto", None),
]

# ---------------- Construcción del árbol ----------------

tree = BinaryTree()

for name, defeated_by in creatures_data:
    other = {
        'derrotado_por': defeated_by,   # quien lo derrotó (string) o None
        'capturada': None,              # nombre del héroe/dios que la capturó
        'descripcion': ''               # campo para cargar una breve descripción
    }
    tree.insert(name, other)

# ---------------- Funciones auxiliares ----------------

def inorder_with_defeated(t: BinaryTree):
    """a) listado inorden de las criaturas y quienes la derrotaron."""
    def _in(root):
        if root is None:
            return
        _in(root.left)
        defeated = root.other_values.get('derrotado_por')
        print(f"{root.value} -> {defeated if defeated is not None else '-'}")
        _in(root.right)
    _in(t.root)


def set_description(t: BinaryTree, name: str, description: str):
    """b) cargar una breve descripción sobre la criatura."""
    node = t.search(name)
    if node is not None:
        node.other_values['descripcion'] = description
        return True
    return False


def show_creature_info(t: BinaryTree, name: str):
    """c) mostrar toda la información de la criatura (si existe)."""
    node = t.search(name)
    if node is None:
        print(f"{name} no encontrada en el árbol.")
    else:
        print(f"Nombre: {node.value}\nDatos: {node.other_values}")


def top_defeaters(t: BinaryTree, top_n=3):
    """d) determinar los n héroes/dioses que derrotaron mayor cantidad de criaturas."""
    counts = {}
    def _count(root):
        if root is None:
            return
        d = root.other_values.get('derrotado_por')
        if d is not None:
            counts[d] = counts.get(d, 0) + 1
        _count(root.left)
        _count(root.right)
    _count(t.root)
    # ordenar por cantidad descendente
    sorted_list = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_list[:top_n]


def creatures_defeated_by(t: BinaryTree, hero_name: str):
    """e) listar las criaturas derrotadas por un héroe (ej: Heracles)."""
    found = []
    def _in(root):
        if root is None:
            return
        _in(root.left)
        if root.other_values.get('derrotado_por') == hero_name:
            found.append(root.value)
        _in(root.right)
    _in(t.root)
    return found


def creatures_not_defeated(t: BinaryTree):
    """f) listar las criaturas que no han sido derrotadas (derrotado_por is None)."""
    res = []
    def _in(root):
        if root is None:
            return
        _in(root.left)
        if root.other_values.get('derrotado_por') is None:
            res.append(root.value)
        _in(root.right)
    _in(t.root)
    return res


def set_captured(t: BinaryTree, name: str, captor: str):
    """g/h) asignar el campo 'capturada' al nodo con nombre 'name'."""
    node = t.search(name)
    if node is not None:
        node.other_values['capturada'] = captor
        return True
    return False


def search_by_substring(t: BinaryTree, substring: str):
    """i) búsquedas por coincidencia (subcadena en el nombre)."""
    matches = []
    sub = substring.lower()
    def _tr(root):
        if root is None:
            return
        _tr(root.left)
        if sub in str(root.value).lower():
            matches.append(root.value)
        _tr(root.right)
    _tr(t.root)
    return matches


def delete_creature(t: BinaryTree, name: str):
    """j) eliminar un nodo por nombre."""
    deleted_value, deleted_other = t.delete(name)
    return deleted_value is not None


def modify_defeated(t: BinaryTree, name: str, new_defeated: str):
    """k) modificar el campo 'derrotado_por' de la criatura indicada."""
    node = t.search(name)
    if node is not None:
        node.other_values['derrotado_por'] = new_defeated
        return True
    return False


def rename_creature(t: BinaryTree, old_name: str, new_name: str):
    """l) modificar el nombre de una criatura (eliminar e insertar con nuevo nombre)."""
    deleted_value, deleted_other = t.delete(old_name)
    if deleted_value is not None:
        # actualizamos el campo de nombre si existe
        deleted_other['name'] = new_name
        t.insert(new_name, deleted_other)
        return True
    return False


def level_order_listing(t: BinaryTree):
    """m) listado por nivel (barrido por niveles)."""
    # Implementamos con una cola simple en Python para mostrar nombre + derrotador
    q = []
    if t.root is None:
        return
    q.append(t.root)
    while q:
        node = q.pop(0)
        defeated = node.other_values.get('derrotado_por')
        print(f"{node.value} -> {defeated if defeated is not None else '-'}")
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)


def creatures_captured_by(t: BinaryTree, captor_name: str):
    """n) mostrar las criaturas capturadas por un héroe concreto."""
    res = []
    def _tr(root):
        if root is None:
            return
        _tr(root.left)
        if root.other_values.get('capturada') == captor_name:
            res.append(root.value)
        _tr(root.right)
    _tr(t.root)
    return res

# ---------------- Ejecución de las consignas (a -> n) ----------------

print('\n=== a) Listado inorden de criaturas y quienes las derrotaron ===')
inorder_with_defeated(tree)

print('\n=== b) Cargar descripciones (ejemplos) ===')
set_description(tree, 'Medusa', 'Monstruo con serpientes en la cabeza; quien mire se convierte en piedra.')
set_description(tree, 'León de Nemea', 'León invulnerable derrotado por Heracles en el primer trabajo.')
show_creature_info(tree, 'Medusa')
show_creature_info(tree, 'León de Nemea')

print('\n=== c) Mostrar toda la información de Talos ===')
show_creature_info(tree, 'Talos')

print('\n=== d) Top 3 héroes/dioses que derrotaron mayor cantidad de criaturas ===')
top3 = top_defeaters(tree, 3)
for person, cnt in top3:
    print(f"{person} -> {cnt}")

print('\n=== e) Criaturas derrotadas por Heracles ===')
heracles_defeated = creatures_defeated_by(tree, 'Heracles')
for c in heracles_defeated:
    print(c)

print('\n=== f) Criaturas que no han sido derrotadas ===')
not_defeated = creatures_not_defeated(tree)
for c in not_defeated:
    print(c)

print('\n=== g) Campo "capturada" agregado (inicialmente None) y h) marcar capturas por Heracles ===')
# h) Modificar nodos: Cerbero, Toro de Creta, Cierva de Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó
for cname in ['Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabalí de Erimanto']:
    ok = set_captured(tree, cname, 'Heracles')
    print(f"Asignar captura {cname}: {'OK' if ok else 'NO ENCONTRADO'}")

print('\n=== i) Búsqueda por coincidencia (ej: buscar "cer") ===')
matches = search_by_substring(tree, 'cer')
for m in matches:
    print(m)

print('\n=== j) Eliminar Basilisco y Sirenas ===')
for name in ['Basilisco', 'Sirenas']:
    ok = delete_creature(tree, name)
    print(f"Eliminar {name}: {'ELIMINADO' if ok else 'NO ENCONTRADO'}")

print('\n=== k) Modificar Aves del Estínfalo agregando que Heracles derroto a varias ===')
# Buscar Aves del Estínfalo: en la tabla aparece como 'Aves del Estínfalo'.
modify_defeated(tree, 'Aves del Estínfalo', 'Heracles (varias)')
show_creature_info(tree, 'Aves del Estínfalo')

print('\n=== l) Cambiar nombre Ladón por Dragón Ladón ===')
ren_ok = rename_creature(tree, 'Ladón', 'Dragón Ladón')
print('Renombrado Ladón -> Dragón Ladón:', 'OK' if ren_ok else 'NO ENCONTRADO')

print('\n=== m) Listado por nivel del árbol ===')
level_order_listing(tree)

print('\n=== n) Criaturas capturadas por Heracles ===')
captured_by_heracles = creatures_captured_by(tree, 'Heracles')
for c in captured_by_heracles:
    print(c)

print('\n--- Fin de ejecucion ---')
