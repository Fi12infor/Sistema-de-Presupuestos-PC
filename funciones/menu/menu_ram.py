import time

from ..data.get_data import get_data
datos = get_data()

def menu_ram():
    print("\n===========================================================")
    print(f"1. {datos["memoria ram"][0]["nombre"]} precio: {datos["memoria ram"][0]["precio"]}€")
    print(f"2. {datos["memoria ram"][1]["nombre"]} precio: {datos["memoria ram"][1]["precio"]}€")
    print(f"3. {datos["memoria ram"][2]["nombre"]} precio: {datos["memoria ram"][2]["precio"]}€")
    print(f"4. {datos["memoria ram"][3]["nombre"]} precio: {datos["memoria ram"][3]["precio"]}€")
    op_ram = int(input("Indique la memoria ram que quiere añadir: "))
    ram = op_ram
    ram = ram - 1
    time.sleep(1)
    return ram