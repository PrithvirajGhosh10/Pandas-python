# Data cleaning = the process of fixing/removing:
#                 incomplete, incorrect, or irrelevant data.
#                 ~75% of work done with Pandas is data cleaning
import pandas as pd
df=pd.read_csv("data.csv")

# 1. Drop irrelevant columns
df=df.drop(columns=["legendary","no"])
print(df)
#handeling missing data
df=df.dropna(subset=["type2"]) #dropna=drop not available
print(df.to_string)

#fill the velue with none
df=df.fillna({"type2":"None"}) 
print(df.to_string)