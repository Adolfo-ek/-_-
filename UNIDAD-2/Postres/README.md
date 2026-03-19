# 🍰 Sistema de Gestión de Postres

Este proyecto es una aplicación en Python que permite gestionar un conjunto de postres y sus ingredientes utilizando estructuras de datos (arreglos y listas).

---

## 📌 Descripción

El programa maneja un arreglo llamado `POSTRES`, donde cada elemento contiene:

* Nombre del postre
* Lista de ingredientes asociados

Los postres se mantienen **ordenados alfabéticamente** y el sistema permite realizar operaciones básicas de gestión.

---

## ⚙️ Funcionalidades

El sistema incluye las siguientes operaciones:

### a) Consultar ingredientes

Permite ingresar el nombre de un postre y muestra todos sus ingredientes.

### b) Agregar ingredientes

Permite añadir nuevos ingredientes a un postre existente, evitando duplicados.

### c) Eliminar ingredientes

Permite eliminar un ingrediente específico de un postre.

### d) Dar de alta un postre

Permite registrar un nuevo postre junto con todos sus ingredientes.

### e) Dar de baja un postre

Elimina un postre junto con todos sus ingredientes del sistema.

---

## 🧠 Estructuras de Datos Utilizadas

* **Listas (arreglos)** para almacenar los postres
* **Diccionarios** para representar cada postre
* **Listas internas** para los ingredientes

Ejemplo de estructura:

```python
POSTRES = [
    {"nombre": "Flan", "ingredientes": ["leche", "huevo", "azúcar"]},
    {"nombre": "Pastel", "ingredientes": ["harina", "huevo", "azúcar"]}
]
```

---

## 🛡️ Validaciones Implementadas

El programa contempla distintos casos para evitar errores:

* Verifica si el postre existe antes de operar
* Evita agregar ingredientes duplicados
* Controla eliminación de elementos inexistentes
* Maneja listas vacías
* Mantiene el orden alfabético automáticamente

---

## ▶️ Ejecución

1. Asegúrate de tener Python instalado
2. Ejecuta el archivo:

```bash
python nombre_del_archivo.py
```

3. Usa el menú interactivo para seleccionar una opción

---

## 📋 Menú del Sistema

* Mostrar ingredientes
* Agregar ingrediente
* Eliminar ingrediente
* Agregar postre
* Eliminar postre
* Salir

---

## 🎯 Objetivo Académico

Este proyecto tiene como finalidad aplicar conceptos de:

* Estructuras de datos
* Manejo de listas
* Búsqueda y validación
* Organización de información

---

## 🚀 Posibles Mejoras

* Interfaz gráfica (GUI)
* Implementación con clases (Programación Orientada a Objetos)
* Persistencia de datos (archivos o base de datos)
* Búsqueda más eficiente (binaria)

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica de estructuras de datos.
