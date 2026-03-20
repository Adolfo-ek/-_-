# Torre de Hanói en Python

## Descripción

Este proyecto implementa la solución al problema clásico de **la Torre de Hanói** utilizando Python.

El problema consiste en mover una torre de discos de una varilla a otra siguiendo ciertas reglas.

Este algoritmo es un ejemplo clásico de **recursividad y uso de pilas en estructuras de datos**.

## Reglas del problema

1. Solo se puede mover **un disco a la vez**.
2. Un disco **más grande nunca puede colocarse sobre uno más pequeño**.
3. Solo se puede mover el **disco superior de cada torre**.

## Funcionamiento del programa

El programa:

* Representa cada torre como una **pila**
* Resuelve el problema mediante **recursividad**
* Muestra los movimientos realizados
* Calcula el número mínimo de movimientos necesarios

## Fórmula del número mínimo de movimientos

El número mínimo de movimientos se calcula con la fórmula:

```
2^n - 1
```

Donde:

* **n** = número de discos

Ejemplo:

| Discos | Movimientos mínimos |
| ------ | ------------------- |
| 3      | 7                   |
| 4      | 15                  |
| 5      | 31                  |

## Tecnologías utilizadas

* Python
* Algoritmos recursivos
* Estructura de datos tipo pila

## Ejecución

1. Tener Python instalado
2. Ejecutar el programa:

```bash
python hanoi.py
```

3. Ingresar el número de discos cuando el programa lo solicite.

## Ejemplo de salida

```
Mover disco 1 de A a C
Mover disco 2 de A a B
Mover disco 1 de C a B
```

## Conceptos de programación aplicados

* Recursividad
* Estructuras de datos
* Pilas
* Algoritmos clásicos

## Autor

Proyecto desarrollado como práctica de **Estructuras de Datos y Algoritmos**.
