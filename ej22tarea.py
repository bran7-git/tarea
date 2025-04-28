def usar_la_fuerza(mochila, indice=0):
    if indice >= len(mochila):
        return False, indice  # No se encontró el sable de luz
    if mochila[indice] == 'sable de luz':
        return True, indice + 1  # Se encontró el sable, se devuelve True y cantidad de objetos sacados
    return usar_la_fuerza(mochila, indice + 1)

# Ejemplo de uso:
mochila = ['comida', 'cuerda', 'linterna', 'sable de luz', 'manta']

encontrado, objetos_sacados = usar_la_fuerza(mochila)

if encontrado:
    print(f"Sable de luz encontrado tras sacar {objetos_sacados} objetos.")
else:
    print("No se encontró un sable de luz en la mochila.")
