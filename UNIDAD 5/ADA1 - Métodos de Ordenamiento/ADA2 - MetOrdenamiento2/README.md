# README - Ordenador Visual de Datos

## Descripción General

**Ordenador Visual de Datos** es una aplicación de escritorio desarrollada en **Python** utilizando la librería **Tkinter**. Su propósito principal es permitir al usuario ingresar listas de números enteros, aplicar distintos algoritmos de ordenamiento y visualizar los resultados de forma rápida e intuitiva.

Además de ordenar datos, el sistema muestra estadísticas como tiempo de ejecución, cantidad de elementos procesados y método utilizado, convirtiéndolo en una herramienta útil tanto para aprendizaje académico como para prácticas de programación.

---

# Objetivos del Proyecto

* Comprender el funcionamiento de algoritmos clásicos de ordenamiento.
* Comparar tiempos de ejecución entre distintos métodos.
* Aplicar interfaces gráficas con Tkinter.
* Integrar lógica algorítmica con diseño visual.
* Facilitar el aprendizaje interactivo de estructuras de datos.

---

# Tecnologías Utilizadas

* **Python 3**
* **Tkinter** (Interfaz gráfica)
* **time** (Medición de tiempos)
* **random** (Generación de datos aleatorios)

---

# Algoritmos Implementados

## 1. Bubble Sort

Compara elementos consecutivos e intercambia posiciones hasta ordenar completamente.

**Ventajas:**

* Fácil de entender.
* Ideal para fines educativos.

**Complejidad:**

* O(n²)

---

## 2. Selection Sort

Busca el valor mínimo del arreglo y lo coloca en su posición correcta.

**Ventajas:**

* Menos intercambios que Bubble Sort.

**Complejidad:**

* O(n²)

---

## 3. Insertion Sort

Inserta cada elemento en la posición adecuada dentro de la parte ya ordenada.

**Ventajas:**

* Muy eficiente en listas pequeñas o casi ordenadas.

**Complejidad:**

* O(n²)

---

## 4. Merge Sort

Divide la lista en partes pequeñas y luego las fusiona ordenadamente.

**Ventajas:**

* Mucho más eficiente en grandes volúmenes de datos.

**Complejidad:**

* O(n log n)

---

# Funcionalidades Principales

## Entrada de Datos

El usuario puede:

* Escribir números manualmente.
* Separarlos por espacios o comas.
* Generar datos aleatorios automáticamente.

## Estadísticas en Tiempo Real

La aplicación muestra:

* Tiempo de ejecución en milisegundos.
* Número total de elementos.
* Método aplicado.

## Visualización

Se presentan tres áreas:

* Arreglo original.
* Arreglo ordenado.
* Bitácora de acciones.

## Controles

* **ORDENAR** → Ejecuta el algoritmo seleccionado.
* **LIMPIAR** → Reinicia toda la interfaz.
* **SALIR** → Cierra la aplicación.

---

# Estructura del Código

```python
bubble_sort()
selection_sort()
insertion_sort()
merge_sort()
fusionar()

class OrdenadorApp(tk.Tk):
```

El código está organizado separando:

* Lógica de algoritmos.
* Diseño visual.
* Eventos y acciones del usuario.

---

# Cómo Ejecutarlo

## Requisitos

Tener instalado Python 3.

## Ejecutar

```bash
python nombre_archivo.py
```

---

# Uso del Programa

1. Ingresar cantidad de números o escribir datos manualmente.
2. Elegir algoritmo de ordenamiento.
3. Presionar **ORDENAR**.
4. Observar resultados y estadísticas.

---

# Ventajas del Proyecto

* Interfaz moderna y amigable.
* Código organizado y legible.
* Ideal para exposiciones escolares.
* Excelente práctica de estructuras de datos.
* Fácil expansión futura.

---

# Posibles Mejoras Futuras

* Animación paso a paso del ordenamiento.
* Soporte para números decimales.
* Exportar resultados a Excel o TXT.
* Comparación simultánea entre algoritmos.
* Gráficas de rendimiento.

---

# Autoría

Proyecto académico desarrollado para la materia de **Estructura de Datos**.

---

# Conclusión

Este programa demuestra cómo los algoritmos clásicos pueden integrarse con interfaces modernas para generar herramientas educativas útiles. Además de ordenar datos, permite analizar rendimiento, comparar métodos y fortalecer conocimientos prácticos de programación.
