import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("unemployment.csv")
print(data.head())
print(data.isnull().sum())

data.columns= ["States","Date","Frequency", "Estimated Unemployment Rate","Estimated Employed","Estimated Labour Participation Rate","Region","longitude","latitude"]

plt.style.use('seaborn-whitegrid')# coorelation ghraph
plt.figure(figsize=(12, 10))
sns.heatmap(data.corr())
plt.show()

plt.title("Indian Unemployment") #no of employes count
sns.histplot(x="Estimated Employed", hue="Region", data=data)
plt.show()

plt.figure(figsize=(12, 10)) # unemployment rate according to different regions of India:
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Unemployment Rate", hue="Region", data=data)
plt.show()

