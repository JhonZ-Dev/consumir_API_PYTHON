import requests
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # Paso 1: Hacer la solicitud a la API
    api_url = 'https://ejemplo.com/api/datos'
    response = requests.get(api_url)