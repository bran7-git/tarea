from typing import Any, Optional


class Queue:
    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None:
        self.__elements.append(value)

    def attention(self) -> Optional[Any]:
        return self.__elements.pop(0) if self.__elements else None

    def size(self) -> int:
        return len(self.__elements)
    
    def on_front(self) -> Optional[Any]:
        return self.__elements[0] if self.__elements else None

    def move_to_end(self) -> Optional[Any]:
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value

    def show(self):
        for i in range(len(self.__elements)):
            print(self.move_to_end())

# Cargar datos a la cola
personajes = [
    {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
    {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"personaje": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"},
    {"personaje": "Shuri", "superheroe": "Black Panther", "genero": "F"},
]

cola_personajes = Queue()
for p in personajes:
    cola_personajes.arrive(p)

# a) Determinar el nombre del personaje de la superhéroe Capitana Marvel
def buscar_personaje_por_superheroe(cola: Queue, nombre_heroe: str):
    for _ in range(cola.size()):
        p = cola.on_front()
        if p["superheroe"] == nombre_heroe:
            print(f"El personaje de {nombre_heroe} es {p['personaje']}")
        cola.move_to_end()

# b) Mostrar los nombres de los superhéroes femeninos
def mostrar_heroes_femeninos(cola: Queue):
    print("Superhéroes femeninos:")
    for _ in range(cola.size()):
        p = cola.on_front()
        if p["genero"] == "F":
            print("-", p["superheroe"])
        cola.move_to_end()

# c) Mostrar los nombres de los personajes masculinos
def mostrar_personajes_masculinos(cola: Queue):
    print("Personajes masculinos:")
    for _ in range(cola.size()):
        p = cola.on_front()
        if p["genero"] == "M":
            print("-", p["personaje"])
        cola.move_to_end()

# d) Determinar el nombre del superhéroe del personaje Scott Lang
def buscar_heroe_por_personaje(cola: Queue, nombre_personaje: str):
    for _ in range(cola.size()):
        p = cola.on_front()
        if p["personaje"] == nombre_personaje:
            print(f"El superhéroe de {nombre_personaje} es {p['superheroe']}")
        cola.move_to_end()

# e) Mostrar todos los datos de los personajes o superhéroes que comienzan con 'S'
def mostrar_datos_letra_s(cola: Queue):
    print("Personajes o superhéroes que comienzan con 'S':")
    for _ in range(cola.size()):
        p = cola.on_front()
        if p["personaje"].startswith("S") or p["superheroe"].startswith("S"):
            print("-", p)
        cola.move_to_end()

# f) Determinar si Carol Danvers está en la cola e indicar su nombre de superhéroe
def buscar_carol_danvers(cola: Queue):
    for _ in range(cola.size()):
        p = cola.on_front()
        if p["personaje"] == "Carol Danvers":
            print("Carol Danvers está en la cola. Su superhéroe es", p["superheroe"])
        cola.move_to_end()

# Ejecutar todas las funciones
print("--- a) ---")
buscar_personaje_por_superheroe(cola_personajes, "Capitana Marvel")

print("\n--- b) ---")
mostrar_heroes_femeninos(cola_personajes)

print("\n--- c) ---")
mostrar_personajes_masculinos(cola_personajes)

print("\n--- d) ---")
buscar_heroe_por_personaje(cola_personajes, "Scott Lang")

print("\n--- e) ---")
mostrar_datos_letra_s(cola_personajes)

print("\n--- f) ---")
buscar_carol_danvers(cola_personajes)


