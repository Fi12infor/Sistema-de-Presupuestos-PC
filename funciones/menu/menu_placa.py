import time

from ..data.get_data import get_data
datos = get_data()

def menu_placa():
    print("\n===========================================================")
    print(f"1. {datos["placa base"][0]["nombre"]} precio: {datos["placa base"][0]["precio"]}€")
    print(f"2. {datos["placa base"][1]["nombre"]} precio: {datos["placa base"][1]["precio"]}€")
    print(f"3. {datos["placa base"][2]["nombre"]} precio: {datos["placa base"][2]["precio"]}€")
    print(f"4. {datos["placa base"][3]["nombre"]} precio: {datos["placa base"][3]["precio"]}€")
    op_placa = int(input("Indique la placa base que quiere añadir: "))
    placa = op_placa
    placa = placa - 1
    time.sleep(1)
    return placa