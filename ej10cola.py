from typing import Any, Optional


class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        return (
            self.__elements.pop()
            if self.__elements
            else None
        )

    def size(self) -> int:
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        return (
            self.__elements[-1]
            if self.__elements
            else None
        )

    def show(self):
        aux_stack = Stack()
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())


class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None:
        self.__elements.append(value)

    def attention(self) -> Optional[Any]:
        return (
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    def on_front(self) -> Optional[Any]:
        return (
            self.__elements[0]
            if self.__elements
            else None
        )

    def move_to_end(self) -> None:
        if self.size() > 0:
            self.arrive(self.attention())

    def size(self) -> int:
        return len(self.__elements)

    def show(self):
        for value in self.__elements:
            print(value)

# Datos simulados
notificaciones = [
    {"hora": "10:00", "app": "Facebook", "mensaje": "Nuevo comentario"},
    {"hora": "11:50", "app": "Twitter", "mensaje": "Aprendé Python con nosotros"},
    {"hora": "12:30", "app": "Instagram", "mensaje": "Nueva historia"},
    {"hora": "13:15", "app": "Facebook", "mensaje": "Nueva reacción"},
    {"hora": "14:00", "app": "Twitter", "mensaje": "Python es tendencia"},
    {"hora": "15:45", "app": "Whatsapp", "mensaje": "Nuevo mensaje"},
    {"hora": "16:10", "app": "Twitter", "mensaje": "Hola mundo"},
]

cola_notificaciones = Queue()
for n in notificaciones:
    cola_notificaciones.arrive(n)

# A) Eliminar todas las notificaciones de Facebook
def eliminar_facebook(cola: Queue):
    for _ in range(cola.size()):
        notif = cola.on_front()
        if notif["app"] != "Facebook":
            cola.move_to_end()
        else:
            cola.attention()

# B) Mostrar notificaciones de Twitter que contengan "Python", sin perder datos
def mostrar_twitter_con_python(cola: Queue):
    for _ in range(cola.size()):
        notif = cola.on_front()
        if notif["app"] == "Twitter" and "Python" in notif["mensaje"]:
            print(notif)
        cola.move_to_end()

# C) Usar una pila para guardar notificaciones entre 11:43 y 15:57, y contarlas
def contar_notificaciones_rango(cola: Queue):
    pila = Stack()
    for _ in range(cola.size()):
        notif = cola.on_front()
        if "11:43" <= notif["hora"] <= "15:57":
            pila.push(notif)
        cola.move_to_end()
    print(f"Cantidad de notificaciones entre 11:43 y 15:57: {pila.size()}")

# Mostrar cola original
print("Cola original:")
cola_notificaciones.show()

print("\nA) Eliminando notificaciones de Facebook...")
eliminar_facebook(cola_notificaciones)
cola_notificaciones.show()

print("\nB) Notificaciones de Twitter que contienen 'Python':")
mostrar_twitter_con_python(cola_notificaciones)

print("\nC) Contar notificaciones entre 11:43 y 15:57:")
contar_notificaciones_rango(cola_notificaciones)
