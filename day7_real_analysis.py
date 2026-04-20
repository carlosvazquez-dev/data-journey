import pandas as pd

df = pd.read_csv("ventas_reales.csv")

print("DATOS:")
print(df)

print("\nINFO:")
print(df.info())

print("\nRESUMEN:")
print(df.describe())

df["Total"] = df["Precio"] * df["Cantidad"]

print("\nDATOS CON TOTAL:")
print(df)

print("\nVENTAS TOTALES POR PRODUCTO:")
ventas_producto = df.groupby("Producto")["Total"].sum()
print(ventas_producto)

print("\nVENTAS POR CIUDAD:")
ventas_ciudad = df.groupby("Ciudad")["Total"].sum()
print(ventas_ciudad)

print("\nPRODUCTO MÁS VENDIDO:")
print(ventas_producto.idxmax())

print("\nCIUDAD CON MÁS VENTAS:")
print(ventas_ciudad.idxmax())