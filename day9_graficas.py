import pandas as pd
import matplotlib.pyplot as plt

datos = {
    "Producto": ["Aceite", "Filtro", "Bujia", "Aceite", "Filtro", "Bateria", "Bujia", "Aceite", "Filtro", "Aceite"],
    "Precio": [250, 180, 90, 260, 175, 1800, 95, 240, 200, 255],
    "Cantidad": [2, 4, 10, 1, 3, 1, 8, 2, 5, 3],
    "Ciudad": ["Saltillo", "Saltillo", "Monterrey", "Monterrey", "Saltillo", "Torreon", "Torreon", "Saltillo", "Monterrey", "Torreon"]
}

df = pd.DataFrame(datos)

df["Total"] = df["Precio"] * df["Cantidad"]

ventas_producto = df.groupby("Producto")["Total"].sum()
ventas_ciudad = df.groupby("Ciudad")["Total"].sum()
ventasprom_producto = df.groupby("Producto")["Precio"].mean().round(2)

print("VENTAS POR PRODUCTO")
print(ventas_producto)

print("\nVENTAS POR CIUDAD")
print(ventas_ciudad)

print("\nVENTAS PROMEDIO POR PRODUCTO")
print(ventasprom_producto)

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

ventasprom_producto.plot(kind="bar")
plt.title("Ventas promedio por producto")
plt.xlabel("Producto")
plt.ylabel("Precio Promedio")
plt.tight_layout()
plt.show()


