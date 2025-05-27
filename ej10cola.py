from typing import Any, Optional


class Queue:
    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None:
        self.__elements.append(value)

    def attention(self) -> Optional[Any]:
        return self.__elements.pop(0) if self.__elements else None

    def size(self) -> int:
        return len(self.__elements)
    
    def on_front(self) -> Optional[Any]:
        return self.__elements[0] if self.__elements else None

    def move_to_end(self) -> Optional[Any]:
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value

    def show(self):
        for i in range(len(self.__elements)):
            print(self.move_to_end())


class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        return self.__elements.pop() if self.__elements else None

    def size(self) -> int:
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        return self.__elements[-1] if self.__elements else None

    def show(self):
        aux = Stack()
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux.push(value)
        while aux.size() > 0:
            self.push(aux.pop())

# Cola de notificaciones simulada
notificaciones = [
    {"hora": "10:15", "app": "Twitter", "mensaje": "Aprendé Python ahora!"},
    {"hora": "11:45", "app": "Facebook", "mensaje": "Tenés nuevos recuerdos"},
    {"hora": "12:30", "app": "Instagram", "mensaje": "Nueva historia disponible"},
    {"hora": "13:15", "app": "Twitter", "mensaje": "Python es lo más!"},
    {"hora": "14:50", "app": "Facebook", "mensaje": "Nuevos eventos en tu zona"},
    {"hora": "15:55", "app": "Twitter", "mensaje": "Curso de Java"},
    {"hora": "16:10", "app": "WhatsApp", "mensaje": "Nuevo mensaje de Juan"},
    {"hora": "11:43", "app": "Twitter", "mensaje": "Python para ciencia de datos"},
]

cola_notificaciones = Queue()
for n in notificaciones:
    cola_notificaciones.arrive(n)

# a) Eliminar todas las notificaciones de Facebook
def eliminar_facebook(cola: Queue):
    for _ in range(cola.size()):
        noti = cola.on_front()
        if noti["app"] != "Facebook":
            cola.move_to_end()
        else:
            cola.attention()

# b) Mostrar notificaciones de Twitter que contienen 'Python' sin perder datos
def mostrar_twitter_python(cola: Queue):
    print("Notificaciones de Twitter con 'Python':")
    for _ in range(cola.size()):
        noti = cola.on_front()
        if noti["app"] == "Twitter" and "Python" in noti["mensaje"]:
            print("-", noti)
        cola.move_to_end()

# c) Usar una pila para almacenar notificaciones entre 11:43 y 15:57 y contarlas
def almacenar_en_pila_por_horario(cola: Queue):
    pila = Stack()
    for _ in range(cola.size()):
        noti = cola.on_front()
        if "11:43" <= noti["hora"] <= "15:57":
            pila.push(noti)
        cola.move_to_end()
    print(f"Cantidad de notificaciones entre 11:43 y 15:57: {pila.size()}")

# Ejecutar funciones
print("Cola original:")
cola_notificaciones.show()

print("\n--- a) Eliminar Facebook ---")
eliminar_facebook(cola_notificaciones)

print("\n--- b) Mostrar Twitter con 'Python' ---")
mostrar_twitter_python(cola_notificaciones)

print("\n--- c) Pila entre 11:43 y 15:57 ---")
almacenar_en_pila_por_horario(cola_notificaciones)

print("\nCola final:")
cola_notificaciones.show()

