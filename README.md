<div align="center">

# Sistema de Presupuestos para PC

Aplicación de consola desarrollada en Python para crear presupuestos de equipos informáticos mediante la selección de componentes.

</div>

---

## 📖 Descripción

Sistema de Presupuestos para PC es una aplicación de consola que permite seleccionar los principales componentes de un ordenador y calcular automáticamente el importe final del presupuesto.

El programa guía al usuario a través de distintos menús para elegir procesador, tarjeta gráfica, memoria RAM, almacenamiento, fuente de alimentación, placa base, refrigeración y caja.

Una vez completada la selección, muestra un resumen con los componentes elegidos, el precio del hardware, la mano de obra, la base imponible, el IGIC y el total final.

---

## 🎓 Contexto del proyecto

Este programa fue desarrollado como parte de un proyecto grupal del ciclo formativo de **Sistemas Microinformáticos y Redes (SMR)**.

El proyecto académico completo fue realizado en grupo. Mi contribución individual consistió en el desarrollo de este sistema de presupuestos en Python.

El programa está relacionado con la empresa ficticia **Inel Tech**, utilizada como base para el proyecto final de curso.

---

## ✨ Funcionalidades

* Solicitud del nombre del cliente.
* Selección interactiva de componentes mediante menús.
* Carga de productos desde un archivo JSON.
* Selección de un componente por cada categoría.
* Cálculo automático del subtotal del hardware.
* Inclusión de un coste fijo de mano de obra.
* Cálculo de la base imponible.
* Aplicación del 7 % de IGIC.
* Presentación detallada del presupuesto final.
* Posibilidad de crear varios presupuestos consecutivos.
* Separación del programa en distintos módulos.

---

## 🖥️ Componentes disponibles

El programa permite seleccionar los siguientes componentes:

* Procesador.
* Tarjeta gráfica.
* Memoria RAM.
* Almacenamiento.
* Fuente de alimentación.
* Placa base.
* Sistema de refrigeración.
* Caja.

Los productos, nombres y precios se almacenan en el archivo `data.json`.

---

## 🛠️ Tecnologías utilizadas

* Python.
* JSON.
* Programación modular.
* Funciones.
* Bucles.
* Condicionales.
* Listas y diccionarios.
* Entrada y salida por consola.
* Git.
* GitHub.

El programa utiliza únicamente módulos de la biblioteca estándar de Python, por lo que no requiere instalar dependencias externas.

---

## 📂 Estructura del proyecto

```text
Sistema-de-Presupuestos-PC/
├── funciones/
│   ├── data/
│   │   └── get_data.py
│   └── menu/
│       ├── menu_almacenamiento.py
│       ├── menu_cajas.py
│       ├── menu_cpu.py
│       ├── menu_fuente.py
│       ├── menu_gpu.py
│       ├── menu_placa.py
│       ├── menu_ram.py
│       ├── menu_refrigeracion.py
│       └── menu_salir.py
├── .gitignore
├── data.json
└── main.py
```

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/imardev/Sistema-de-Presupuestos-PC.git
```

### 2. Acceder al directorio

```bash
cd Sistema-de-Presupuestos-PC
```

### 3. Ejecutar el programa

En Windows:

```bash
python main.py
```

En algunos sistemas Linux o macOS puede ser necesario utilizar:

```bash
python3 main.py
```

---

## ▶️ Funcionamiento

Al ejecutar el programa, se solicita primero el nombre del cliente.

```text
================================
 INEL TECH - PRESUPUESTOS
================================

Nombre del cliente:
```

A continuación, el usuario debe seleccionar un producto de cada categoría mediante los diferentes menús de la aplicación.

Las selecciones se guardan temporalmente en una lista llamada `presupuesto`.

Después, el programa recorre los componentes seleccionados y suma sus precios.

```python
subtotal_hardware = 0

for componente in presupuesto:
    subtotal_hardware += componente["precio"]
```

---

## 🧮 Cálculo del presupuesto

El presupuesto se calcula utilizando los siguientes valores:

* Subtotal del hardware: suma de todos los componentes seleccionados.
* Mano de obra: `40 €`.
* Base imponible: subtotal del hardware más la mano de obra.
* IGIC: `7 %` de la base imponible.
* Total: base imponible más IGIC.

La lógica utilizada es la siguiente:

```python
IGIC = 0.07
MANO_OBRA = 40

base_imponible = subtotal_hardware + MANO_OBRA
igic = base_imponible * IGIC
total = base_imponible + igic
```

---

## 📋 Ejemplo de resultado

```text
================================
 PRESUPUESTO FINAL
================================
Cliente: Cliente de ejemplo
--------------------------------
Procesador seleccionado: 149.90€
Tarjeta gráfica seleccionada: 459.90€
Memoria RAM seleccionada: 139.95€
Almacenamiento seleccionado: 109.99€
Fuente de alimentación seleccionada: 120.99€
Placa base seleccionada: 203.99€
Refrigeración seleccionada: 84.99€
Caja seleccionada: 124.99€
--------------------------------
Hardware: 1394.70€
Mano de obra: 40.00€
Base imponible: 1434.70€
IGIC 7%: 100.43€
Total a pagar: 1535.13€
================================
```

Los productos y precios mostrados dependen de las opciones seleccionadas por el usuario.

---

## 🗃️ Gestión de los datos

La información de los componentes se encuentra en el archivo:

```text
data.json
```

Cada producto contiene los siguientes datos:

```json
{
  "id": 1,
  "categoria": "Procesador",
  "nombre": "Procesador Intel Core i7-14700KF",
  "precio": 340.90
}
```

El módulo `get_data.py` se encarga de leer el archivo JSON para que el programa pueda utilizar los productos disponibles.

Esta separación permite actualizar nombres, componentes y precios sin modificar directamente la lógica principal del programa.

---

## 🧩 Organización modular

El programa divide sus responsabilidades en varios archivos.

`main.py` contiene el flujo principal, la selección de componentes y los cálculos del presupuesto.

La carpeta `funciones/menu` contiene los menús correspondientes a cada categoría de producto.

La carpeta `funciones/data` contiene la lógica utilizada para cargar la información almacenada en el archivo JSON.

Esta organización facilita la lectura del código y evita concentrar toda la aplicación en un único archivo.

---

## 🎯 Objetivos de aprendizaje

Durante el desarrollo de este programa se trabajaron los siguientes conceptos:

* Creación de aplicaciones interactivas por consola.
* Organización modular de un proyecto en Python.
* Importación de funciones desde otros archivos.
* Lectura y utilización de datos en formato JSON.
* Uso de listas y diccionarios.
* Recorrido de estructuras de datos.
* Creación de menús interactivos.
* Cálculos de precios e impuestos.
* Formateo de valores decimales.
* Repetición del flujo mediante bucles.
* Control de versiones con Git.

---

## ⚠️ Alcance del proyecto

El programa fue diseñado como una aplicación educativa de consola.

Actualmente:

* No comprueba la compatibilidad entre componentes.
* No consulta precios en tiempo real.
* No guarda los presupuestos creados.
* No genera documentos PDF.
* No utiliza una base de datos.
* No dispone de interfaz gráfica.
* Los precios deben actualizarse manualmente en `data.json`.

Estas características forman parte del alcance definido para el ejercicio y no impiden el funcionamiento principal del programa.

---

## 👨‍💻 Desarrollo

Este repositorio contiene la implementación del sistema de presupuestos desarrollada por **Ismael Martín**.

El programa forma parte de un proyecto académico grupal de **Sistemas Microinformáticos y Redes**, aunque el desarrollo de este script fue mi contribución individual.

* GitHub: https://github.com/imardev

---

## 📄 Licencia

Actualmente este proyecto no dispone de una licencia definida.
