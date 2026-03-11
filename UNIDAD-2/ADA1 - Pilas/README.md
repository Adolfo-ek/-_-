Este proyecto muestra la implementación de la estructura de datos Pila (Stack) utilizando Python y Tkinter.
Se desarrollaron dos programas para demostrar su funcionamiento:

Evaluador de expresiones aritméticas en notación prefija y posfija.

Resolución del juego de las Torres de Hanoi utilizando la clase Pila.

Ambos programas incluyen interfaz gráfica para visualizar cómo se comporta la pila.

Tecnologías utilizadas

Python

Tkinter (interfaz gráfica)

Programa 1: Evaluador de Expresiones con Pila
Descripción

Permite evaluar expresiones matemáticas usando una pila en notación prefija o posfija.

Funcionamiento

Si el elemento es un número, se inserta en la pila.

Si es un operador, se sacan dos elementos de la pila, se realiza la operación y el resultado se vuelve a insertar.

Ejemplo

Expresión posfija:

3 4 + 2 *

Resultado:

14
Programa 2: Torres de Hanoi con Pila
Descripción

Simula el juego de Torres de Hanoi usando tres pilas que representan las torres.

Reglas

Solo se mueve un disco a la vez.

Un disco grande no puede colocarse sobre uno pequeño.

Se utilizan tres torres.

El número mínimo de movimientos se calcula con:

2
𝑛
−
1
2
n
−1

Ejemplo para 3 discos:

7 movimientos.
Autor 
Gomez Ek Adolfo Rene
