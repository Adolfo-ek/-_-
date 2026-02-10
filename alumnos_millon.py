import time
import hashlib

# -------------------------------
# Configuración extrema
# -------------------------------
NUM_ALUMNOS = 100_000_000
NUM_MATERIAS = 100_000_000

# -------------------------------
# Simulación de acceso O(1)
# -------------------------------
def obtener_calificacion(alumno, materia):
    # Convertimos la combinación a un hash
    clave = f"{alumno}-{materia}".encode()
    hash_val = hashlib.sha256(clave).hexdigest()

    # Convertimos el hash a un número entre 0 y 10
    return int(hash_val[:2], 16) % 11


# -------------------------------
# Entrada del usuario
# -------------------------------
alumno = int(input(f"Ingresa el alumno (0 a {NUM_ALUMNOS - 1}): "))
materia = int(input(f"Ingresa la materia (0 a {NUM_MATERIAS - 1}): "))

# -------------------------------
# Medición de tiempo
# -------------------------------
inicio = time.time()
calificacion = obtener_calificacion(alumno, materia)
fin = time.time()

# -------------------------------
# Resultado
# -------------------------------
print("\nRESULTADO (MATRIZ NO ALMACENADA)")
print("--------------------------------")
print(f"Alumno: {alumno}")
print(f"Materia: Materia_{materia + 1}")
print(f"Calificación simulada: {calificacion}")
print(f"Tiempo de ejecución: {fin - inicio:.10f} segundos")
