
class Pila:
    def __init__(self):  
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop() if not self.esta_vacia() else None

    def esta_vacia(self):  
        return len(self.items) == 0

    def en_cima(self):
        return self.items[-1] if not self.esta_vacia() else None

    def tamanio(self):
        return len(self.items)

#  PERSONAJES 

def posicion_personaje(pila, nombres):
    aux = Pila()
    pos = 1
    encontrados = {nombre: None for nombre in nombres}
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje["nombre"] in nombres:
            encontrados[personaje["nombre"]] = pos
        aux.apilar(personaje)
        pos += 1
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())
    print("\nPosiciones de personajes:")
    for nombre in nombres:
        print(f"{nombre}: posición {encontrados[nombre] if encontrados[nombre] else 'no encontrada'}")

def personajes_mas_de_5(pila):
    aux = Pila()
    print("\nPersonajes con más de 5 películas:")
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje["peliculas"] > 5:
            print(f"- {personaje['nombre']} ({personaje['peliculas']} películas)")
        aux.apilar(personaje)
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())

def cantidad_viuda_negra(pila):
    aux = Pila()
    cantidad = 0
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje["nombre"] == "Black Widow":
            cantidad = personaje["peliculas"]
        aux.apilar(personaje)
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())
    print(f"\nBlack Widow participó en {cantidad} películas.")

def personajes_por_letras(pila, letras):
    aux = Pila()
    letras = [letra.upper() for letra in letras]  
    print(f"\nPersonajes cuyos nombres empiezan con {', '.join(letras)}:")
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje["nombre"][0].upper() in letras:
            print(f"- {personaje['nombre']}")
        aux.apilar(personaje)
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())

# Carga de personajes 
pila_personajes = Pila()
pila_personajes.apilar({"nombre": "Iron Man", "peliculas": 10})
pila_personajes.apilar({"nombre": "Groot", "peliculas": 4})
pila_personajes.apilar({"nombre": "Rocket Raccoon", "peliculas": 5})
pila_personajes.apilar({"nombre": "Black Widow", "peliculas": 7})
pila_personajes.apilar({"nombre": "Doctor Strange", "peliculas": 3})
pila_personajes.apilar({"nombre": "Captain America", "peliculas": 9})
pila_personajes.apilar({"nombre": "Gamora", "peliculas": 5})

# Ejecución 
posicion_personaje(pila_personajes, ["Rocket Raccoon", "Groot"])
personajes_mas_de_5(pila_personajes)
cantidad_viuda_negra(pila_personajes)
personajes_por_letras(pila_personajes, ["C", "D", "G"])
