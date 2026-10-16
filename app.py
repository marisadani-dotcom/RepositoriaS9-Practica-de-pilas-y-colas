from flask import Flask, render_template, request, redirect, url_for
import logica

app = Flask(__name__)

@app.route('/')
def index():
    # Obtenemos estadísticas del Reto 5
    pendientes, historial, unicas = logica.obtener_estadisticas()
    siguiente = logica.consultar_siguiente() # Reto 1
    
    return render_template(
        'index.html', 
        pendientes=logica.cola_solicitudes, 
        historial=logica.historial_atenciones,
        cant_pendientes=pendientes,
        cant_historial=historial,
        cant_unicas=unicas,
        siguiente=siguiente
    )

@app.route('/registrar', methods=['POST'])
def registrar():
    cliente = request.form.get('cliente')
    asunto = request.form.get('asunto')
    if cliente and asunto:
        logica.registrar_solicitud(cliente, asunto)
    return redirect(url_for('index'))

@app.route('/atender')
def atender():
    logica.atender_siguiente()
    return redirect(url_for('index'))

@app.route('/deshacer')
def deshacer():
    logica.deshacer_ultima_atencion()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)