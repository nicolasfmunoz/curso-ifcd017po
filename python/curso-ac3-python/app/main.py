import requests as req
import json
import csv
import os
import re
from pprint import pprint


API_URL = 'https://datos.comunidad.madrid/catalogo/dataset/81c88111-8e8b-4c01-a609-f8b075d4647b/resource/c8086e7b-4fc7-45cb-bc54-2435f17f1a40/download/madrid.json'

current_path = os.path.dirname(os.path.abspath(__file__))

json_data = f'{current_path}/data.json'

json_response = req.get(API_URL).json()
with open(json_data, 'w', encoding='UTF-8') as file:
    json.dump(json_response, file, ensure_ascii=False)

def get_births_by_age(births_data):
    births = {}

    for d in births_data:
        if 'rango_edad_de_la_madre' not in births.keys():
            births[d['rango_edad_de_la_madre']] = 0
        births[d['rango_edad_de_la_madre']] += d['numero_nacimientos']

    return births


def get_data():
    with open(json_data, 'r', encoding='UTF-8') as file:
        data = json.load(file)['data']
        return data

data = get_data()

#nacimientos = [d if int(d['numero_nacimientos']) > 0 else {} for d in data]

nacimientos = filter(lambda x: x['numero_nacimientos'] > 0, data)

#nacimientos_edad = list(map(lambda x: {x['rango_edad_de_la_madre']: x['numero_nacimientos']}, nacimientos))

nacimientos_edad = get_births_by_age(data)

pprint(nacimientos_edad)
