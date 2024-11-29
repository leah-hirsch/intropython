#starting question 4 for PCA graph, first i must scale the data, and get rid of the last column bc it is a string not a float
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the data
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
iris_data = pd.read_csv(url, header=None, names=column_names)

df_iris_drop_species=iris_data.drop(columns=['species'])

scaler = StandardScaler()
df_iris_scaled= scaler.fit_transform(df_iris_drop_species)

pca = PCA(n_components=2)
result = pca.fit_transform(df_iris_scaled)

sns.scatterplot(x=result[:,0], y=result[:,1], hue=iris_data['species'])
plt.savefig('pca_iris.pdf')
