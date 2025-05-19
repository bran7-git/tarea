class TorreStark:
    def __init__(self):
        self.armaduras = []

    def almacenar(self, nueva_armadura):
        self.armaduras.append(nueva_armadura)

    def retirar(self):
        return self.armaduras.pop() if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.armaduras) == 0

    def ver_ultima(self):
        return self.armaduras[-1] if not self.esta_vacia() else None

    def cantidad(self):
        return len(self.armaduras)

#  FUNCIONES 

def buscar_hulkbuster(repositorio):
    respaldo = TorreStark()
    encontrado = False
    print("\nPelículas donde se usó la Hulkbuster (Mark XLIV):")
    while not repositorio.esta_vacia():
        pieza = repositorio.retirar()
        if pieza["modelo"] == "Mark XLIV":
            print(f"- {pieza['pelicula']}")
            encontrado = True
        respaldo.almacenar(pieza)
    while not respaldo.esta_vacia():
        repositorio.almacenar(respaldo.retirar())
    if not encontrado:
        print("Tony no usó la Hulkbuster en ninguna película.")

def listar_danadas(repositorio):
    respaldo = TorreStark()
    print("\nArmaduras que resultaron dañadas:")
    while not repositorio.esta_vacia():
        pieza = repositorio.retirar()
        if pieza["estado"] == "Dañado":
            print(f"- {pieza['modelo']} ({pieza['pelicula']})")
        respaldo.almacenar(pieza)
    while not respaldo.esta_vacia():
        repositorio.almacenar(respaldo.retirar())

def eliminar_destruidas(repositorio):
    respaldo = TorreStark()
    print("\nEliminando armaduras destruidas:")
    while not repositorio.esta_vacia():
        pieza = repositorio.retirar()
        if pieza["estado"] == "Destruido":
            print(f"- {pieza['modelo']} ({pieza['pelicula']})")
        else:
            respaldo.almacenar(pieza)
    while not respaldo.esta_vacia():
        repositorio.almacenar(respaldo.retirar())

def registrar_ultima(repositorio, modelo, pelicula, estado):
    respaldo = TorreStark()
    repetido = False
    while not repositorio.esta_vacia():
        pieza = repositorio.retirar()
        if pieza["modelo"] == modelo and pieza["pelicula"] == pelicula:
            repetido = True
        respaldo.almacenar(pieza)
    if not repetido:
        respaldo.almacenar({"modelo": modelo, "pelicula": pelicula, "estado": estado})
        print(f"\nSe registró la armadura {modelo} en {pelicula}.")
    else:
        print(f"\nYa está registrada la armadura {modelo} en la película {pelicula}.")
    while not respaldo.esta_vacia():
        repositorio.almacenar(respaldo.retirar())

def mostrar_por_peliculas(repositorio, titulos):
    respaldo = TorreStark()
    print("\nArmaduras utilizadas en películas seleccionadas:")
    while not repositorio.esta_vacia():
        pieza = repositorio.retirar()
        if pieza["pelicula"] in titulos:
            print(f"- {pieza['modelo']} ({pieza['pelicula']})")
        respaldo.almacenar(pieza)
    while not respaldo.esta_vacia():
        repositorio.almacenar(respaldo.retirar())

#  PROGRAMA PRINCIPAL 

if __name__ == "__main__":
    base_de_datos = TorreStark()

    # Cargar armaduras
    base_de_datos.almacenar({"modelo": "Mark II", "pelicula": "Iron Man", "estado": "Dañado"})
    base_de_datos.almacenar({"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Dañado"})
    base_de_datos.almacenar({"modelo": "Mark L", "pelicula": "Avengers: Infinity War", "estado": "Destruido"})
    base_de_datos.almacenar({"modelo": "Mark XLVII", "pelicula": "Spider-Man: Homecoming", "estado": "Impecable"})
    base_de_datos.almacenar({"modelo": "Mark XLVI", "pelicula": "Captain America: Civil War", "estado": "Dañado"})
    base_de_datos.almacenar({"modelo": "Mark XLIV", "pelicula": "Avengers: Endgame", "estado": "Impecable"})

    # Ejecutar acciones
    buscar_hulkbuster(base_de_datos)
    listar_danadas(base_de_datos)
    eliminar_destruidas(base_de_datos)
    registrar_ultima(base_de_datos, "Mark LXXXV", "Avengers: Endgame", "Impecable")
    mostrar_por_peliculas(base_de_datos, ["Spider-Man: Homecoming", "Captain America: Civil War"])
