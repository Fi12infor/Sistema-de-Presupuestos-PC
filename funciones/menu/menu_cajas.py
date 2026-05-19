import time

from ..data.get_data import get_data
datos = get_data()

def menu_cajas():
    print("Usted ha seleccionado la categoria Cajas")
    print("===========================================================")
    print(f"1. {datos["cajas"][0]["nombre"]} precio: {datos["cajas"][0]["precio"]}€")
    print(f"2. {datos["cajas"][1]["nombre"]} precio: {datos["cajas"][1]["precio"]}€")
    print(f"3. {datos["cajas"][2]["nombre"]} precio: {datos["cajas"][2]["precio"]}€")
    print(f"4. {datos["cajas"][3]["nombre"]} precio: {datos["cajas"][3]["precio"]}€")
    op_caja = int(input("Indique la Caja que quiere añadir: "))
    caja = op_caja
    caja = caja - 1
    time.sleep(1)
    return caja