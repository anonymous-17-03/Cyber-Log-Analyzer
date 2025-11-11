# 🛡️ Cyber Log Analyzer

**Cyber Log Analyzer** es una herramienta sencilla escrita en **Python** que permite analizar registros (logs) de ciberseguridad en formato **CSV**, limpiarlos y generar visualizaciones informativas para identificar tendencias de ataques, puertos más vulnerados, tipos de amenazas y su severidad.

---

## 🚀 Características principales

✅ Limpieza y normalización de datos (manejo de nulos, tipos de datos y duplicados).  
✅ Conversión automática de fechas y horas para facilitar el análisis temporal.  
✅ Estadísticas descriptivas de los ataques (por tipo, severidad, puerto y hora).  
✅ Exportación del dataset limpio a **Excel (.xlsx)**.  
✅ Visualizaciones gráficas con **Matplotlib** y **Seaborn**:
- Gráfico de barras: cantidad de ataques por tipo.  
- Gráfico de barras: distribución de severidad.  
- Gráfico de barras (Top 10): puertos más atacados.  
- Gráfico de línea: evolución de ataques por hora del día.  
- Gráfico de pastel: distribución de puertos más vulnerados.  

---

## 🧩 Requisitos

Asegúrate de tener instalado **Python 3.8+** y las siguientes librerías:

```bash
pip install pandas numpy matplotlib seaborn openpyxl
````

---

## 📂 Estructura del proyecto

```
Cyber-Log-Analyzer/
│
├── cybersecurity_log.csv           # Archivo de entrada (log original)
├── cyber_log_analyzer.py           # Script principal de análisis
├── cybersecurity_log_cleaned.xlsx  # Archivo generado tras limpieza
└── README.md                       # Documentación del proyecto
```

---

## 🧠 Uso

1. Coloca tu archivo de logs en formato CSV con los siguientes campos mínimos (Puede usar el ejemplo `cybersecurity_log.csv`):

| FechaHora        | IP           | Puerto | TipoAtaque   | Severidad | Detalles              |
| ---------------- | ------------ | ------ | ------------ | --------- | --------------------- |
| 2025-11-10 13:42 | 192.168.1.23 | 22     | Fuerza Bruta | Alta      | Intento de acceso SSH |

2. Ejecuta el script:

```bash
python3 cyber_log_analyzer.py
```

3. El programa:

   * Cargará y limpiará los datos.
   * Mostrará un resumen estadístico en consola.
   * Exportará el dataset limpio a `cybersecurity_log_cleaned.xlsx`.
   * Generará automáticamente **5 gráficos interactivos**.

---

## 📊 Ejemplos de análisis generados

* **Tipos de ataque:** visualiza qué amenazas son más frecuentes.
* **Severidad:** determina la gravedad de los incidentes detectados.
* **Puertos más atacados:** descubre cuáles son los vectores de ataque más comunes.
* **Evolución temporal:** observa en qué horas del día ocurren más ataques.
* **Distribución por puerto:** compara gráficamente las principales rutas de ataque.

---

## 🧰 Tecnologías utilizadas

* **Python 3**
* **Pandas** – Limpieza y análisis de datos.
* **NumPy** – Operaciones estadísticas.
* **Matplotlib** – Visualización básica.
* **Seaborn** – Visualización avanzada y estética.
* **OpenPyXL** – Exportación a Excel.

---

## 🧑‍💻 Autor

**Víctor García**
🔗 GitHub: [anonymous-17-03](https://github.com/anonymous-17-03)

---

> 💬 *"Analiza tus logs, entiende tus ataques y protege tu red."*
