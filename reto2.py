cola_solicitudes = [
    {"id": 101, "cliente": "Juan", "tipo": "Soporte"},
    {"id": 102, "cliente": "Maria", "tipo": "Factura"}
]

historial_atenciones = [
    {"id": 99, "cliente": "Carlos", "tipo": "Soporte"}
]

def consultar_siguiente():
    """
    Muestra el primer elemento de la cola de pendientes 
    sin sacarlo ni modificar su orden.
    """
    if not cola_solicitudes:
        return None
    
    return cola_solicitudes[0]

def buscar_solicitud(id_solicitud):
    """
    Busca una solicitud por ID primero en la cola de pendientes
    y luego en la pila del historial.
    Condición: No modifica el orden de ninguna estructura.
    """

    for solicitud in cola_solicitudes:
        if solicitud["id"] == id_solicitud:
            return solicitud, "pendientes"
            
    for solicitud in historial_atenciones:
        if solicitud["id"] == id_solicitud:
            return solicitud, "historial"
            
    return None