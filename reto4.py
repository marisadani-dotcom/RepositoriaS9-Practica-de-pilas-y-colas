cola_solicitudes = []
historial_atenciones = [
    {"id": 1, "cliente": "A"},
    {"id": 2, "cliente": "B"},
    {"id": 3, "cliente": "C"}
]

def deshacer_ultima_atencion():
    if not historial_atenciones:
        return None
    # Saca la última de la pila (historial) y la pone al inicio de la cola
    elemento = historial_atenciones.pop()
    cola_solicitudes.insert(0, elemento)
    return elemento

def deshacer_varias(cantidad):

    if not isinstance(cantidad, int) or cantidad <= 0:
        print("Error: La cantidad debe ser un número entero positivo.")
        return 0
        
    contador_recuperados = 0
    
    for _ in range(cantidad):
        
        resultado = deshacer_ultima_atencion()
        
        if resultado is not None:
            contador_recuperados += 1
        else:
    
            break
            
    print(f"Se informan {contador_recuperados} solicitudes recuperadas.")
    return contador_recuperados

print("Historial antes:", [s["cliente"] for s in historial_atenciones])

deshacer_varias(2)

print("Pendientes devueltos a la cola:", [s["cliente"] for s in cola_solicitudes])
print("Historial restante:", [s["cliente"] for s in historial_atenciones])