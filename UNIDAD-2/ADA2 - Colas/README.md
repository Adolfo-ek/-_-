Implementación de Estructuras de Datos: Pila y Cola en Python
Descripción

Este proyecto reúne varias aplicaciones desarrolladas en Python para demostrar el uso de las estructuras de datos Pila (Stack) y Cola (Queue) mediante interfaces gráficas creadas con Tkinter.

Los programas simulan diferentes situaciones donde estas estructuras son útiles, permitiendo visualizar su funcionamiento de forma práctica.

Tecnologías utilizadas

Python

Tkinter (interfaz gráfica)

Estructuras de datos utilizadas
Pila (Stack)

La pila funciona con el principio LIFO (Last In, First Out):

El último elemento que entra es el primero en salir.

Operaciones principales:

push / Pone() → insertar elemento

pop / Quita() → eliminar elemento

Cola (Queue)

La cola funciona con el principio FIFO (First In, First Out):

El primer elemento que entra es el primero en salir.

Operaciones principales:

encolar() → agregar elemento

desencolar() → eliminar el primer elemento

Programas incluidos
1. Evaluador de Expresiones con Pila

Este programa permite evaluar expresiones matemáticas utilizando una pila en notación prefija o posfija.

Funcionamiento

Si el elemento es un número, se inserta en la pila.

Si es un operador, se sacan dos elementos de la pila.

Se realiza la operación y el resultado se vuelve a insertar.

Ejemplo

Expresión:

3 4 + 2 *

Resultado:

14
2. Torres de Hanoi utilizando Pila

Este programa resuelve el problema clásico de Torres de Hanoi utilizando pilas para representar las torres.

Reglas

Solo se puede mover un disco a la vez

Un disco grande no puede colocarse sobre uno pequeño

Se utilizan tres torres

El número mínimo de movimientos se calcula con:

2
𝑛
−
1
2
n
−1

Ejemplo para 3 discos:

7 movimientos
3. Suma de dos Colas

Este programa recibe dos colas con números enteros y genera una nueva cola con la suma de los elementos correspondientes.

Ejemplo
Cola A	Cola B	Resultado
3	6	9
4	2	6
2	9	11
8	11	19
12	3	15
4. Sistema de Colas para Compañía de Seguros

Este programa simula un sistema de atención al cliente utilizando colas de servicios.

Cada cliente recibe un número de turno dependiendo del servicio solicitado.
El personal puede llamar al siguiente cliente en la cola correspondiente.

Servicios disponibles

Servicio 1

Servicio 2

Servicio 3

Ejemplo

Llegada de cliente:

Turno generado: S1-1

Atención de cliente:

Atendiendo: S1-1
Cómo ejecutar los programas

Instalar Python 3

Descargar los archivos .py

Ejecutar en la terminal según el programa:

Evaluador de expresiones:

python evaluador_pila.py

Torres de Hanoi:

python torres_hanoi.py

Suma de colas:

python suma_colas.py

Sistema de colas de atención:

python sistema_colas.py
Objetivo del proyecto
Autor
Gomez Ek Adolfo Rene 
El objetivo de este proyecto es aplicar y comprender el uso de estructuras de datos fundamentales (Pila y Cola) mediante la resolución de diferentes problemas de programación y su visualización con interfaces gráficas en Python.
Autor
