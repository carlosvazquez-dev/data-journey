import pandas as pd

"""datos = {

    "Nombre": ["Carlos", "Ana", "Luis", None, "Pedro"],
    "Edad": [28, 25, None, 32, 40],
    "Ciudad": ["Saltillo", "Monterrey", "Torreón", "Saltillo", None]
}"""


datos = {

    "Producto": ["Computadora", "Antena", "Lámpara", None, "Pantalla", None, "Ropero"],
    "Precio": [28000, 250, None, 3200, 4000, 7000, None],
    "Cantidad": [1, 35, 75, 64, 11, None, None]
}

df = pd.DataFrame(datos)

print("DATOS ORIGINALES")
print(df)
print()
print("FILAS CON DATOS FALTANTES")
print(df.isnull())
print()
print("CANTIDAD DE DATOS FALTANTES POR COLUMNA")
print(df.isnull().sum())

df_limpio = df.dropna()

print()
print("DATOS LIMPIOS")
print(df_limpio)

df2 = pd.DataFrame(datos)

df2["Producto"] = df2["Producto"].fillna("Desconocido")
df2["Precio"] = df2["Precio"].fillna(df2["Precio"].mean())
df2["Cantidad"] = df2["Cantidad"].fillna(df2["Cantidad"].mean())

print()
print("DATOS RELLENADOS")
print(df2)

print()
print("PROMEDIO DE PRECIOS")
print(df2["Precio"].mean())

"""print()
print("CIUDADES UNICAS")
print(df2["Ciudad"].unique())"""

