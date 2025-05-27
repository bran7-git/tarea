from typing import Any, Optional


class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        return self.__elements.pop() if self.__elements else None

    def size(self) -> int:
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        return self.__elements[-1] if self.__elements else None

    def show(self):
        aux_stack = Stack()
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())


class Queue:
    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None:
        self.__elements.append(value)

    def attention(self) -> Optional[Any]:
        return self.__elements.pop(0) if self.__elements else None

    def on_front(self) -> Optional[Any]:
        return self.__elements[0] if self.__elements else None

    def move_to_end(self) -> None:
        if self.size() > 0:
            self.arrive(self.attention())

    def size(self) -> int:
        return len(self.__elements)

    def show(self):
        for value in self.__elements:
            print(value)

# Cola con personajes del MCU
personajes_mcu = [
    {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
    {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"personaje": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"},
    {"personaje": "Shuri", "superheroe": "Black Panther", "genero": "F"},
]

cola_personajes = Queue()
for p in personajes_mcu:
    cola_personajes.arrive(p)

# A) Nombre del personaje de Capitana Marvel
def personaje_de_capitana_marvel(cola: Queue):
    for _ in range(cola.size()):
        dato = cola.on_front()
        if dato["superheroe"] == "Capitana Marvel":
            print("a) Personaje de Capitana Marvel:", dato["personaje"])
        cola.move_to_end()

# B) Superhéroes femeninos
def superheroinas(cola: Queue):
    print("b) Superhéroes femeninos:")
    for _ in range(cola.size()):
        dato = cola.on_front()
        if dato["genero"] == "F":
            print("-", dato["superheroe"])
        cola.move_to_end()

# C) Personajes masculinos
def personajes_masculinos(cola: Queue):
    print("c) Personajes masculinos:")
    for _ in range(cola.size()):
        dato = cola.on_front()
        if dato["genero"] == "M":
            print("-", dato["personaje"])
        cola.move_to_end()

# D) Superhéroe de Scott Lang
def superheroe_de_scott_lang(cola: Queue):
    for _ in range(cola.size()):
        dato = cola.on_front()
        if dato["personaje"] == "Scott Lang":
            print("d) Superhéroe de Scott Lang:", dato["superheroe"])
        cola.move_to_end()

# E) Datos de los que empiezan con 'S'
def nombres_con_s(cola: Queue):
    print("e) Datos de personajes o superhéroes que comienzan con 'S':")
    for _ in range(cola.size()):
        dato = cola.on_front()
        if dato["personaje"].startswith("S") or dato["superheroe"].startswith("S"):
            print("-", dato)
        cola.move_to_end()

# F) Si está Carol Danvers, mostrar su superhéroe
def buscar_carol_danvers(cola: Queue):
    encontrado = False
    for _ in range(cola.size()):
        dato = cola.on_front()
        if dato["personaje"] == "Carol Danvers":
            encontrado = True
            print("f) Carol Danvers se encuentra en la cola. Superhéroe:", dato["superheroe"])
        cola.move_to_end()
    if not encontrado:
        print("f) Carol Danvers no se encuentra en la cola.")

# Ejecutar todas
personaje_de_capitana_marvel(cola_personajes)
superheroinas(cola_personajes)
personajes_masculinos(cola_personajes)
superheroe_de_scott_lang(cola_personajes)
nombres_con_s(cola_personajes)
buscar_carol_danvers(cola_personajes)

