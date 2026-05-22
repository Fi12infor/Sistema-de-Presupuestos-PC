import time

from ..data.get_data import get_data
datos = get_data()

def menu_cpu():
    print("\n===========================================================")
    print(f"1. {datos["procesadores"][0]["nombre"]} precio: {datos["procesadores"][0]["precio"]}€")
    print(f"2. {datos["procesadores"][1]["nombre"]} precio: {datos["procesadores"][1]["precio"]}€")
    print(f"3. {datos["procesadores"][2]["nombre"]} precio: {datos["procesadores"][2]["precio"]}€")
    print(f"4. {datos["procesadores"][3]["nombre"]} precio: {datos["procesadores"][3]["precio"]}€")
    op_cpu = int(input("Indique el procesador que quiere añadir: "))
    cpu = op_cpu
    cpu = cpu - 1
    time.sleep(1)
    return cpu