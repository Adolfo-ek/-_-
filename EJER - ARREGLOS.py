DEPARTAMENTOS = ["Ropa", "Deportes", "Juguetería"]
MESES = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

class VentasMensuales:
    def __init__(self):
        self.ventas = [[0 for _ in range(12)] for _ in range(3)]

    # ---------- VISUALIZAR TABLA ----------
    def visualizar_tabla(self):
        print("\nVENTAS MENSUALES POR DEPARTAMENTO\n")
        print(f"{'Departamento':<15}", end="")
        for mes in MESES:
            print(f"{mes:<12}", end="")
        print("\n" + "-" * 160)

        for i, depto in enumerate(DEPARTAMENTOS):
            print(f"{depto:<15}", end="")
            for monto in self.ventas[i]:
                print(f"${monto:<11.2f}", end="")
            print()
        print()

    # ---------- INSERTAR / MODIFICAR ----------
    def insertar_modificar(self):
        depto = input("Departamento (Ropa / Deportes / Juguetería): ")
        mes = input("Mes: ")
        monto = float(input("Monto de la venta: "))

        try:
            fila = DEPARTAMENTOS.index(depto)
            columna = MESES.index(mes)
            self.ventas[fila][columna] = monto
            print("✔ Venta registrada o modificada correctamente")
        except ValueError:
            print("❌ Departamento o mes inválido")

    # ---------- BUSCAR ----------
    def buscar_venta(self):
        depto = input("Departamento: ")
        mes = input("Mes: ")

        try:
            fila = DEPARTAMENTOS.index(depto)
            columna = MESES.index(mes)
            print(f"🔍 Venta encontrada: ${self.ventas[fila][columna]:.2f}")
        except ValueError:
            print("❌ Departamento o mes inválido")

    # ---------- ELIMINAR ----------
    def eliminar_venta(self):
        depto = input("Departamento: ")
        mes = input("Mes: ")

        try:
            fila = DEPARTAMENTOS.index(depto)
            columna = MESES.index(mes)
            self.ventas[fila][columna] = 0
            print("🗑 Venta eliminada correctamente")
        except ValueError:
            print("❌ Departamento o mes inválido")


# ---------- MENÚ PRINCIPAL ----------
def menu():
    sistema = VentasMensuales()

    while True:
        print("\n--- MENÚ DE VENTAS ---")
        print("1. Insertar / Modificar venta")
        print("2. Buscar venta")
        print("3. Eliminar venta")
        print("4. Visualizar tabla")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.insertar_modificar()
        elif opcion == "2":
            sistema.buscar_venta()
        elif opcion == "3":
            sistema.eliminar_venta()
        elif opcion == "4":
            sistema.visualizar_tabla()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("❌ Opción inválida")


menu()


