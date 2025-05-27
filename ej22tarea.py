def usar_la_fuerza(mochila, pos=0, contador=0):
    if pos >= len(mochila):
        return False, contador  # No hay más objetos, no se encontró sable

    if mochila[pos] == 'sable de luz':
        return True, contador + 1  # Encontrado

    return usar_la_fuerza(mochila, pos + 1, contador + 1)


# Mochila representada como un vector (lista)
mochila = [
    'comunicador', 'ración de comida', 'binoculares',
    'baterías', 'manta térmica', 'sable de luz', 'medkit'
]

# Llamada a la función recursiva
encontrado, cantidad_objetos = usar_la_fuerza(mochila)

# Mostrar resultados
if encontrado:
    print(f" Sable de luz encontrado sacando {cantidad_objetos} objetos.")
else:
    print(" No se encontró ningún sable de luz en la mochila.")
