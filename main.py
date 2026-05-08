## Imports
import time
from funciones.menu.menu import menu
from funciones.menu.menu_cajas import menu_cajas
from funciones.menu.menu_cpu import menu_cpu
from funciones.menu.menu_fuente import menu_fuente
from funciones.menu.menu_gpu import menu_gpu
from funciones.menu.menu_placa import menu_placa
from funciones.menu.menu_ram import menu_ram
from funciones.menu.menu_refrigeracion import menu_refrigeracion
from funciones.menu.menu_salir import menu_salir
## Codigo principal
op = 0
salir = 9



while op!=salir:
    op = menu()
    if op == 1:
        op_cpu = menu_cpu()
    elif op == 2:
        op_gpu = menu_gpu()
    elif op == 3:
        op_ram = menu_ram()
    elif op == 4:
        op_fuente = menu_fuente()
    elif op == 5:
        op_refrigeracion = menu_refrigeracion()
    elif op == 6:
        op_caja = menu_cajas()
    elif op == 7:
        op_placa = menu_placa()
    elif op == salir:
        menu_salir()
    else:
        print("Opción invalida")
        time.sleep(1)