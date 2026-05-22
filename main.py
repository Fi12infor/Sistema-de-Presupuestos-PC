## Imports
from funciones.menu.menu_cajas import menu_cajas
from funciones.menu.menu_cpu import menu_cpu
from funciones.menu.menu_fuente import menu_fuente
from funciones.menu.menu_gpu import menu_gpu
from funciones.menu.menu_placa import menu_placa
from funciones.menu.menu_ram import menu_ram
from funciones.menu.menu_refrigeracion import menu_refrigeracion
from funciones.menu.menu_almacenamiento import menu_almacenamiento
from funciones.menu.menu_salir import menu_salir
from funciones.data.get_data import get_data



## Codigo principal
op = 0
salir = 9
datos = get_data()

## Constantes
IGIC = 0.07
MANO_OBRA = 40

## Codigo principal
while op != salir:
    print("================================")
    print(" INEL TECH - PRESUPUESTOS")
    print("================================\n")

    cliente = input("Nombre del cliente: ")

    presupuesto = []

    cpu = menu_cpu()
    presupuesto.append(datos["procesadores"][cpu])
    gpu = menu_gpu()
    presupuesto.append(datos["tarjetas graficas"][gpu])

    ram = menu_ram()
    presupuesto.append(datos["memoria ram"][ram])

    almacenamiento = menu_almacenamiento()
    presupuesto.append(datos["discos duros"][almacenamiento])

    fuente = menu_fuente()
    presupuesto.append(datos["fuente de alimentacion"][fuente])

    placa = menu_placa()
    presupuesto.append(datos["placa base"][placa])

    refrigeracion = menu_refrigeracion()
    presupuesto.append(datos["refrigeracion"][refrigeracion])

    caja = menu_cajas()
    presupuesto.append(datos["cajas"][caja])

    subtotal_hardware = 0

    for componente in presupuesto:
        subtotal_hardware += componente["precio"]

    base_imponible = subtotal_hardware + MANO_OBRA
    igic = base_imponible * IGIC
    total = base_imponible + igic

    print("\n================================")
    print(" PRESUPUESTO FINAL")
    print("================================")
    print(f"Cliente: {cliente}")
    print("--------------------------------")

    for componente in presupuesto:
        print(f'{componente["nombre"]}: {componente["precio"]}€')

    print("--------------------------------")
    print(f"Hardware: {subtotal_hardware:.2f}€")
    print(f"Mano de obra: {MANO_OBRA:.2f}€")
    print(f"Base imponible: {base_imponible:.2f}€")
    print(f"IGIC 7%: {igic:.2f}€")
    print(f"Total a pagar: {total:.2f}€")
    print("================================")

    repetir = input("¿Quieres crear otro presupuesto? s/n: ")

    if repetir.lower() != "s":
        menu_salir()