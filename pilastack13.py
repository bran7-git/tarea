from stack import Stack

personajes = [
    {"nombre": "Iron Man", "peliculas": 10},
    {"nombre": "Captain America", "peliculas": 9},
    {"nombre": "Thor", "peliculas": 8},
    {"nombre": "Hulk", "peliculas": 7},
    {"nombre": "Black Widow", "peliculas": 7},
    {"nombre": "Hawkeye", "peliculas": 6},
    {"nombre": "Rocket Raccoon", "peliculas": 5},
    {"nombre": "Groot", "peliculas": 4},
    {"nombre": "Doctor Strange", "peliculas": 5},
    {"nombre": "Captain Marvel", "peliculas": 3},
]

pila_personajes = Stack()
for p in personajes:
    pila_personajes.push(p)

def posicion_personajes(pila, nombres):
    aux = Stack()
    posiciones = {}
    posicion = 1
    while pila.size():
        personaje = pila.pop()
        if personaje["nombre"] in nombres and personaje["nombre"] not in posiciones:
            posiciones[personaje["nombre"]] = posicion
        aux.push(personaje)
        posicion += 1
    while aux.size():
        pila.push(aux.pop())
    return posiciones

def personajes_mas_de_5(pila):
    aux = Stack()
    resultado = []
    while pila.size():
        personaje = pila.pop()
        if personaje["peliculas"] > 5:
            resultado.append({"nombre": personaje["nombre"], "peliculas": personaje["peliculas"]})
        aux.push(personaje)
    while aux.size():
        pila.push(aux.pop())
    return resultado

def peliculas_black_widow(pila):
    aux = Stack()
    cantidad = 0
    while pila.size():
        personaje = pila.pop()
        if personaje["nombre"] == "Black Widow":
            cantidad = personaje["peliculas"]
        aux.push(personaje)
    while aux.size():
        pila.push(aux.pop())
    return cantidad

def personajes_iniciales(pila, letras):
    aux = Stack()
    resultado = []
    while pila.size():
        personaje = pila.pop()
        if personaje["nombre"][0] in letras:
            resultado.append(personaje["nombre"])
        aux.push(personaje)
    while aux.size():
        pila.push(aux.pop())
    return resultado

print("a) Posiciones de Rocket Raccoon y Groot:")
print(posicion_personajes(pila_personajes, ["Rocket Raccoon", "Groot"]))

print("\nb) Personajes con más de 5 películas:")
for p in personajes_mas_de_5(pila_personajes):
    print("-", p)

print("\nc) Películas con Black Widow:", peliculas_black_widow(pila_personajes))

print("\nd) Personajes que empiezan con C, D o G:")
for nombre in personajes_iniciales(pila_personajes, {"C", "D", "G"}):
    print("-",nombre)
