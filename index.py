import requests
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # Paso 1: Hacer la solicitud a la API
    api_url = 'https://ejemplo.com/api/datos'
    response = requests.get(api_url)
    
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Paso 2: Procesar los datos de la API (supongamos que la API devuelve datos en formato JSON)
        datos_api = response.json()
# Paso 3: Generar el código HTML
        tabla_html = '<table border="1"><tr><th>Nombre</th><th>Valor</th></tr>'
        
        for dato in datos_api:
            tabla_html += f'<tr><td>{dato["nombre"]}</td><td>{dato["valor"]}</td></tr>'

        tabla_html += '</table>'