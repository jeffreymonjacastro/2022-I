import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Trabajar con datos csv
dataset = pd.read_csv("Pokemon2.csv")

# Eliminar algunas columnas
dataset.drop(['#', 'Type 1', 'Type 2', 'Generation', 'Legendary'],1, inplace = True)

# Cluster para agrupar
km = KMeans(n_clusters = 3)

# Variable con todos los valores de grupos de cluster
cluster = km.fit_predict(dataset[['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']])

# Agregar la columna nueva (Cluster)
dataset['Cluster'] = cluster

print(dataset)