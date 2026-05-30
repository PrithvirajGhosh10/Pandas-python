import pandas as pd
df=pd.read_csv("data.csv")
group=df.groupby("type1")
print(group["height"].mean())
'''
type1
Bug            1.578947
Electric       1.477778
Electricity    1.050000
Fire           1.384211
Grass          1.322222
Ground         1.555556
Normal         1.257895
Poison         1.357895
Water          1.500000
Name: height, dtype: float64
'''

print(group["height"].sum())
print(group["height"].min())
print(group["height"].max())
print(group["height"].count())
