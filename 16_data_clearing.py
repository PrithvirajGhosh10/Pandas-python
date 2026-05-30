#2. fill the velue with none
import pandas as pd
df=pd.read_csv("data.csv")
df=df.fillna({"type2":"None"}) 
print(df.to_string())

# 3.fix inconsistent values
df["type1"]=df["type1"].replace({"Grass":"GRASS"})
print(df.to_string())

df["type1"]=df["type1"].replace({"Grass":"GRASS",
                                 "Fire":"FIRE",
                                 "Water":"WATER"})
print(df.to_string())

# 4. Standardize text
df["name"]=df["name"].str.lower()
print(df.to_string())

# 5. fix data types

df["legendary"]=df["legendary"].astype(bool)
print(df.to_string())

# 6. remove duplicate values
df=df.drop_duplicates()
print(df.to_string())
