import pandas as pd
df=pd.read_csv("data.csv", index_col="name")

pokemon=input("Enter a Pokemon name: ")
try:
    print(df.loc[pokemon])
except keyError:
    print(f"{pokemon} not found")

'''
Enter a Pokemon name: Pikachu
no                    25
type1        Electricity
type2                NaN
height               1.0
weight              42.5
legendary              0
Name: Pikachu, dtype: object
'''