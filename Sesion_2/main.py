# Importa la libreria Pandas, fundamental para analisis de datos
import pandas as pd
# Define la ruta del archivo CSV que contiene los datos
# Si el archivo esta en el mismo directorio, basta con poner el nombre del archivo
path = 'estaciones_viento.csv'

retail_data = pd.read_csv(path, encoding='latin1')

print(type(retail_data))
print(retail_data)
