def es_solicitud_duplicada(cliente, asunto):
    cliente_norm = cliente.strip().lower()
    asunto_norm = asunto.strip().lower()
    for s in cola_solicitudes:
        if s["cliente"].strip().lower() == cliente_norm and s["asunto"].strip().lower() == asunto_norm:
            return True
    return False

def registrar_solicitud(cliente, asunto):
    if es_solicitud_duplicada(cliente, asunto):
        print("Error: Ya existe una solicitud pendiente idéntica.")
        return None
    
    nueva_solicitud = {"id": len(cola_solicitudes) + 101, "cliente": cliente, "asunto": asunto}
    cola_solicitudes.append(nueva_solicitud)
    return nueva_solicitud

def obtener_estadisticas():
    cant_pendientes = len(cola_solicitudes)
    cant_historial = len(historial_atenciones)
    unicas = set()
    for s in cola_solicitudes + historial_atenciones:
        clave = (s["cliente"].strip().lower(), s["asunto"].strip().lower())
        unicas.add(clave)
    return cant_pendientes, cant_historial, len(unicas)

cola_solicitudes = []
historial_atenciones = []

registrar_solicitud("Ana", "Wi-Fi")

registrar_solicitud("ana ", "wi-fi ")

print("Cantidad de pendientes en la cola:", len(cola_solicitudes))

pendientes, historial, unicas = obtener_estadisticas()
print(f"Estadísticas -> Pendientes: {pendientes}, Historial: {historial}, Únicas globales: {unicas}")