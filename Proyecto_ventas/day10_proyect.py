# Cargar librerías
import pandas as pd
import matplotlib.pyplot as plt

# Crear datos
datos = {
    "Producto": ["Aceite", "Filtro", "Bujia", "Aceite", "Filtro", "Bateria", "Bujia", "Aceite", "Filtro", "Aceite"],
    "Precio": [250, 180, 90, 260, 175, 1800, 95, 240, 200, 255],
    "Cantidad": [2, 4, 10, 1, 3, 1, 8, 2, 5, 3],
    "Ciudad": ["Saltillo", "Saltillo", "Monterrey", "Monterrey", "Saltillo", "Torreon", "Torreon", "Saltillo", "Monterrey", "Torreon"]
}

df = pd.DataFrame(datos)

# Calcular totales
df["Total"] = df["Precio"] * df["Cantidad"]

# Agrupar por producto
ventas_producto = df.groupby("Producto")["Total"].sum()
# Agrupar por ciudad
ventas_ciudad = df.groupby("Ciudad")["Total"].sum()
precio_promedio_producto = df.groupby("Producto")["Precio"].mean()

print("TABLA COMPLETA")
print(df)

print("\nVENTAS TOTALES POR PRODUCTO")
print(ventas_producto)

print("\nVENTAS TOTALES POR CIUDAD")
print(ventas_ciudad)

print("\nPRECIO PROMEDIO POR PRODUCTO")
print(precio_promedio_producto)

# Graficar resultados
ventas_producto.plot(kind="bar")
plt.title("Ventas totales por producto")
plt.xlabel("Producto")
plt.ylabel("Total vendido")
plt.tight_layout()
plt.show()

ventas_ciudad.plot(kind="bar")
plt.title("Ventas totales por ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Total vendido")
plt.tight_layout()
plt.show()

precio_promedio_producto.plot(kind="bar")
plt.title("Precio promedio por producto")
plt.xlabel("Producto")
plt.ylabel("Precio promedio")
plt.tight_layout()
plt.show()

print("\n=== RESUMEN FINAL ===")
print("Producto con mayor ingreso:", ventas_producto.idxmax())
print("Ciudad con mayores ventas:", ventas_ciudad.idxmax())
print("Producto con mayor precio promedio:", precio_promedio_producto.idxmax())