# 🏢 Sistema de Gestión de Tareas Enterprise

Simulador avanzado de colas prioritarias desarrollado en Python con interfaz gráfica.
Permite gestionar tareas normales y críticas, visualizar métricas en tiempo real y analizar el rendimiento del sistema.

---

## 🚀 Características principales

* 📋 Gestión de tareas normales (cola FIFO)
* ⚡ Gestión de tareas críticas (bicola con prioridad)
* 📊 Métricas en tiempo real:

  * Tareas en cola
  * Tareas completadas
  * Tiempo promedio de ejecución
  * Rendimiento del sistema
* 📈 Gráficas dinámicas con Matplotlib
* 🖥️ Interfaz profesional con Tkinter
* ⏱ Simulación de ejecución de tareas

---

## 🧠 Funcionamiento del sistema

El sistema utiliza dos estructuras principales:

* **Cola normal (FIFO)** → procesa tareas en orden de llegada
* **Bicola crítica** → inserta tareas al inicio (mayor prioridad)

### 🔄 Flujo de ejecución:

1. Se agregan tareas (normales o críticas)
2. Se inicia la simulación
3. El sistema ejecuta primero las tareas críticas
4. Luego procesa las tareas normales
5. Se actualizan métricas y gráficas en tiempo real

---

## 🛠️ Tecnologías utilizadas

* Python 3
* Tkinter (interfaz gráfica)
* Matplotlib (gráficas)
* NumPy (cálculos)
* Collections (deque)

---

## 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/tu-repo.git
```

2. Instala dependencias:

```bash
pip install matplotlib numpy
```

3. Ejecuta el programa:

```bash
python main.py
```

---

## 🎮 Uso

* ➕ Agregar tareas normales o críticas
* ▶ Iniciar simulación
* 🎲 Generar tareas automáticamente
* ⏹ Detener ejecución
* 🔄 Reiniciar sistema

---

## 📊 Métricas disponibles

* Número de tareas en cola
* Tareas completadas
* Tiempo promedio de ejecución
* Throughput (tareas/segundo)
* Utilización del sistema (%)

---

## ⚠️ Notas técnicas

* Se utiliza `after()` en lugar de `threading` para evitar bloqueos en la interfaz
* Tkinter no es thread-safe, por lo que la ejecución se maneja por eventos
* El sistema simula tiempos de ejecución aleatorios

---

## 👨‍💻 Autor
Gomez Ek Adolfo Rene
Proyecto desarrollado como simulador académico de estructuras de datos y sistemas de colas.

---

## 📌 Posibles mejoras

* Exportar reportes
* Guardar historial de tareas
* Implementar base de datos
* Versión web del sistema
* Multiusuario

---

## 🏁 Estado del proyecto

✅ Funcional
🔄 En mejora continua

---
