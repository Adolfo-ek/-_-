# MyLinkedList - Implementación de Lista Enlazada

## 📌 Descripción

Este proyecto consiste en la implementación de una **Lista Enlazada (Linked List)** en Python sin utilizar librerías externas.

Forma parte de la actividad:

**ADA4 - Implementar Linked List**
Unidad 3 - Estructuras Lineales

El objetivo es comprender cómo funcionan internamente las estructuras dinámicas de datos.

---

## 🧠 Concepto

Una **Linked List** es una estructura de datos lineal donde cada elemento (nodo) contiene:

* Un valor (data)
* Una referencia al siguiente nodo

A diferencia de los arreglos, no ocupa memoria contigua.

---

## 🏗️ Estructura del Proyecto

* `Node`: Representa un nodo de la lista
* `MyLinkedList`: Clase principal que gestiona la lista

---

## ⚙️ Funcionalidades Implementadas

✔ Insertar al inicio
✔ Insertar al final
✔ Insertar en posición específica
✔ Eliminar un elemento
✔ Buscar un elemento
✔ Mostrar la lista

---

## 🚀 Ejemplo de Uso

```python
lista = MyLinkedList()

lista.insert_at_beginning(10)
lista.insert_at_end(20)
lista.insert_at_end(30)
lista.insert_at_position(15, 1)

lista.display()
```

Salida esperada:

```
10 -> 15 -> 20 -> 30
```

---

## 🔍 Métodos

### insert_at_beginning(data)

Inserta un elemento al inicio de la lista.

### insert_at_end(data)

Inserta un elemento al final.

### insert_at_position(data, position)

Inserta un elemento en una posición específica.

### delete(key)

Elimina un elemento por valor.

### search(key)

Busca un elemento y devuelve su posición.

### display()

Muestra todos los elementos de la lista.

---

## 📚 Conclusión

Esta implementación permite entender el funcionamiento interno de las listas enlazadas, incluyendo la manipulación de nodos y referencias.

Es una base fundamental para estructuras de datos más avanzadas como:

* Pilas (Stacks)
* Colas (Queues)
* Árboles

---

## 👨‍💻 Autor

Proyecto desarrollado como parte de práctica académica en estructuras de datos.
