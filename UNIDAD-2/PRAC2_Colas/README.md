# Sistema de Colas para Atención de Clientes

## Descripción

Este proyecto consiste en una aplicación que permite **gestionar colas de atención para una compañía de seguros**.
El sistema permite registrar clientes que llegan a solicitar un servicio y organizar su atención mediante el uso de **estructuras de datos tipo cola (Queue)**.

Cada cliente recibe un número y se coloca en la cola correspondiente. El personal de atención puede ir llamando a los clientes según la cola que desee atender.

Este programa fue desarrollado como parte de un ejercicio práctico para comprender el funcionamiento de **estructuras de datos dinámicas**.

---

## Características

* Agregar clientes a la cola
* Atender al siguiente cliente
* Eliminar clientes de la cola
* Visualizar los clientes en espera
* Limitar el número máximo de clientes en la cola
* Vaciar completamente la cola con un solo botón
* Interfaz simple y fácil de usar

---

## Estructura del Proyecto

El programa está compuesto principalmente por las siguientes clases:

### Nodo

Representa a cada cliente dentro de la cola.

Contiene:

* Información del cliente
* Referencia al siguiente nodo

### Cola

Implementa la lógica de la estructura de datos **cola (FIFO – First In, First Out)**.

Funciones principales:

* `agregar_cliente()`
* `atender_cliente()`
* `eliminar_cliente()`
* `mostrar_clientes()`
* `vaciar_cola()`

### Interfaz

Permite interactuar con el sistema mediante botones y opciones para gestionar la cola de clientes.

---

## Funcionamiento de la Cola

El sistema utiliza el principio **FIFO (First In, First Out)**:

El **primer cliente en llegar es el primero en ser atendido**.

Ejemplo:

Cliente 1 → Cliente 2 → Cliente 3

Si se atiende un cliente:

Cliente 2 → Cliente 3

---

## Tecnologías Utilizadas

* Python
* Programación Orientada a Objetos
* Estructuras de Datos (Colas)
* Interfaz gráfica básica

---

## Cómo ejecutar el programa

1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/tu-repositorio.git
```

2. Entrar a la carpeta del proyecto

```bash
cd tu-repositorio
```

3. Ejecutar el programa

```bash
python main.py
```

---

## Objetivo Académico

El objetivo de este proyecto es demostrar la implementación práctica de la estructura de datos **cola**, así como reforzar conceptos de:

* Programación orientada a objetos
* Manejo de estructuras dinámicas
* Organización de datos en memoria

---

## Autor

Desarrollado por **Adolfo**
Proyecto académico de programación.

---
