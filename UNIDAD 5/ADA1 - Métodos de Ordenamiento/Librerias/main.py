# ============================================
# LIBRERÍA DE ESTRUCTURA DE DATOS
# SISTEMA PRINCIPAL
# ============================================

from internos.burbuja import bubble_sort
from internos.insercion import insertion_sort
from internos.seleccion import selection_sort
from internos.shellsort import shell_sort


# ============================================
# PRUEBAS GENERALES
# ============================================

if __name__ == "__main__":

    datos = [9, 4, 7, 1, 3]

    print("\n==============================")
    print(" LIBRERÍA ESTRUCTURA DE DATOS ")
    print("==============================")

    print("\nDatos originales:")
    print(datos)

    print("\nBubble Sort:")
    print(bubble_sort(datos))

    print("\nInsertion Sort:")
    print(insertion_sort(datos))

    print("\nSelection Sort:")
    print(selection_sort(datos))

    print("\nShell Sort:")
    print(shell_sort(datos))

    input("\nPresiona ENTER para cerrar...")