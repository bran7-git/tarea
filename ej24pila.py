
from stack import Stack

# Datos iniciales de los personajes MCU
personajes_stack = Stack()

# Cada personaje es un diccionario con nombre y cantidad de peliculas
personajes = [
    {"nombre": "Iron Man", "peliculas": 10},
    {"nombre": "Captain America", "peliculas": 9},
    {"nombre": "Thor", "peliculas": 8},
    {"nombre": "Rocket Raccoon", "peliculas": 6},
    {"nombre": "Groot", "peliculas": 5},
    {"nombre": "Black Widow", "peliculas": 7},
    {"nombre": "Doctor Strange", "peliculas": 4},
    {"nombre": "Gamora", "peliculas": 4},
    {"nombre": "Drax", "peliculas": 4},
    {"nombre": "Captain Marvel", "peliculas": 3},
    {"nombre": "Hawkeye", "peliculas": 5},
]

for personaje in personajes:
    personajes_stack.push(personaje)

print("--- a) Posición de Rocket Raccoon y Groot ---")
posiciones = {}
aux_stack = Stack()
posicion_actual = 1
while personajes_stack.size() > 0:
    personaje = personajes_stack.pop()
    if personaje["nombre"] in ["Rocket Raccoon", "Groot"]:
        posiciones[personaje["nombre"]] = posicion_actual
    aux_stack.push(personaje)
    posicion_actual += 1
while aux_stack.size() > 0:
    personajes_stack.push(aux_stack.pop())

for nombre in ["Rocket Raccoon", "Groot"]:
    if nombre in posiciones:
        print(f"{nombre} está en la posición {posiciones[nombre]} desde la cima.")
    else:
        print(f"{nombre} no está en la pila.")

print("\n--- b) Personajes que participaron en más de 5 películas ---")
aux_stack = Stack()
while personajes_stack.size() > 0:
    personaje = personajes_stack.pop()
    if personaje["peliculas"] > 5:
        print(f"{personaje['nombre']}: {personaje['peliculas']} películas")
    aux_stack.push(personaje)
while aux_stack.size() > 0:
    personajes_stack.push(aux_stack.pop())

print("\n--- c) Películas en que participó Black Widow ---")
aux_stack = Stack()
while personajes_stack.size() > 0:
    personaje = personajes_stack.pop()
    if personaje["nombre"] == "Black Widow":
        print(f"Black Widow participó en {personaje['peliculas']} películas")
    aux_stack.push(personaje)
while aux_stack.size() > 0:
    personajes_stack.push(aux_stack.pop())

print("\n--- d) Personajes cuyos nombres empiezan con C, D o G ---")
aux_stack = Stack()
while personajes_stack.size() > 0:
    personaje = personajes_stack.pop()
    if personaje["nombre"].startswith(("C", "D", "G")):
        print(personaje["nombre"])
    aux_stack.push(personaje)
while aux_stack.size() > 0:
    personajes_stack.push(aux_stack.pop())

print("\nd) Personajes que empiezan con C, D o G:")
for nombre in nombres_con_cdg(pila_personajes):
    print(f"- {nombre}")

