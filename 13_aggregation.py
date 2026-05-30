#aggregate functions

#Reduces a set of values into a single summary value Used to summarize and analyze data Often used with the groupby() function
import pandas as pd
df=pd.read_csv("data.csv")
print(df)
#whole dataframe
print(df.mean(numeric_only=True)) #only column which are numeric and can mean
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count())
#for single column
print(df["height"].mean()) #only column which are numeric and can mean
print(df["legendary"].sum())
print(df["legendary"].min())
print(df["height"].max())
print(df["weight"].count())

#pcnf=please click next file

