from list_ import List

def order_by_name(item):
    return item.name

def order_by_species(item):
    return item.species


class Jedi:
    def __init__(self, name, masters, lightsaber_colors, species):
        self.name = name
        self.masters = masters
        self.lightsaber_colors = lightsaber_colors
        self.species = species

    def __str__(self):
        return f"{self.name} ({self.species}) - Maestros: {', '.join(self.masters) if self.masters else 'Ninguno'} - Sables: {', '.join(self.lightsaber_colors)}"


# ---- Datos de Jedis ----
jedis = [
    {
        "name": "Luke Skywalker",
        "masters": ["Obi-Wan Kenobi", "Yoda"],
        "lightsaber_colors": ["green"],
        "species": "Human"
    },
    {
        "name": "Anakin Skywalker",
        "masters": ["Obi-Wan Kenobi"],
        "lightsaber_colors": ["blue"],
        "species": "Human"
    },
    {
        "name": "Obi-Wan Kenobi",
        "masters": ["Qui-Gon Jinn", "Yoda"],
        "lightsaber_colors": ["blue"],
        "species": "Human"
    },
    {
        "name": "Yoda",
        "masters": [],
        "lightsaber_colors": ["green"],
        "species": "Unknown"
    },
    {
        "name": "Mace Windu",
        "masters": [],
        "lightsaber_colors": ["violet"],
        "species": "Human"
    },
    {
        "name": "Ahsoka Tano",
        "masters": ["Anakin Skywalker"],
        "lightsaber_colors": ["green", "blue", "white"],
        "species": "Togruta"
    },
    {
        "name": "Kit Fisto",
        "masters": [],
        "lightsaber_colors": ["green"],
        "species": "Nautolan"
    },
    {
        "name": "Plo Koon",
        "masters": [],
        "lightsaber_colors": ["blue"],
        "species": "Kel Dor"
    },
    {
        "name": "Aayla Secura",
        "masters": ["Quinlan Vos"],
        "lightsaber_colors": ["blue"],
        "species": "Twi'lek"
    },
    {
        "name": "Qui-Gon Jinn",
        "masters": ["Count Dooku"],
        "lightsaber_colors": ["green"],
        "species": "Human"
    }
]

# ---- Carga de datos en la lista ----
list_jedis = List()
list_jedis.add_criterion("name", order_by_name)
list_jedis.add_criterion("species", order_by_species)

for jedi in jedis:
    j = Jedi(
        name=jedi["name"],
        masters=jedi["masters"],
        lightsaber_colors=jedi["lightsaber_colors"],
        species=jedi["species"],
    )
    list_jedis.append(j)



# A) listado ordenado por nombre y por especie
print("A) Listado ordenado por nombre:")
list_jedis.sort_by_criterion("name")
list_jedis.show()
print("\nA) Listado ordenado por especie:")
list_jedis.sort_by_criterion("species")
list_jedis.show()

# B) mostrar info de Ahsoka Tano y Kit Fisto
print("\nB) Información de Ahsoka Tano y Kit Fisto:")
for jedi in list_jedis:
    if jedi.name in ["Ahsoka Tano", "Kit Fisto"]:
        print(jedi)

# C) padawans de Yoda y Luke
print("\nC) Padawans de Yoda y Luke Skywalker:")
for jedi in list_jedis:
    if "Yoda" in jedi.masters or "Luke Skywalker" in jedi.masters:
        print(jedi)

# D) jedis humanos y twi'lek
print("\nD) Jedi de especie Humana y Twi'lek:")
for jedi in list_jedis:
    if jedi.species in ["Human", "Twi'lek"]:
        print(jedi)

# E) jedis que comienzan con A
print("\nE) Jedi que comienzan con A:")
for jedi in list_jedis:
    if jedi.name.startswith("A"):
        print(jedi)

# F) jedis con más de un color de sable
print("\nF) Jedi con más de un color de sable:")
for jedi in list_jedis:
    if len(jedi.lightsaber_colors) > 1:
        print(jedi)

# G) jedis con sable amarillo o violeta
print("\nG) Jedi con sable amarillo o violeta:")
for jedi in list_jedis:
    if "yellow" in jedi.lightsaber_colors or "violet" in jedi.lightsaber_colors:
        print(jedi)

# H) padawans de Qui-Gon Jinn y Mace Windu
print("\nH) Padawans de Qui-Gon Jinn y Mace Windu:")
for jedi in list_jedis:
    if "Qui-Gon Jinn" in jedi.masters or "Mace Windu" in jedi.masters:
        print(jedi)
