from stack import Stack

# Datos iniciales de los trajes de Iron Man
ironman_stack = Stack()

# Cada traje es un diccionario con modelo, pelicula, estado
trajes = [
    {"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Impecable"},
    {"modelo": "Mark V", "pelicula": "Iron Man 2", "estado": "Dañado"},
    {"modelo": "Mark XLII", "pelicula": "Iron Man 3", "estado": "Destruido"},
    {"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Dañado"},
    {"modelo": "Mark L", "pelicula": "Avengers: Infinity War", "estado": "Impecable"},
    {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Destruido"},
    {"modelo": "Mark XLVI", "pelicula": "Captain America: Civil War", "estado": "Dañado"},
    {"modelo": "Mark XLVII", "pelicula": "Spider-Man: Homecoming", "estado": "Impecable"},
    {"modelo": "Mark XLIV", "pelicula": "Avengers: Endgame", "estado": "Destruido"},
]

for traje in trajes:
    ironman_stack.push(traje)

print("--- a) Verificar si se usó Mark XLIV ---")
aux_stack = Stack()

peliculas_xliv = set()
while ironman_stack.size() > 0:
    traje = ironman_stack.pop()
    if traje["modelo"] == "Mark XLIV":
        peliculas_xliv.add(traje["pelicula"])
    aux_stack.push(traje)

# Restaurar la pila original
while aux_stack.size() > 0:
    ironman_stack.push(aux_stack.pop())

if peliculas_xliv:
    print("Mark XLIV fue utilizado en:", ", ".join(peliculas_xliv))
else:
    print("Mark XLIV no fue utilizado.")

print("\n--- b) Mostrar modelos DAÑADOS ---")
aux_stack = Stack()
while ironman_stack.size() > 0:
    traje = ironman_stack.pop()
    if traje["estado"] == "Dañado":
        print(traje)
    aux_stack.push(traje)
while aux_stack.size() > 0:
    ironman_stack.push(aux_stack.pop())

print("\n--- c) Eliminar modelos DESTRUIDOS ---")
aux_stack = Stack()
while ironman_stack.size() > 0:
    traje = ironman_stack.pop()
    if traje["estado"] == "Destruido":
        print("Eliminado:", traje)
    else:
        aux_stack.push(traje)
while aux_stack.size() > 0:
    ironman_stack.push(aux_stack.pop())

print("\n--- d) Agregar Mark LXXXV si no está repetido en la misma película ---")
nuevo_traje = {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Impecable"}
existe = False
aux_stack = Stack()
while ironman_stack.size() > 0:
    traje = ironman_stack.pop()
    if traje["modelo"] == nuevo_traje["modelo"] and traje["pelicula"] == nuevo_traje["pelicula"]:
        existe = True
    aux_stack.push(traje)
while aux_stack.size() > 0:
    ironman_stack.push(aux_stack.pop())
if not existe:
    ironman_stack.push(nuevo_traje)
    print("Se agregó:", nuevo_traje)
else:
    print("Ya existe el traje Mark LXXXV en Avengers: Endgame")

print("\n--- e) Trajes en Spider-Man: Homecoming y Captain America: Civil War ---")
aux_stack = Stack()
while ironman_stack.size() > 0:
    traje = ironman_stack.pop()
    if traje["pelicula"] in ["Spider-Man: Homecoming", "Captain America: Civil War"]:
        print(traje["modelo"], "-", traje["pelicula"])
    aux_stack.push(traje)
while aux_stack.size() > 0:
    ironman_stack.push(aux_stack.pop())
