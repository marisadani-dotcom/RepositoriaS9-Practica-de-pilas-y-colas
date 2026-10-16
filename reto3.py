def cancelar_pendiente(id_solicitud):
   
    for i, solicitud in enumerate(cola_solicitudes):
        if solicitud["id"] == id_solicitud:

            return cola_solicitudes.pop(i)
            
    return None

cola_solicitudes = [
    {"id": 101, "cliente": "Juan"},
    {"id": 102, "cliente": "Maria"}, 
    {"id": 103, "cliente": "Carlos"}
]

print("Cola inicial:", [s["id"] for s in cola_solicitudes])

eliminada = cancelar_pendiente(102)
print("Solicitud eliminada:", eliminada)

print("Cola final:", [s["id"] for s in cola_solicitudes])