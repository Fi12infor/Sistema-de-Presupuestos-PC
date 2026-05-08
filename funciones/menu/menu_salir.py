import time

from ..data.get_data import get_data
datos = get_data()

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