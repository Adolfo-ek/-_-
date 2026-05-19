# Método de Mezcla Equilibrada

## Descripción

La mezcla equilibrada es un método de ordenamiento externo que divide los datos en bloques equilibrados para posteriormente fusionarlos de forma ordenada.

Es utilizado en procesamiento de archivos grandes.

---

## Funcionamiento

1. Dividir los datos en bloques pequeños.
2. Ordenar cada bloque.
3. Fusionar los bloques ordenados.
4. Repetir hasta obtener una sola estructura ordenada.

---

## Complejidad

- Tiempo: O(n log n)

---

## Ventajas

- Muy eficiente en archivos grandes.
- Reduce el tiempo de procesamiento.
- Ideal para memoria secundaria.

---

## Desventajas

- Requiere manejo adicional de archivos.
- Más complejo que métodos internos.
