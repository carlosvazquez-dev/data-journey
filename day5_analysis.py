import pandas as pd
import matplotlib.pyplot as plt

datos = {
    "Producto": ["Aceite", "Filtro", "Bujía", "Aceite", "Filtro", "Batería", "Bujía", "Aceite"],
    "Precio": [250, 180, 90, 260, 175, 1800, 95, 240],
    "Cantidad": [2, 4, 10, 1, 3, 1, 8, 2],
    "Ciudad": ["Saltillo", "Saltillo", "Monterrey", "Monterrey", "Saltillo", "Torreón", "Torreón", "Saltillo"]
}

df = pd.DataFrame(datos)

print("TABLA ORIGINAL")
print(df)

print("\nPRODUCTOS CON PRECIO MAYOR A 200")
print(df[df["Precio"] > 200])

print("\nORDENADO POR PRECIO")
print(df.sort_values(by="Precio", ascending=False))

print("\nVENTAS TOTALES POR PRODUCTO")
ventas = df.groupby("Producto")["Cantidad"].sum()
print(ventas)

print("\nPROMEDIO DE PRECIO POR PRODUCTO")
promedio_precio = df.groupby("Producto")["Precio"].mean()
print(promedio_precio)

ventas.plot(kind="bar")
plt.title("Cantidad total vendida por producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.show()