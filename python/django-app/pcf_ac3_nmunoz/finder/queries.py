import requests as req
import os
import json
from .models import Births

API_URL = 'https://datos.comunidad.madrid/catalogo/dataset/81c88111-8e8b-4c01-a609-f8b075d4647b/resource/c8086e7b-4fc7-45cb-bc54-2435f17f1a40/download/madrid.json'

current_path = os.path.dirname(os.path.abspath(__file__))

json_data = f'{current_path}/data.json'

def get_births_data():
    return req.get(API_URL).json()['data']

def get_births_by_age(births_data):
    births = {}

    for d in births_data:
        if 'rango_edad_de_la_madre' not in births.keys():
            births[d['rango_edad_de_la_madre']] = 0
        births[d['rango_edad_de_la_madre']] += d['numero_nacimientos']

    return births

def insert_dea(dataset):
    for dea in dataset:
        codigo_dea = dea["codigo_dea"]
        direccion_ubicacion = dea["direccion_ubicacion"]
        direccion_via_nombre = dea["direccion_via_nombre"]
        direccion_portal_numero = dea["direccion_portal_numero"]
        horario_acceso = dea["horario_acceso"]
        x_utm = dea["direccion_coordenada_x"]
        y_utm = dea["direccion_coordenada_y"]

        Births.objects.create(
            codigo_dea = codigo_dea,
            direccion_ubicacion = direccion_ubicacion,
            direccion_via_nombre = direccion_via_nombre,
            direccion_portal_numero = direccion_portal_numero,
            horario_acceso = horario_acceso,
            x_utm = int(x_utm),
            y_utm = int(y_utm)
        )
