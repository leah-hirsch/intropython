#!/usr/bin/env python
# coding: utf-8

# In[12]:


#question 2: read csv and calculate the stats (mean, median, std)
import pandas as pd

# Load the data
df_iris = pd.read_csv(url, header=None, names=column_names)
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

# Calculate statistics for sepal and petal dimensions'
sepal_petal_stats = df_iris[["sepal_length", "sepal_width", "petal_length", "petal_width"]].agg(["mean", "median", "std"])
print(sepal_petal_stats)




