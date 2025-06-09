from list_ import List
from queue_ import Queue
from super_heroes_data import superheroes


def order_by_name(item):
    return item.name

def order_by_real_name(item):
    return item.real_name or ""

def order_by_year(item):
    return item.first_appearance


class Superhero:
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        return self.name

 
list_superheroes = List()
list_superheroes.add_criterion('name', order_by_name)
list_superheroes.add_criterion('real_name', order_by_real_name)
list_superheroes.add_criterion('year', order_by_year)

for s in superheroes:
    hero = Superhero(
        name=s["name"],
        alias=s["alias"],
        real_name=s["real_name"],
        short_bio=s["short_bio"],
        first_appearance=s["first_appearance"],
        is_villain=s["is_villain"]
    )
    list_superheroes.append(hero)

# a) Listado ordenado por nombre ascendente
print("\n--- a) Ordenados por nombre (solo nombre) ---")
list_superheroes.sort_by_criterion("name")
for hero in list_superheroes:
    print(hero.name)

# b) Posicion de The Thing y Rocket Raccoon
print("\n--- b) Posición de The Thing y Rocket Raccoon ---")
pos_thing = list_superheroes.search("The Thing", "name")
pos_rocket = list_superheroes.search("Rocket Raccoon", "name")
print("The Thing está en la posición:", pos_thing)
print("Rocket Raccoon está en la posición:", pos_rocket)

# c) Listar villanos
print("\n--- c) Villanos ---")
for hero in list_superheroes:
    if hero.is_villain:
        print(hero.name)

# d) Cola de villanos para filtrar los que aparecieron antes de 1980
print("\n--- d) Villanos antes de 1980 ---")
villanos_queue = Queue()
for hero in list_superheroes:
    if hero.is_villain:
        villanos_queue.arrive(hero)

print("Villanos con primera aparición antes de 1980:")
for _ in range(villanos_queue.size()):
    personaje = villanos_queue.attention()
    if personaje.first_appearance < 1980:
        print(personaje.name, "-", personaje.first_appearance)
    villanos_queue.arrive(personaje)

# e) Superhéroes que comienzan con Bl, G, My, W
print("\n--- e) Superhéroes que comienzan con Bl, G, My, W ---")
for hero in list_superheroes:
    if hero.name.startswith(("Bl", "G", "My", "W")):
        print(hero.name)

# f) Ordenar por nombre real
print("\n--- f) Ordenados por nombre real ---")
list_superheroes.sort_by_criterion("real_name")
for hero in list_superheroes:
    print(hero.real_name)

# g) Ordenados por año de aparición
print("\n--- g) Ordenados por fecha de aparición ---")
list_superheroes.sort_by_criterion("year")
for hero in list_superheroes:
    print(hero.name, "-", hero.first_appearance)

# h) Modificar nombre real de Ant Man
print("\n--- h) Modificar nombre real de Ant Man ---")
pos_antman = list_superheroes.search("Ant Man", "name")
if pos_antman is not None:
    list_superheroes[pos_antman].real_name = "Scott Lang"
    print("Nombre real actualizado:", list_superheroes[pos_antman].real_name)
else:
    print("Ant Man no encontrado.")

# i) Mostrar biografías que incluyan 'time-traveling' o 'suit'
print("\n--- i) Biografías con 'time-traveling' o 'suit' ---")
for hero in list_superheroes:
    bio = hero.short_bio.lower()
    if "time-traveling" in bio or "suit" in bio:
        print(hero.name)

# j) Eliminar a Electro y Baron Zemo
print("\n--- j) Eliminar Electro y Baron Zemo ---")
eliminados = []
for nombre in ["Electro", "Baron Zemo"]:
    eliminado = list_superheroes.delete_value(nombre, "name")
    if eliminado:
        eliminados.append(eliminado)

if eliminados:
    for e in eliminados:
        print("Eliminado:", e.name)
else:
    print("Ninguno de los personajes fue encontrado para eliminar.")
