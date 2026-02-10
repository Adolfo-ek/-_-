Simulación de Calificaciones de Alumnos (Acceso O(1))
Descripción del proyecto

Este proyecto simula el acceso a una matriz de calificaciones de gran tamaño sin almacenarla físicamente en memoria. A través de una función determinística basada en hashing, se obtiene una calificación para cualquier combinación de alumno y materia en tiempo constante.

El sistema está diseñado con fines educativos para ilustrar conceptos de estructuras de datos, eficiencia algorítmica y optimización de recursos.

Objetivo

Simular una matriz de alumnos y materias de dimensiones extremadamente grandes.

Obtener calificaciones sin almacenar la matriz completa.

Demostrar el acceso en tiempo constante (O(1)).

Medir el tiempo de ejecución del proceso.

Enfoque del sistema

En lugar de utilizar una matriz tradicional, el programa genera una calificación a partir de la combinación alumno–materia mediante una función hash. Este método garantiza que una misma entrada produzca siempre el mismo resultado, sin depender del tamaño total de la matriz.

Tecnologías utilizadas

Python 3

Librerías estándar del lenguaje
Funcionamiento general

Se define el número total de alumnos y materias.

El usuario ingresa el identificador del alumno y de la materia.

El sistema calcula una calificación simulada.

Se muestra el resultado junto con el tiempo de ejecución.

Ventajas del enfoque

No requiere almacenamiento de grandes volúmenes de datos.

Tiempo de acceso constante.

Uso eficiente de memoria.

Adecuado para simulaciones y prácticas académicas.

Limitaciones

Las calificaciones generadas no representan datos reales.

El sistema no almacena información de forma persistente.

No sustituye a un sistema académico real.

Autor
Adolfo-Rene-Gomez-Ek_3SA
Proyecto desarrollado con fines académicos para la materia de Estructura de Datos.
Autor

Proyecto desarrollado con fines académicos para la materia de Estructura de Datos.
