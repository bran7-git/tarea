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

# Datos de trajes
trajes = [
    {"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Dañado"},
    {"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Dañado"},
    {"modelo": "Mark XLV", "pelicula": "Avengers: Age of Ultron", "estado": "Impecable"},
    {"modelo": "Mark XLVI", "pelicula": "Captain America: Civil War", "estado": "Impecable"},
    {"modelo": "Mark XLVII", "pelicula": "Spider-Man: Homecoming", "estado": "Dañado"},
    {"modelo": "Mark L", "pelicula": "Avengers: Infinity War", "estado": "Destruido"},
    {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Destruido"},
]

# Cargar trajes en la pila
pila_trajes = Stack()
for traje in trajes:
    pila_trajes.push(traje)

# a) Buscar Mark XLIV
def buscar_mark_xliv(pila):
    aux = Stack()
    peliculas = []
    while pila.size() > 0:
        traje = pila.pop()
        if traje["modelo"] == "Mark XLIV":
            peliculas.append(traje["pelicula"])
        aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())
    return peliculas

# b) Modelos dañados
def modelos_danados(pila):
    aux = Stack()
    danados = []
    while pila.size() > 0:
        traje = pila.pop()
        if traje["estado"] == "Dañado":
            danados.append(traje)
        aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())
    return danados

# c) Eliminar destruidos
def eliminar_destruidos(pila):
    aux = Stack()
    destruidos = []
    while pila.size() > 0:
        traje = pila.pop()
        if traje["estado"] == "Destruido":
            destruidos.append(traje["modelo"])
        else:
            aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())
    return destruidos

# d) Ya se cumple con la carga inicial

# e) Agregar Mark LXXXV si no está ya en esa película
def agregar_mark_lxxxv(pila):
    nuevo = {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Impecable"}
    aux = Stack()
    existe = False
    while pila.size() > 0:
        traje = pila.pop()
        if traje["modelo"] == nuevo["modelo"] and traje["pelicula"] == nuevo["pelicula"]:
            existe = True
        aux.push(traje)
    if not existe:
        aux.push(nuevo)
    while aux.size() > 0:
        pila.push(aux.pop())
    return not existe

# f) Modelos usados en películas dadas
def modelos_en_peliculas(pila, peliculas_buscadas):
    aux = Stack()
    modelos = []
    while pila.size() > 0:
        traje = pila.pop()
        if traje["pelicula"] in peliculas_buscadas:
            modelos.append(traje["modelo"])
        aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())
    return modelos

# Resultados
print("a) Mark XLIV fue usado en:", buscar_mark_xliv(pila_trajes))

print("\nb) Modelos dañados:")
for d in modelos_danados(pila_trajes):
    print("-", d)

print("\nc) Modelos destruidos eliminados:")
for m in eliminar_destruidos(pila_trajes):
    print("-", m)

print("\nd) Agregar Mark LXXXV si no estaba:", agregar_mark_lxxxv(pila_trajes))

print("\ne) Modelos usados en Spider-Man: Homecoming y Captain America: Civil War:")
for modelo in modelos_en_peliculas(pila_trajes, ["Spider-Man: Homecoming", "Captain America: Civil War"]):
    print("-", modelo)

