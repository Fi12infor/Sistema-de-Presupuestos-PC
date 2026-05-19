import time

from ..data.get_data import get_data
datos = get_data()

def menu_refrigeracion():
    print("Usted ha seleccionado la categoria refrigeración")
    print("===========================================================")
    print(f"1. {datos["refrigeracion"][0]["nombre"]} precio: {datos["refrigeracion"][0]["precio"]}€")
    print(f"2. {datos["refrigeracion"][1]["nombre"]} precio: {datos["refrigeracion"][1]["precio"]}€")
    print(f"3. {datos["refrigeracion"][2]["nombre"]} precio: {datos["refrigeracion"][2]["precio"]}€")
    print(f"4. {datos["refrigeracion"][3]["nombre"]} precio: {datos["refrigeracion"][3]["precio"]}€")
    op_refrigeracion = int(input("Indique la refrigeración que quiere añadir: "))
    refrigeracion = op_refrigeracion
    refrigeracion = refrigeracion - 1
    time.sleep(1)
    return refrigeracion