import pandas as pd

"""datos = {
   "Nombre": ["Carlos", "Ana", "Luis"],
   "Edad": [28, 25, 30],
   "Ciudad": ["Saltillo", "Monterrey", "Torreón"] #Esta parte del codico se usa para leer los datos desde la variable datos
   }

#df = pd.DataFrame(datos)

print(df)"""

#Esta otra parte se usa para llamar los datos desde un archivo csv
df_csv = pd.read_csv("personas.csv") 
print(df_csv)
print()
print(df_csv.head())
print()
print(df_csv["Nombre"])
print()
print(df_csv["Edad"].mean())



