from queue import Queue
from datetime import datetime

# Definimos una notificación como diccionario
def crear_notificacion(hora, app, mensaje):
    return {
        "hora": hora,           # string formato HH:MM
        "app": app.lower(),     # nombre de la aplicación en minúscula
        "mensaje": mensaje
    }

# Cargar cola con notificaciones de ejemplo
def cargar_notificaciones():
    cola = Queue()
    datos = [
        crear_notificacion("10:30", "Facebook", "Nueva solicitud de amistad"),
        crear_notificacion("11:45", "Twitter", "Python es genial"),
        crear_notificacion("12:00", "Instagram", "Nueva historia disponible"),
        crear_notificacion("13:15", "Twitter", "Aprende Python con nosotros"),
        crear_notificacion("14:50", "Facebook", "Recordatorio de evento"),
        crear_notificacion("15:30", "Twitter", "¿Te interesa Python?"),
        crear_notificacion("16:10", "LinkedIn", "Nueva oferta de trabajo"),
    ]
    for n in datos:
        cola.put(n)
    return cola

# a. Eliminar notificaciones de Facebook
def eliminar_facebook(cola):
    nueva_cola = Queue()
    while not cola.empty():
        noti = cola.get()
        if noti['app'] != 'facebook':
            nueva_cola.put(noti)
    return nueva_cola

# b. Mostrar notificaciones de Twitter que contengan "Python"
def mostrar_twitter_python(cola):
    aux = Queue()
    print("Notificaciones de Twitter con 'Python':")
    while not cola.empty():
        noti = cola.get()
        if noti['app'] == 'twitter' and 'python' in noti['mensaje'].lower():
            print(f"[{noti['hora']}] {noti['app'].capitalize()}: {noti['mensaje']}")
        aux.put(noti)
    # Restaurar la cola original
    while not aux.empty():
        cola.put(aux.get())

# c. Usar pila para notificaciones entre 11:43 y 15:57
def notificaciones_rango_horario(cola):
    pila = []
    aux = Queue()
    hora_ini = datetime.strptime("11:43", "%H:%M")
    hora_fin = datetime.strptime("15:57", "%H:%M")
    while not cola.empty():
        noti = cola.get()
        hora_noti = datetime.strptime(noti["hora"], "%H:%M")
        if hora_ini <= hora_noti <= hora_fin:
            pila.append(noti)
        aux.put(noti)
    # Restaurar la cola
    while not aux.empty():
        cola.put(aux.get())
    print(f"Cantidad de notificaciones entre 11:43 y 15:57: {len(pila)}")

# Ejecución de prueba
if __name__ == "__main__":
    cola = cargar_notificaciones()

    print("a) Eliminando notificaciones de Facebook...")
    cola = eliminar_facebook(cola)

    print("\nb) Mostrando notificaciones de Twitter que contienen 'Python'...")
    mostrar_twitter_python(cola)

    print("\nc) Cantidad de notificaciones entre 11:43 y 15:57...")
    notificaciones_rango_horario(cola)
