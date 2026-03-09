# Simulación Visual de Pila en Python

## Descripción

Este proyecto implementa una **simulación gráfica de una estructura de datos tipo pila (Stack)** utilizando **Python y la librería Tkinter**.

El programa permite visualizar de forma clara cómo funcionan las operaciones básicas de una pila, mostrando:

* Inserción de elementos
* Eliminación de elementos
* Eliminación de un valor específico
* Manejo de variables al realizar operaciones de eliminación
* Representación gráfica del **TOPE**
* Visualización del **arreglo interno de la pila**
* Historial de operaciones realizadas

La pila tiene una **capacidad máxima de 8 elementos**, tal como se utiliza comúnmente en ejercicios académicos de estructuras de datos.

---

# Características del programa

## Interfaz gráfica

El sistema muestra visualmente:

* La **pila representada como bloques**
* El **puntero TOPE**
* Las **posiciones del arreglo interno**
* Un **historial de operaciones**
* Un **panel de variables (Z, T, U, P)**

Esto permite observar cómo cambia el estado de la pila después de cada operación.

---

# Operaciones disponibles

## Insertar

Permite agregar un elemento a la pila siempre que no esté llena.

Si la pila ya tiene 8 elementos, el programa mostrará un error de **Overflow**.

Ejemplo:

Insertar → X

---

## Eliminar

Elimina el elemento que se encuentra en el **tope de la pila** y guarda el valor eliminado en una variable.

Variables disponibles:

* Z
* T
* U
* P

Ejemplo:

Z = X

---

## Eliminar valor específico

Permite eliminar un valor específico dentro de la pila.

El algoritmo utiliza una **pila auxiliar** para poder acceder a elementos que no estén en el tope.

### Caso especial implementado

Si el valor que se intenta eliminar **no existe en la pila**, el programa realiza una **simulación automática**:

1. Inserta temporalmente el valor en la pila
2. Lo muestra visualmente
3. Después de 2 segundos lo elimina automáticamente

Esto permite simular la operación solicitada sin alterar permanentemente la estructura.

---

## Vaciar pila

Elimina todos los elementos de la pila y la deja en estado inicial.

---

# Componentes visuales

## Pila gráfica

Cada elemento se representa como un **bloque azul** dentro de la estructura de la pila.

---

## Indicador de TOPE

El programa muestra una **flecha roja** que señala el elemento que actualmente se encuentra en el **tope de la pila**.

También se muestra el valor numérico del tope.

Ejemplo:

TOPE = 3

---

## Arreglo interno

Se muestra la representación del arreglo utilizado internamente para almacenar los elementos.

Ejemplo:

```
[ X ] [ Y ] [ V ] [   ] [   ] [   ] [   ] [   ]
```

---

## Historial

El programa registra todas las operaciones realizadas para poder observar la secuencia de acciones.

Ejemplo:

```
Insertar → X
Insertar → Y
Eliminar valor específico → X
```

---

# Tecnologías utilizadas

* Python 3
* Tkinter (interfaz gráfica)

Tkinter es una biblioteca estándar de Python que permite crear aplicaciones gráficas de manera sencilla.

---

# Cómo ejecutar el programa

1. Instalar Python 3 en el sistema.

2. Guardar el archivo del programa, por ejemplo:

```
pila_visual.py
```

3. Ejecutar el programa desde la terminal o consola:

```
python pila_visual.py
```

4. Se abrirá la interfaz gráfica de la simulación de pila.

---

# Aplicación académica

Este programa está diseñado como apoyo para el aprendizaje de **estructuras de datos**, permitiendo visualizar:

* Funcionamiento de una **pila (Stack)**
* Operaciones **Push** e **Pop**
* Manejo del **TOPE**
* Conceptos de **Overflow y Underflow**
* Uso de **estructuras auxiliares**

---

# Autor
Gomez Ek Adolfo Rene 
Proyecto académico desarrollado para prácticas de **Estructura de Datos** utilizando Python.
