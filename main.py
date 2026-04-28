## Imports
import time
import json
from funciones import menu_cpu, menu_gpu, menu_ram, menu_fuente, menu_placa, menu_refrigeracion, menu, menu_cajas, menu_salir
## Codigo principal
op = 0
salir = 9

with open ('data.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)


while op!=salir:
    op = menu()
    if op == 1:
        op_cpu = menu_cpu()
    elif op == 2:
        op_gpu = menu_gpu()
    elif op == 3:
        op_ram = menu_ram()
    elif op == 4:
        op_fuente = menu_fuente()
    elif op == 5:
        op_refrigeracion = menu_refrigeracion()
    elif op == 6:
        op_caja = menu_cajas()
    elif op == 7:
        op_placa = menu_placa()
    elif op == salir:
        menu_salir()
    else:
        print("Opción invalida")
        time.sleep(1)