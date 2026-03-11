Este programa implementa una estructura de datos tipo pila para evaluar expresiones aritméticas en notación prefija y posfija.
La aplicación incluye una interfaz gráfica desarrollada con Tkinter que permite visualizar el comportamiento de la pila mientras se realiza la evaluación.

Durante la ejecución del programa se muestran los elementos que se insertan y eliminan de la pila, permitiendo observar el proceso paso a paso.

Funcionalidades

Evaluación de expresiones en notación posfija

Evaluación de expresiones en notación prefija

Visualización gráfica de la pila

Inserción y eliminación automática de elementos

Animación del proceso de evaluación

Visualización del resultado final

Tecnologías utilizadas

Python

Tkinter para la interfaz gráfica

Estructura del programa

El programa utiliza una lista para representar la pila y aplica las operaciones básicas:

Push → insertar elemento en la pila

Pop → eliminar elemento de la pila

Durante la evaluación:

Si el token es un número → se inserta en la pila.

Si el token es un operador → se extraen dos elementos de la pila.

Se realiza la operación aritmética.

El resultado se vuelve a insertar en la pila.
