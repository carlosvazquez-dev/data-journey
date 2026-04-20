import pandas as pd

datos = {
    "Producto": ["Aceite","Aceite", "Filtro", "Bujia", "Aceite", "Filtro", "Bateria", "Bujia", "Aceite", "Filtro", "Aceite"],
    "Precio": ["250", "250", "90", "260", None, "1800", "95", "240", "200", "255", None],
    "Cantidad": [2, 2, 10, 1, 3, 1, 8, 2, 5, 3, 7],
    "Ciudad": ["Saltillo","Saltillo", "Saltillo", "Monterrey", "Monterrey", " Saltillo", "Torreon", "Torreon", "Saltillo", "Monterrey", None]
}

df = pd.DataFrame(datos)

print("TABLA ORIGINAL")
print(df)

print("\nFALTANTES POR COLUMNA")
print(df.isnull().sum())

print("\nDUPLICADOS")
print(df.duplicated().sum())

df["Precio"] = pd.to_numeric(df["Precio"], errors="coerce")
df["Precio"] = df["Precio"].fillna(df["Precio"].mean())
df["Ciudad"] = df["Ciudad"].fillna("Desconocida")
df["Producto"] = df["Producto"].str.strip()
df["Ciudad"] = df["Ciudad"].str.strip()
df = df.drop_duplicates()

print("\nTABLA LIMPIA")
print(df)

df["Total"] = df["Precio"] * df["Cantidad"]

print("\nTABLA CON TOTAL")
print(df)

print("\nTOTAL POR PRODUCTO")
print(df.groupby("Producto")["Total"].sum())

print("\nTOTAL POR CIUDAD")
print(df.groupby("Ciudad")["Total"].sum())