
from typing import Any, Optional

class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        return (
            self.__elements.pop()
            if self.__elements
            else None
        )

    def size(self) -> int:
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        return (
            self.__elements[-1]
            if self.__elements
            else None
        )

    def show(self):
        aux_stack = Stack()
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())

# Datos de personajes
personajes = [
    {"nombre": "Tony Stark", "peliculas": 10},
    {"nombre": "Steve Rogers", "peliculas": 9},
    {"nombre": "Natasha Romanoff", "peliculas": 7},
    {"nombre": "Bruce Banner", "peliculas": 8},
    {"nombre": "Thor", "peliculas": 9},
    {"nombre": "Rocket Raccoon", "peliculas": 5},
    {"nombre": "Groot", "peliculas": 4},
    {"nombre": "Clint Barton", "peliculas": 6},
    {"nombre": "Carol Danvers", "peliculas": 3},
    {"nombre": "Doctor Strange", "peliculas": 4},
    {"nombre": "Gamora", "peliculas": 5}
]

# Cargar personajes a la pila
pila_personajes = Stack()
for personaje in personajes:
    pila_personajes.push(personaje)

# a) Posición de Rocket Raccoon y Groot
def buscar_posiciones(pila):
    aux = Stack()
    pos = 1
    posiciones = {}
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje["nombre"] == "Rocket Raccoon":
            posiciones["Rocket Raccoon"] = pos
        elif personaje["nombre"] == "Groot":
            posiciones["Groot"] = pos
        aux.push(personaje)
        pos += 1
    while aux.size() > 0:
        pila.push(aux.pop())
    return posiciones

# b) Personajes con más de 5 películas
def mas_de_5_peliculas(pila):
    aux = Stack()
    resultado = []
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje["peliculas"] > 5:
            resultado.append(personaje)
        aux.push(personaje)
    while aux.size() > 0:
        pila.push(aux.pop())
    return resultado

# c) Cantidad de películas de Black Widow
def peliculas_black_widow(pila):
    aux = Stack()
    cantidad = 0
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje["nombre"] == "Natasha Romanoff":
            cantidad = personaje["peliculas"]
        aux.push(personaje)
    while aux.size() > 0:
        pila.push(aux.pop())
    return cantidad

# d) Personajes que empiezan con C, D o G
def nombres_con_cdg(pila):
    aux = Stack()
    lista = []
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje["nombre"][0] in ["C", "D", "G"]:
            lista.append(personaje["nombre"])
        aux.push(personaje)
    while aux.size() > 0:
        pila.push(aux.pop())
    return lista

# Resultados
print("a) Posiciones desde la cima:")
posiciones = buscar_posiciones(pila_personajes)
for nombre in ["Rocket Raccoon", "Groot"]:
    print(f"- {nombre}: posición {posiciones.get(nombre, 'No encontrado')}")

print("\nb) Personajes con más de 5 películas:")
for p in mas_de_5_peliculas(pila_personajes):
    print(f"- {p['nombre']} ({p['peliculas']} películas)")

print("\nc) Cantidad de películas de Black Widow:")
print(f"- {peliculas_black_widow(pila_personajes)}")

print("\nd) Personajes que empiezan con C, D o G:")
for nombre in nombres_con_cdg(pila_personajes):
    print(f"- {nombre}")

