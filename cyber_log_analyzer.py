import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================
# CONFIGURACIÓN GENERAL
# ============================
sns.set(style="whitegrid", font_scale=1.15)
plt.rcParams["axes.edgecolor"] = "0.7"
plt.rcParams["axes.linewidth"] = 1
plt.rcParams["figure.facecolor"] = "white"

# ============================
# CARGA Y LIMPIEZA DE DATOS
# ============================
df = pd.read_csv("cybersecurity_log.csv")

print("\n--- Información del Dataset ---")
print(df.info())
print("\n--- Primeras Filas ---")
print(df.head())

# Limpieza de valores nulos
df.fillna({
    "IP": "Desconocido",
    "Puerto": 0,
    "TipoAtaque": "Desconocido",
    "Severidad": "Desconocido",
    "Detalles": "Sin detalles"
}, inplace=True)

# Conversión de tipos
df["FechaHora"] = pd.to_datetime(df["FechaHora"], errors="coerce")
df["Puerto"] = df["Puerto"].astype(int)

# Normalización de texto
df["TipoAtaque"] = df["TipoAtaque"].astype(str).str.strip().str.title()
df["Severidad"] = df["Severidad"].astype(str).str.strip().str.title()

# Eliminar duplicados
df.drop_duplicates(inplace=True)

# ============================
# ANÁLISIS EXPLORATORIO
# ============================
print("\n--- Resumen Estadístico ---")
print(df.describe(include="all"))

# Agrupaciones útiles
ataques_por_tipo = df["TipoAtaque"].value_counts()
ataques_por_severidad = df["Severidad"].value_counts()
ataques_por_puerto = df["Puerto"].value_counts()

print("\n--- Ataques por Tipo ---")
print(ataques_por_tipo)
print("\n--- Ataques por Severidad ---")
print(ataques_por_severidad)

# Exportar dataset limpio
df.to_excel("cybersecurity_log_cleaned.xlsx", index=False)
print("\n✅ Archivo limpio exportado como 'cybersecurity_log_cleaned.xlsx'")

# ============================
# VISUALIZACIONES
# ============================

# 1️⃣ Gráfico de barras - Tipos de ataques
plt.figure(figsize=(12, 6))
colores_tipo = sns.color_palette("tab10", len(ataques_por_tipo))
sns.countplot(
    x="TipoAtaque", data=df,
    order=df["TipoAtaque"].value_counts().index,
    hue="TipoAtaque", palette=colores_tipo, legend=False
)
plt.title("Cantidad de Ataques por Tipo", fontsize=15)
plt.xlabel("Tipo de Ataque")
plt.ylabel("Cantidad de Incidentes")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# 2️⃣ Gráfico de barras - Severidad
plt.figure(figsize=(7, 4))
colores_severidad = sns.color_palette("Set1", len(ataques_por_severidad))
sns.countplot(
    x="Severidad", data=df,
    order=df["Severidad"].value_counts().index,
    hue="Severidad", palette=colores_severidad, legend=False
)
plt.title("Distribución de Severidad de los Ataques", fontsize=15)
plt.xlabel("Nivel de Severidad")
plt.ylabel("Cantidad de Incidentes")
plt.tight_layout()
plt.show()

# 3️⃣ Gráfico de barras - Puertos más atacados (Top 10)
top_puertos = df["Puerto"].value_counts().head(10)
plt.figure(figsize=(10, 5))
colores_puertos = sns.color_palette("viridis", len(top_puertos))
sns.barplot(
    x=top_puertos.index, y=top_puertos.values,
    hue=top_puertos.index, palette=colores_puertos, legend=False
)
plt.title("Puertos Más Atacados (Top 10)", fontsize=15)
plt.xlabel("Puerto")
plt.ylabel("Incidentes Detectados")
plt.tight_layout()
plt.show()

# 4️⃣ Línea temporal - Evolución de ataques por hora
ataques_por_hora = df.groupby(df["FechaHora"].dt.hour).size()
plt.figure(figsize=(10, 5))
plt.plot(
    ataques_por_hora.index, ataques_por_hora.values,
    marker="o", linewidth=2.2, color="#1f77b4"
)
plt.title("Evolución de Ataques por Hora del Día", fontsize=15)
plt.xlabel("Hora del Día")
plt.ylabel("Cantidad de Ataques")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# 5️⃣ Gráfico de pastel - Distribución de Puertos (Top 6)
puertos_top = df["Puerto"].value_counts().head(6)
colores_pie = sns.color_palette("cool", len(puertos_top))
plt.figure(figsize=(7, 7))
plt.pie(
    puertos_top.values,
    labels=puertos_top.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=colores_pie,
    textprops={"fontsize": 11, "color": "black"}
)
plt.title("Distribución de Puertos Más Atacados", fontsize=15, pad=20)
plt.axis("equal")
plt.tight_layout()
plt.show()
