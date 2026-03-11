Este proyecto consiste en la implementación y aplicación de la estructura de datos Pila (Stack) utilizando el lenguaje Python y una interfaz gráfica con Tkinter.

Se desarrollaron dos programas principales para demostrar el funcionamiento de esta estructura:

Evaluación de expresiones aritméticas en notación prefija y posfija

Resolución del juego de las Torres de Hanoi utilizando pilas

Ambos programas permiten visualizar de manera gráfica cómo funciona la pila durante la ejecución.

Tecnologías utilizadas

Python 3

Tkinter (interfaz gráfica)

Programación orientada a objetos

Estructura de Datos Pila

Una pila es una estructura de datos que funciona bajo el principio:

LIFO (Last In, First Out)
El último elemento que entra es el primero que sale.

Operaciones principales utilizadas en el proyecto:

Push (Pone) → insertar elemento

Pop (Quita) → eliminar elemento

Pila_vacia()

Pila_llena()

Programa 1: Evaluador de Expresiones con Pila
Descripción

Este programa permite evaluar expresiones aritméticas utilizando una pila en:

Notación Posfija

Notación Prefija

El sistema muestra gráficamente el estado de la pila mientras se realiza el cálculo.

Funcionamiento

El algoritmo sigue los siguientes pasos:

Se separa la expresión en tokens.

Si el token es un número:

Se inserta en la pila.

Si el token es un operador:

Se extraen dos elementos de la pila.

Se realiza la operación aritmética.

El resultado se vuelve a insertar en la pila.

Al finalizar, el único elemento restante es el resultado final.

Ejemplo Posfijo

Entrada:

3 4 + 2 *

Proceso:

3 → push
4 → push
+ → pop 3 y 4 → resultado 7
2 → push
* → pop 7 y 2 → resultado 14

Resultado:

14
Ejemplo Prefijo

Entrada:

* + 3 4 2

Resultado:

14
Programa 2: Torres de Hanoi utilizando la clase Pila
Descripción

Este programa implementa la solución del problema clásico Torres de Hanoi utilizando la estructura de datos Pila.

Cada torre del juego es representada mediante una instancia de la clase Pila, donde los discos se almacenan siguiendo las reglas del juego.

El programa incluye una interfaz gráfica que muestra el movimiento de los discos entre las torres.

Reglas del juego

Solo se puede mover un disco a la vez

Un disco grande no puede colocarse sobre uno más pequeño

Se utilizan tres torres

Algoritmo

Se utiliza el algoritmo recursivo clásico de Torres de Hanoi.

Pasos generales:

Mover n-1 discos de la torre origen a la torre auxiliar.

Mover el disco más grande a la torre destino.

Mover los n-1 discos desde la torre auxiliar a la torre destino.

Número mínimo de movimientos

El número mínimo de movimientos se calcula con la fórmula:

2
𝑛
−
1
2
n
−1

Ejemplo:

Para 3 discos:

2³ - 1 = 7 movimientos
Interfaz gráfica

Los programas utilizan Tkinter para mostrar:

Visualización de la pila

Movimiento de discos en Torres de Hanoi

Contador de movimientos

Controles de interacción con el usuario

Esto permite observar de forma clara el comportamiento de la estructura de datos.

Cómo ejecutar los programas

Instalar Python 3

Descargar los archivos .py

Ejecutar en la terminal:

Evaluador de expresiones:

python evaluador_pila.py

Torres de Hanoi:

python torres_hanoi.py
Objetivo académico

El objetivo de este proyecto es aplicar y comprender el funcionamiento de la estructura de datos pila, utilizándola para resolver problemas clásicos de programación como:

Evaluación de expresiones matemáticas

Resolución del problema de Torres de Hanoi

Además, se busca reforzar conceptos de:

Programación orientada a objetos

Recursividad

Estructuras de datos

Interfaces gráficas en Python
Autor
Gomez Ek Adolfo Rene 

Operaciones principales utilizadas en el proyecto:

Push (Pone) → insertar elemento

Pop (Quita) → eliminar elemento

Pila_vacia()

Pila_llena()

Programa 1: Evaluador de Expresiones con Pila
Descripción

Este programa permite evaluar expresiones aritméticas utilizando una pila en:

Notación Posfija

Notación Prefija

El sistema muestra gráficamente el estado de la pila mientras se realiza el cálculo.

Funcionamiento

El algoritmo sigue los siguientes pasos:

Se separa la expresión en tokens.

Si el token es un número:

Se inserta en la pila.

Si el token es un operador:

Se extraen dos elementos de la pila.

Se realiza la operación aritmética.

El resultado se vuelve a insertar en la pila.

Al finalizar, el único elemento restante es el resultado final.

Ejemplo Posfijo

Entrada:

3 4 + 2 *

Proceso:

3 → push
4 → push
+ → pop 3 y 4 → resultado 7
2 → push
* → pop 7 y 2 → resultado 14

Resultado:

14
Ejemplo Prefijo

Entrada:

* + 3 4 2

Resultado:

14
Programa 2: Torres de Hanoi utilizando la clase Pila
Descripción

Este programa implementa la solución del problema clásico Torres de Hanoi utilizando la estructura de datos Pila.

Cada torre del juego es representada mediante una instancia de la clase Pila, donde los discos se almacenan siguiendo las reglas del juego.

El programa incluye una interfaz gráfica que muestra el movimiento de los discos entre las torres.

Reglas del juego

Solo se puede mover un disco a la vez

Un disco grande no puede colocarse sobre uno más pequeño

Se utilizan tres torres

Algoritmo

Se utiliza el algoritmo recursivo clásico de Torres de Hanoi.

Pasos generales:

Mover n-1 discos de la torre origen a la torre auxiliar.

Mover el disco más grande a la torre destino.

Mover los n-1 discos desde la torre auxiliar a la torre destino.

Número mínimo de movimientos

El número mínimo de movimientos se calcula con la fórmula:

2
𝑛
−
1
2
n
−1

Ejemplo:

Para 3 discos:

2³ - 1 = 7 movimientos
Interfaz gráfica

Los programas utilizan Tkinter para mostrar:

Visualización de la pila

Movimiento de discos en Torres de Hanoi

Contador de movimientos

Controles de interacción con el usuario

Esto permite observar de forma clara el comportamiento de la estructura de datos.

Cómo ejecutar los programas

Instalar Python 3

Descargar los archivos .py

Ejecutar en la terminal:

Evaluador de expresiones:

python evaluador_pila.py

Torres de Hanoi:

python torres_hanoi.py
Objetivo académico

El objetivo de este proyecto es aplicar y comprender el funcionamiento de la estructura de datos pila, utilizándola para resolver problemas clásicos de programación como:

Evaluación de expresiones matemáticas

Resolución del problema de Torres de Hanoi

Además, se busca reforzar conceptos de:

Programación orientada a objetos

Recursividad

Estructuras de datos

Interfaces gráficas en Python
Autor
Gomez Ek Adolfo Rene
Estructura del programa

El programa utiliza una lista para representar la pila y aplica las operaciones básicas:

Push → insertar elemento en la pila

Pop → eliminar elemento de la pila

Durante la evaluación:

Si el token es un número → se inserta en la pila.

Si el token es un operador → se extraen dos elementos de la pila.

Se realiza la operación aritmética.

El resultado se vuelve a insertar en la pila.
