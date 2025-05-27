from queue_ import Queue
from stack import Stack

# Datos de ejemplo
notificaciones = [
    {"hora": "11:00", "app": "Facebook", "mensaje": "Recordatorio de evento"},
    {"hora": "11:45", "app": "Twitter", "mensaje": "Nuevo curso de Python disponible"},
    {"hora": "12:15", "app": "Instagram", "mensaje": "Nueva foto etiquetada"},
    {"hora": "13:30", "app": "Facebook", "mensaje": "Publicación de amigo"},
    {"hora": "14:00", "app": "Twitter", "mensaje": "Python es tendencia"},
    {"hora": "15:00", "app": "WhatsApp", "mensaje": "Nuevo mensaje de grupo"},
    {"hora": "16:00", "app": "Twitter", "mensaje": "Actualización disponible"},
]

cola_notificaciones = Queue()
for notif in notificaciones:
    cola_notificaciones.arrive(notif)

print("--- a) Eliminar notificaciones de Facebook ---")
def eliminar_facebook(cola: Queue):
    aux = Queue()
    while cola.size() > 0:
        notif = cola.attention()
        if notif["app"] != "Facebook":
            aux.arrive(notif)
    while aux.size() > 0:
        cola.arrive(aux.attention())

eliminar_facebook(cola_notificaciones)
cola_notificaciones.show()

print("\n--- b) Mostrar notificaciones de Twitter con 'Python' ---")
def mostrar_twitter_python(cola: Queue):
    aux = Queue()
    while cola.size() > 0:
        notif = cola.attention()
        if notif["app"] == "Twitter" and "Python" in notif["mensaje"]:
            print(notif)
        aux.arrive(notif)
    while aux.size() > 0:
        cola.arrive(aux.attention())

mostrar_twitter_python(cola_notificaciones)

print("\n--- c) Notificaciones entre 11:43 y 15:57 (guardadas en una pila) ---")
def en_rango(hora: str) -> bool:
    return "11:43" <= hora <= "15:57"

def notificaciones_en_rango(cola: Queue):
    pila = Stack()
    contador = 0
    aux = Queue()
    while cola.size() > 0:
        notif = cola.attention()
        if en_rango(notif["hora"]):
            pila.push(notif)
            contador += 1
        aux.arrive(notif)
    while aux.size() > 0:
        cola.arrive(aux.attention())
    return pila, contador

pila_rango, cantidad = notificaciones_en_rango(cola_notificaciones)
print(f"Cantidad de notificaciones entre 11:43 y 15:57: {cantidad}")


