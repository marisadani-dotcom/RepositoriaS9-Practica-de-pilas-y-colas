def consultar_siguiente(cola):
    """
    Reto 1: Devuelve el primer pendiente sin modificar la cola.
    Si está vacía, devuelve None.
    """
    if not cola:
        return None
    return cola[0]

cola_solicitudes = [
    {"id": 101, "tramite": "Renovación"},
    {"id": 102, "tramite": "Inscripción"},
    {"id": 103, "tramite": "Consulta"}
]

print("--- PRUEBA DEL RETO 1 ---")
print(f"Longitud inicial de la cola: {len(cola_solicitudes)}")

# Primera llamada
primer_intento = consultar_siguiente(cola_solicitudes)
print(f"Primera consulta -> ID del siguiente: {primer_intento['id'] if primer_intento else 'None'}")

# Segunda llamada
segundo_intento = consultar_siguiente(cola_solicitudes)
print(f"Segunda consulta -> ID del siguiente: {segundo_intento['id'] if segundo_intento else 'None'}")

print(f"Longitud final de la cola: {len(cola_solicitudes)}")