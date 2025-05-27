from queue_ import Queue

# Datos de ejemplo de personajes MCU
personajes = [
    {"nombre": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"nombre": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
    {"nombre": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"nombre": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"nombre": "Peter Parker", "superheroe": "Spider-Man", "genero": "M"},
    {"nombre": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"nombre": "Shuri", "superheroe": "Shuri", "genero": "F"},
    {"nombre": "Gamora", "superheroe": "Gamora", "genero": "F"},
    {"nombre": "Sam Wilson", "superheroe": "Falcon", "genero": "M"},
    {"nombre": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"}
]

cola_personajes = Queue()
for p in personajes:
    cola_personajes.arrive(p)

print("--- a) Nombre del personaje de Capitana Marvel ---")
aux = Queue()
while cola_personajes.size() > 0:
    personaje = cola_personajes.attention()
    if personaje["superheroe"] == "Capitana Marvel":
        print("Personaje:", personaje["nombre"])
    aux.arrive(personaje)
while aux.size() > 0:
    cola_personajes.arrive(aux.attention())

print("\n--- b) Superhéroes femeninos ---")
aux = Queue()
while cola_personajes.size() > 0:
    personaje = cola_personajes.attention()
    if personaje["genero"] == "F":
        print(personaje["superheroe"])
    aux.arrive(personaje)
while aux.size() > 0:
    cola_personajes.arrive(aux.attention())

print("\n--- c) Personajes masculinos ---")
aux = Queue()
while cola_personajes.size() > 0:
    personaje = cola_personajes.attention()
    if personaje["genero"] == "M":
        print(personaje["nombre"])
    aux.arrive(personaje)
while aux.size() > 0:
    cola_personajes.arrive(aux.attention())

print("\n--- d) Superhéroe de Scott Lang ---")
aux = Queue()
while cola_personajes.size() > 0:
    personaje = cola_personajes.attention()
    if personaje["nombre"] == "Scott Lang":
        print("Superhéroe:", personaje["superheroe"])
    aux.arrive(personaje)
while aux.size() > 0:
    cola_personajes.arrive(aux.attention())

print("\n--- e) Datos de nombres que empiezan con S ---")
aux = Queue()
while cola_personajes.size() > 0:
    personaje = cola_personajes.attention()
    if personaje["nombre"].startswith("S") or personaje["superheroe"].startswith("S"):
        print(personaje)
    aux.arrive(personaje)
while aux.size() > 0:
    cola_personajes.arrive(aux.attention())

print("\n--- f) Verificar si Carol Danvers está en la cola ---")
aux = Queue()
encontrado = False
while cola_personajes.size() > 0:
    personaje = cola_personajes.attention()
    if personaje["nombre"] == "Carol Danvers":
        print("Carol Danvers está en la cola. Superhéroe:", personaje["superheroe"])
        encontrado = True
    aux.arrive(personaje)
while aux.size() > 0:
    cola_personajes.arrive(aux.attention())
if not encontrado:
    print("Carol Danvers no está en la cola.")

print("\n--- f) ---")
buscar_carol_danvers(cola_personajes)


