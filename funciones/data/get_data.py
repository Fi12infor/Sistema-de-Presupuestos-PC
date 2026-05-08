import json


def get_data():
    with open ('data.json', 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    return datos