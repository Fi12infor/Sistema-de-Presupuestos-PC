import time

from ..data.get_data import get_data
datos = get_data()

def menu_fuente():
    print("\n===========================================================")
    print(f"1. {datos["fuente de alimentacion"][0]["nombre"]} precio: {datos["fuente de alimentacion"][0]["precio"]}€")
    print(f"2. {datos["fuente de alimentacion"][1]["nombre"]} precio: {datos["fuente de alimentacion"][1]["precio"]}€")
    print(f"3. {datos["fuente de alimentacion"][2]["nombre"]} precio: {datos["fuente de alimentacion"][2]["precio"]}€")
    print(f"4. {datos["fuente de alimentacion"][3]["nombre"]} precio: {datos["fuente de alimentacion"][3]["precio"]}€")
    op_fuente = int(input("Indique la fuente de alimentación que quiere añadir: "))
    fuente = op_fuente
    fuente = fuente - 1
    time.sleep(1)
    return fuente