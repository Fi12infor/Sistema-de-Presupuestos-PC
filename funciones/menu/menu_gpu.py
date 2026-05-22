import time

from ..data.get_data import get_data
datos = get_data()

def menu_gpu():
    print("\n===========================================================")
    print(f"1. {datos["tarjetas graficas"][0]["nombre"]} precio: {datos["tarjetas graficas"][0]["precio"]}€")
    print(f"2. {datos["tarjetas graficas"][1]["nombre"]} precio: {datos["tarjetas graficas"][1]["precio"]}€")
    print(f"3. {datos["tarjetas graficas"][2]["nombre"]} precio: {datos["tarjetas graficas"][2]["precio"]}€")
    print(f"4. {datos["tarjetas graficas"][3]["nombre"]} precio: {datos["tarjetas graficas"][3]["precio"]}€")
    op_gpu = int(input("Indique la tarjeta grafica que quiere añadir: "))
    gpu = op_gpu
    gpu = gpu - 1
    time.sleep(1)
    return gpu