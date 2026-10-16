# ==========================================
# VARIABLES GLOBALES (ESTRUCTURAS DE DATOS)
# ==========================================
cola_solicitudes = []      # Cola para pendientes
historial_atenciones = []  # Pila para el historial

# ------------------------------------------
# RETOS 1 AL 5 INTEGRADOS
# ------------------------------------------

def registrar_solicitud(cliente, asunto):
    if es_solicitud_duplicada(cliente, asunto):
        return None
    nueva = {"id": len(cola_solicitudes) + len(historial_atenciones) + 101, "cliente": cliente, "asunto": asunto}
    cola_solicitudes.append(nueva)
    return nueva

def consultar_siguiente():
    if not cola_solicitudes:
        return None
    return cola_solicitudes[0]

def buscar_solicitud(id_solicitud):
    for s in cola_solicitudes:
        if s["id"] == int(id_solicitud):
            return s, "pendientes"
    for s in historial_atenciones:
        if s["id"] == int(id_solicitud):
            return s, "historial"
    return None

def cancelar_pendiente(id_solicitud):
    for i, s in enumerate(cola_solicitudes):
        if s["id"] == int(id_solicitud):
            return cola_solicitudes.pop(i)
    return None

def atender_siguiente():
    if not cola_solicitudes:
        return None
    solicitud = cola_solicitudes.pop(0)
    historial_atenciones.append(solicitud)
    return solicitud

def deshacer_ultima_atencion():
    if not historial_atenciones:
        return None
    solicitud = historial_atenciones.pop()
    cola_solicitudes.insert(0, solicitud)
    return solicitud

def deshacer_varias(cantidad):
    if not isinstance(cantidad, int) or cantidad <= 0:
        return 0
    contador = 0
    for _ in range(cantidad):
        if deshacer_ultima_atencion():
            contador += 1
        else:
            break
    return contador

def es_solicitud_duplicada(cliente, asunto):
    c_norm = cliente.strip().lower()
    a_norm = asunto.strip().lower()
    for s in cola_solicitudes:
        if s["cliente"].strip().lower() == c_norm and s["asunto"].strip().lower() == a_norm:
            return True
    return False

def obtener_estadisticas():
    unicas = set((s["cliente"].strip().lower(), s["asunto"].strip().lower()) for s in cola_solicitudes + historial_atenciones)
    return len(cola_solicitudes), len(historial_atenciones), len(unicas)