
# Lista simple de superhéroes
superheroes = [
    "Iron Man",
    "Hulk",
    "Thor",
    "Spiderman",
    "Black Widow",
    "Doctor Strange",
    "Wolverine",
    "Ant Man",
    "Black Panther",
    "Vision",
    "Scarlet Witch",
    "Falcon",
    "Hawkeye",
    "Captain Marvel",
    "Capitan America"  
]


def buscar_superheroe(lista, nombre, pos=0):
    if pos >= len(lista):
        return False
    elif lista[pos] == nombre:
        return True
    else:
        return buscar_superheroe(lista, nombre, pos + 1)


def listar_superheroes(lista, pos=0):
    if pos >= len(lista):
        return
    print(lista[pos])
    listar_superheroes(lista, pos + 1)


print("\n--- Buscar 'Capitan America' ---")
if buscar_superheroe(superheroes, "Capitan America"):
    print("Capitan America está en la lista.")
else:
    print("Capitan America NO está en la lista.")

print("\n--- Listado de superhéroes ---")
listar_superheroes(superheroes)
