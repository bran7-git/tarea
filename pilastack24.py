
from stack import Stack

trajes = [
    {"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Dañado"},
    {"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Dañado"},
    {"modelo": "Mark XLV", "pelicula": "Avengers: Age of Ultron", "estado": "Impecable"},
    {"modelo": "Mark XLVI", "pelicula": "Captain America: Civil War", "estado": "Impecable"},
    {"modelo": "Mark XLVII", "pelicula": "Spider-Man: Homecoming", "estado": "Dañado"},
    {"modelo": "Mark L", "pelicula": "Avengers: Infinity War", "estado": "Destruido"},
    {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Destruido"},
]

pila_trajes = Stack()
for traje in trajes:
    pila_trajes.push(traje)

def buscar_mark_xliv(pila):
    aux = Stack()
    peliculas = []
    while pila.size():
        traje = pila.pop()
        if traje["modelo"] == "Mark XLIV":
            peliculas.append(traje["pelicula"])
        aux.push(traje)
    while aux.size():
        pila.push(aux.pop())
    return peliculas

def modelos_danados(pila):
    aux = Stack()
    danados = []
    while pila.size():
        traje = pila.pop()
        if traje["estado"] == "Dañado":
            danados.append(traje)
        aux.push(traje)
    while aux.size():
        pila.push(aux.pop())
    return danados

def eliminar_destruidos(pila):
    aux = Stack()
    destruidos = []
    while pila.size():
        traje = pila.pop()
        if traje["estado"] == "Destruido":
            destruidos.append(traje["modelo"])
        else:
            aux.push(traje)
    while aux.size():
        pila.push(aux.pop())
    return destruidos

def agregar_mark_lxxxv(pila):
    nuevo = {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Impecable"}
    aux = Stack()
    existe = False
    while pila.size():
        traje = pila.pop()
        if traje["modelo"] == nuevo["modelo"] and traje["pelicula"] == nuevo["pelicula"]:
            existe = True
        aux.push(traje)
    if not existe:
        aux.push(nuevo)
    while aux.size():
        pila.push(aux.pop())
    return not existe

def modelos_en_peliculas(pila, pelis):
    aux = Stack()
    modelos = []
    while pila.size():
        traje = pila.pop()
        if traje["pelicula"] in pelis:
            modelos.append(traje["modelo"])
        aux.push(traje)
    while aux.size():
        pila.push(aux.pop())
    return modelos

print("a) Mark XLIV apareció en:", buscar_mark_xliv(pila_trajes))
print("b) Modelos dañados:")
for d in modelos_danados(pila_trajes):
    print("-", d)
print("c) Modelos destruidos eliminados:", eliminar_destruidos(pila_trajes))
print("e) ¿Se agregó Mark LXXXV?:", agregar_mark_lxxxv(pila_trajes))
print("f) Modelos en películas pedidas:", modelos_en_peliculas(pila_trajes, ["Spider-Man: Homecoming", "Captain America: Civil War"]))
