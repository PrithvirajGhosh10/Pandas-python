import pandas as pd
df=pd.read_csv("data.csv")
#SELECTION BY CLOUMN
print(df["name"].to_string()) #will print all names
print(df["height"].to_string())
print(df["weight"].to_string())
print(df[["name","weight","height"]].to_string())

