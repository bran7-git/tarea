from queue import Queue

# Estructura para representar un personaje del MCU
def crear_personaje(nombre_personaje, nombre_superheroe, genero):
    return {
        "personaje": nombre_personaje,
        "superheroe": nombre_superheroe,
        "genero": genero.upper()
    }

# Cargar cola con personajes de ejemplo
def cargar_personajes():
    cola = Queue()
    datos = [
        crear_personaje("Tony Stark", "Iron Man", "M"),
        crear_personaje("Steve Rogers", "Capitán América", "M"),
        crear_personaje("Natasha Romanoff", "Black Widow", "F"),
        crear_personaje("Carol Danvers", "Capitana Marvel", "F"),
        crear_personaje("Wanda Maximoff", "Scarlet Witch", "F"),
        crear_personaje("Scott Lang", "Ant-Man", "M"),
        crear_personaje("Stephen Strange", "Doctor Strange", "M"),
        crear_personaje("Sam Wilson", "Falcon", "M"),
        crear_personaje("Shuri", "Black Panther", "F"),
    ]
    for p in datos:
        cola.put(p)
    return cola

# a. Determinar el nombre del personaje de Capitana Marvel
def buscar_personaje_por_superheroe(cola, nombre_superheroe):
    aux = Queue()
    encontrado = False
    while not cola.empty():
        p = cola.get()
        if p['superheroe'].lower() == nombre_superheroe.lower():
            print(f"a) El personaje de {nombre_superheroe} es: {p['personaje']}")
            encontrado = True
        aux.put(p)
    while not aux.empty():
        cola.put(aux.get())
    if not encontrado:
        print(f"a) No se encontró el superhéroe {nombre_superheroe}.")

# b. Mostrar superhéroes femeninos
def mostrar_superheroinas(cola):
    print("b) Superhéroes femeninos:")
    aux = Queue()
    while not cola.empty():
        p = cola.get()
        if p['genero'] == 'F':
            print(f"- {p['superheroe']}")
        aux.put(p)
    while not aux.empty():
        cola.put(aux.get())

# c. Mostrar personajes masculinos
def mostrar_personajes_masculinos(cola):
    print("c) Personajes masculinos:")
    aux = Queue()
    while not cola.empty():
        p = cola.get()
        if p['genero'] == 'M':
            print(f"- {p['personaje']}")
        aux.put(p)
    while not aux.empty():
        cola.put(aux.get())

# d. Determinar el superhéroe de Scott Lang
def buscar_superheroe_por_personaje(cola, nombre_personaje):
    aux = Queue()
    encontrado = False
    while not cola.empty():
        p = cola.get()
        if p['personaje'].lower() == nombre_personaje.lower():
            print(f"d) El superhéroe de {nombre_personaje} es: {p['superheroe']}")
            encontrado = True
        aux.put(p)
    while not aux.empty():
        cola.put(aux.get())
    if not encontrado:
        print(f"d) No se encontró el personaje {nombre_personaje}.")

# e. Mostrar datos cuyos nombres comienzan con S (personaje o superhéroe)
def mostrar_nombres_con_s(cola):
    print("e) Datos con nombres que comienzan con 'S':")
    aux = Queue()
    while not cola.empty():
        p = cola.get()
        if p['personaje'].startswith('S') or p['superheroe'].startswith('S'):
            print(f"- Personaje: {p['personaje']}, Superhéroe: {p['superheroe']}, Género: {p['genero']}")
        aux.put(p)
    while not aux.empty():
        cola.put(aux.get())

# f. Verificar si Carol Danvers está y mostrar su superhéroe
def verificar_carol_danvers(cola):
    aux = Queue()
    encontrado = False
    while not cola.empty():
        p = cola.get()
        if p['personaje'].lower() == "carol danvers":
            print(f"f) Carol Danvers está en la cola y su superhéroe es: {p['superheroe']}")
            encontrado = True
        aux.put(p)
    while not aux.empty():
        cola.put(aux.get())
    if not encontrado:
        print("f) Carol Danvers no se encuentra en la cola.")

# Programa principal
if __name__ == "__main__":
    cola = cargar_personajes()
    
    buscar_personaje_por_superheroe(cola, "Capitana Marvel")
    print()
    mostrar_superheroinas(cola)
    print()
    mostrar_personajes_masculinos(cola)
    print()
    buscar_superheroe_por_personaje(cola, "Scott Lang")
    print()
    mostrar_nombres_con_s(cola)
    print()
    verificar_carol_danvers(cola)
