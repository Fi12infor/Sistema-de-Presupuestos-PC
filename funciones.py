import time
import json


with open ('data.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)




## Declaración de funciones
def menu():
    print("=====Inel Tech S.L=====")
    print("1. Procesadores")
    print("2. Tarjetas Graficas")
    print("3. Memoria RAM")
    print("4. Fuente de alimentación")
    print("5. Refrigeración")
    print("6. Cajas")
    print("7. Placa base")
    print("8. Almacenamiento")
    print("9. Salir")
    op = int(input("Seleccione una de las categorias: "))
    return op

def menu_cpu():
    cpu = False
    print("Usted ha seleccionado la categoria procesadores")
    print("=======")
    print(f"1. {datos["procesadores"][0]["nombre"]} precio: {datos["procesadores"][0]["precio"]}€")
    print(f"2. {datos["procesadores"][1]["nombre"]} precio: {datos["procesadores"][1]["precio"]}€")
    print(f"3. {datos["procesadores"][2]["nombre"]} precio: {datos["procesadores"][2]["precio"]}€")
    print(f"4. {datos["procesadores"][3]["nombre"]} precio: {datos["procesadores"][3]["precio"]}€")
    op_cpu = int(input("Indique el procesador que quiere añadir: "))
    cpu = True
    time.sleep(1)
    return op_cpu, cpu

def menu_gpu():
    gpu = False
    print("Usted ha seleccionado la categoria Tarjetas Graficas")
    print("=======")
    print(f"1. {datos["procesadores"][0]["nombre"]} precio: {datos["procesadores"][0]["precio"]}€")
    print(f"2. {datos["procesadores"][1]["nombre"]} precio: {datos["procesadores"][1]["precio"]}€")
    print(f"3. {datos["procesadores"][2]["nombre"]} precio: {datos["procesadores"][2]["precio"]}€")
    print(f"4. {datos["procesadores"][3]["nombre"]} precio: {datos["procesadores"][3]["precio"]}€")
    op_gpu = int(input("Indique la tarjeta grafica que quiere añadir: "))
    gpu = True
    time.sleep(1)
    return op_gpu

def menu_ram():
    print("Usted ha seleccionado la categoria Memorias ram")
    print("=======")
    print(f"1. {datos["procesadores"][0]["nombre"]} precio: {datos["procesadores"][0]["precio"]}€")
    print(f"2. {datos["procesadores"][1]["nombre"]} precio: {datos["procesadores"][1]["precio"]}€")
    print(f"3. {datos["procesadores"][2]["nombre"]} precio: {datos["procesadores"][2]["precio"]}€")
    print(f"4. {datos["procesadores"][3]["nombre"]} precio: {datos["procesadores"][3]["precio"]}€")
    op_ram = int(input("Indique la memoria ram que quiere añadir: "))
    time.sleep(1)
    return op_ram

def menu_fuente():
    print("Usted ha seleccionado la categoria Fuente de alimentación")
    print("=======")
    print(f"1. {datos["procesadores"][0]["nombre"]} precio: {datos["procesadores"][0]["precio"]}€")
    print(f"2. {datos["procesadores"][1]["nombre"]} precio: {datos["procesadores"][1]["precio"]}€")
    print(f"3. {datos["procesadores"][2]["nombre"]} precio: {datos["procesadores"][2]["precio"]}€")
    print(f"4. {datos["procesadores"][3]["nombre"]} precio: {datos["procesadores"][3]["precio"]}€")
    op_fuente = int(input("Indique la fuente de alimentación que quiere añadir: "))
    time.sleep(1)
    return op_fuente

def menu_refrigeracion():
    print("Usted ha seleccionado la categoria refrigeración")
    print("=======")
    print(f"1. {datos["procesadores"][0]["nombre"]} precio: {datos["procesadores"][0]["precio"]}€")
    print(f"2. {datos["procesadores"][1]["nombre"]} precio: {datos["procesadores"][1]["precio"]}€")
    print(f"3. {datos["procesadores"][2]["nombre"]} precio: {datos["procesadores"][2]["precio"]}€")
    print(f"4. {datos["procesadores"][3]["nombre"]} precio: {datos["procesadores"][3]["precio"]}€")
    op_refrigeracion = int(input("Indique la refrigeración que quiere añadir: "))
    time.sleep(1)
    return op_refrigeracion

def menu_placa():
    print("Usted ha seleccionado la categoria  Placa base")
    print("=======")
    print(f"1. {datos["procesadores"][0]["nombre"]} precio: {datos["procesadores"][0]["precio"]}€")
    print(f"2. {datos["procesadores"][1]["nombre"]} precio: {datos["procesadores"][1]["precio"]}€")
    print(f"3. {datos["procesadores"][2]["nombre"]} precio: {datos["procesadores"][2]["precio"]}€")
    print(f"4. {datos["procesadores"][3]["nombre"]} precio: {datos["procesadores"][3]["precio"]}€")
    op_placa = int(input("Indique la placa base que quiere añadir: "))
    time.sleep(1)
    return op_placa

def menu_cajas():
    print("Usted ha seleccionado la categoria Cajas")
    print("=======")
    print(f"1. {datos["procesadores"][0]["nombre"]} precio: {datos["procesadores"][0]["precio"]}€")
    print(f"2. {datos["procesadores"][1]["nombre"]} precio: {datos["procesadores"][1]["precio"]}€")
    print(f"3. {datos["procesadores"][2]["nombre"]} precio: {datos["procesadores"][2]["precio"]}€")
    print(f"4. {datos["procesadores"][3]["nombre"]} precio: {datos["procesadores"][3]["precio"]}€")
    op_caja = int(input("Indique la Caja que quiere añadir: "))
    time.sleep(1)
    return op_caja

def menu_salir():
    ops = input("Esta seguro/a que desea salir (S/N): ")
    ops = ops.upper()
    if ops == "S":
        print("Saliendo del programa...")
        time.sleep(1)
    elif ops == "N":
        op = 0
        time.sleep(1)
    else:
        print("Opcion invalida")
        time.sleep(1)