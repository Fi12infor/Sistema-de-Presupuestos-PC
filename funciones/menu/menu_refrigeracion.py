import time

from ..data.get_data import get_data
datos = get_data()

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