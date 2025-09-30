# tp6_listas.py
from typing import Any, Optional

class List(list):

    CRITERION_FUNCTIONS = {}

    def add_criterion(
        self,
        key_criterion: str,
        function,
    ):
        self.CRITERION_FUNCTIONS[key_criterion] = function

    def show(
        self
    ) -> None:
        for element in self:
            print(element)

    def delete_value(
        self,
        value,
        key_value: str = None,
    ) -> Optional[Any]:
        index = self.search(value, key_value)
        return self.pop(index) if index is not None else index

    def sort_by_criterion(
        self,
        criterion_key: str = None,
    ) -> None:
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)

        if criterion is not None:
            self.sort(key=criterion)
        elif self and  isinstance(self[0], (int, str, bool)):
            self.sort()
        else:
            print('criterio de orden no encontrado')

    def search(
        self,
        search_value,
        search_key: str = None,
    ) -> Optional[int]:
        # Ordena por el criterio antes de buscar
        self.sort_by_criterion(search_key)
        start = 0
        end = len(self) - 1

        if end < 0:
            return None

        middle = (start + end) // 2

        # Si se pide buscar por un criterio que no existe y los elementos no son primitivos:
        criterion = self.CRITERION_FUNCTIONS.get(search_key)
        if criterion is None and self and not isinstance(self[0], (int, str, bool)):
            return None

        while start <= end:
            value = criterion(self[middle]) if criterion else self[middle]
            if value == search_value:
                return middle
            elif value < search_value:
                start = middle + 1
            else:
                end = middle - 1
            middle = (start + end) // 2

        return None


class Superhero:
    def __init__(self, name: str, year: int, house: str, bio: str):
        self.name = name
        self.year = year
        self.house = house  # "Marvel" o "DC"
        self.bio = bio

    def __str__(self):
        return f"{self.name} | {self.year} | {self.house} | {self.bio}"


# --- funciones criterio ---
def order_by_name(item: Superhero):
    return item.name

def order_by_year(item: Superhero):
    return item.year

def order_by_house(item: Superhero):
    return item.house

# --- carga de datos (lista independiente con los 5 faltantes incluidos) ---
def load_superheroes():
    heroes = List()
    # Añadimos una muestra representativa (podés extenderla)
    data = [
        # Algunos Marvel
        ("Wolverine", 1974, "Marvel", "Mutante con factor de curación y garras de adamantium."),
        ("Dr Strange", 1963, "Marvel", "Hechicero supremo, manipula las artes místicas y la realidad."),
        ("Star-Lord", 1976, "Marvel", "Líder de los Guardianes, aventurero espacial con habilidades tácticas."),
        ("Captain America", 1941, "Marvel", "Súper soldado símbolo de patriotismo."),

        # Algunos DC
        ("Linterna Verde", 1940, "DC", "Miembro del Cuerpo de Linternas Verdes que usa un anillo de poder."),
        ("Mujer Maravilla", 1941, "DC", "Princesa amazona con gran fuerza, justicia y compasión."),
        ("Flash", 1940, "DC", "Velocista alcanzando velocidades sobrehumanas, defensor de Central City."),
        ("Batman", 1939, "DC", "Detective enmascarado y vigilante de Gotham con traje y gadgets."),

        # Otros para cumplir condiciones (letras B, M, S)
        ("Black Panther", 1966, "Marvel", "Rey y protector de Wakanda con traje y tecnología avanzada."),
        ("Magneto", 1963, "Marvel", "Mutante capaz de controlar campos magnéticos."),
        ("Spider-Man", 1962, "Marvel", "Joven con poderes arácnidos que usa un traje y lucha contra el crimen."),
        ("Superman", 1938, "DC", "Hombre de acero con poderes sobrehumanos; símbolo de esperanza."),
        ("Green Arrow", 1941, "DC", "Arquero vigilante que usa un traje y tecnología de flechas especiales."),

        # Capitana Marvel y Woman: aclaramos Capitana Marvel como Carol Danvers (Marvel)
        ("Capitana Marvel", 1968, "Marvel", "Carol Danvers: piloto y heroína con fuerza y vuelo."),
        # Star-Lord ya añadido; añadimos algún otro B, M, S
        ("Black Widow", 1964, "Marvel", "Ex-espía con habilidades de combate y tácticas."),
        ("Moon Knight", 1975, "Marvel", "Vigilante con múltiples identidades."),
        ("Mystique", 1978, "Marvel", "Mutante que cambia de forma."),
        ("Batgirl", 1961, "DC", "Aliada de Batman, usa traje y gadgets."),
        ("Shazam", 1939, "DC", "Joven que se transforma en un héroe con poderes mágicos."),
    ]

    for name, year, house, bio in data:
        heroes.append(Superhero(name, year, house, bio))

    # criterios de lista
    heroes.add_criterion('name', order_by_name)
    heroes.add_criterion('year', order_by_year)
    heroes.add_criterion('house', order_by_house)

    return heroes


# --- resolución de la consigna (a - i) ---
def inciso_a_eliminar_linterna(heroes: List):
    print("a) Eliminar el nodo que contiene Linterna Verde:")
    removed = heroes.delete_value("Linterna Verde", "name")
    if removed is not None:
        print(f"   Eliminado: {removed}")
    else:
        print("   Linterna Verde no encontrada en la lista.")
    print()


def inciso_b_ano_wolverine(heroes: List):
    print("b) Mostrar el año de aparición de Wolverine:")
    pos = heroes.search("Wolverine", "name")
    if pos is not None:
        print(f"   Wolverine apareció en {heroes[pos].year}")
    else:
        print("   Wolverine no está en la lista.")
    print()


def inciso_c_cambiar_house_dr_strange(heroes: List):
    print("c) Cambiar la casa de Dr Strange a Marvel:")
    pos = heroes.search("Dr Strange", "name")
    if pos is not None:
        print(f"   Antes: {heroes[pos].name} pertenece a {heroes[pos].house}")
        heroes[pos].house = "Marvel"
        print(f"   Después: {heroes[pos].name} pertenece a {heroes[pos].house}")
    else:
        print("   Dr Strange no está en la lista.")
    print()


def inciso_d_traje_armadura(heroes: List):
    print('d) Mostrar nombres de superhéroes cuya biografía menciona "traje" o "armadura":')
    found = False
    for h in heroes:
        bio_lower = h.bio.lower()
        if "traje" in bio_lower or "armadura" in bio_lower:
            print(f"   {h.name}")
            found = True
    if not found:
        print("   Ningún superhéroe menciona 'traje' o 'armadura' en la biografía.")
    print()


def inciso_e_antes_1963(heroes: List):
    print("e) Nombre y casa de superhéroes cuya fecha de aparición sea anterior a 1963:")
    found = False
    for h in heroes:
        if h.year < 1963:
            print(f"   {h.name} - {h.house} ({h.year})")
            found = True
    if not found:
        print("   No hay superhéroes con año anterior a 1963 en la lista.")
    print()


def inciso_f_casa_cap_marv_y_mujer_maravilla(heroes: List):
    print("f) Mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla:")
    pos1 = heroes.search("Capitana Marvel", "name")
    if pos1 is not None:
        print(f"   Capitana Marvel -> {heroes[pos1].house}")
    else:
        print("   Capitana Marvel no está en la lista.")

    pos2 = heroes.search("Mujer Maravilla", "name")
    if pos2 is not None:
        print(f"   Mujer Maravilla -> {heroes[pos2].house}")
    else:
        print("   Mujer Maravilla no está en la lista.")
    print()


def inciso_g_info_flash_and_starlord(heroes: List):
    print("g) Mostrar toda la información de Flash y Star-Lord:")
    posf = heroes.search("Flash", "name")
    if posf is not None:
        print(f"   Flash -> {heroes[posf]}")
    else:
        print("   Flash no está en la lista.")

    poss = heroes.search("Star-Lord", "name")
    if poss is not None:
        print(f"   Star-Lord -> {heroes[poss]}")
    else:
        print("   Star-Lord no está en la lista.")
    print()


def inciso_h_listar_por_letra(heroes: List):
    print("h) Listar los superhéroes que comienzan con la letra B, M y S:")
    starts = ('B', 'M', 'S')
    found = False
    for h in heroes:
        if h.name.startswith(starts):
            print(f"   {h.name}")
            found = True
    if not found:
        print("   No se encontraron superhéroes que comiencen con B, M o S.")
    print()


def inciso_i_contar_por_casa(heroes: List):
    print("i) Determinar cuántos superhéroes hay de cada casa de cómic:")
    counts = {}
    for h in heroes:
        counts[h.house] = counts.get(h.house, 0) + 1
    for house, count in counts.items():
        print(f"   {house}: {count}")
    print()


if __name__ == "__main__":

    lista_heroes = load_superheroes()

    # Mostrar lista inicial 
    print("Lista inicial de superhéroes cargados:")
    lista_heroes.show()
    print("\n" + "-"*60 + "\n")

    # a
    inciso_a_eliminar_linterna(lista_heroes)

    # b
    inciso_b_ano_wolverine(lista_heroes)

    # c
    inciso_c_cambiar_house_dr_strange(lista_heroes)

    # d
    inciso_d_traje_armadura(lista_heroes)

    # e
    inciso_e_antes_1963(lista_heroes)

    # f
    inciso_f_casa_cap_marv_y_mujer_maravilla(lista_heroes)

    # g
    inciso_g_info_flash_and_starlord(lista_heroes)

    # h
    inciso_h_listar_por_letra(lista_heroes)

    # i
    inciso_i_contar_por_casa(lista_heroes)

    # Mostrar lista final 
    print("Lista final de superhéroes (después de modificaciones):")
    lista_heroes.show()
