import time

from ..data.get_data import get_data
datos = get_data()


def menu_almacenamiento():
    print("\n===========================================================")
    print(f"1. {datos["discos duros"][0]["nombre"]} precio: {datos["discos duros"][0]["precio"]}€")
    print(f"2. {datos["discos duros"][1]["nombre"]} precio: {datos["discos duros"][1]["precio"]}€")
    print(f"3. {datos["discos duros"][2]["nombre"]} precio: {datos["discos duros"][2]["precio"]}€")
    print(f"4. {datos["discos duros"][3]["nombre"]} precio: {datos["discos duros"][3]["precio"]}€")
    op_almacenamiento = int(input("Indique el almacenamiento que quiere añadir: "))
    almacenamiento = op_almacenamiento
    almacenamiento = almacenamiento - 1
    time.sleep(1)
    return almacenamiento