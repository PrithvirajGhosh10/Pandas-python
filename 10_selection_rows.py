import pandas as pd
df=pd.read_csv("data.csv", index_col="name") #to scarch by name
#SELECTION BY ROW/S
print(df.loc["Pikachu"])
'''
no                    25
type1        Electricity
type2                NaN
height               1.0
weight              42.5
legendary              0
Name: Pikachu, dtype: object
'''
print(df.loc["Charizard",["height","weight"]])
'''
height     1.1
weight    14.0
Name: Charizard, dtype: float64
'''
print(df.loc["Charizard":"Blastoise",["height","weight"]]) #height weight between two name

'''
           height  weight
name                     
Charizard     1.1    14.0
Squirtle      1.2    15.5
Wartortle     1.3    17.0
Blastoise     1.4    18.5
'''
#selection by integers
print(df.iloc[0:11])
'''
            no     type1   type2  height  weight  legendary
name                                                       
Bulbasaur    1      Fire     NaN     0.6     6.5          0
Ivysaur      2     Water     NaN     0.7     8.0          0
Venusaur     3       Bug     NaN     0.8     9.5          0
Charmander   4    Normal  Flying     0.9    11.0          0
Charmeleon   5    Poison     NaN     1.0    12.5          0
Charizard    6  Electric     NaN     1.1    14.0          0
Squirtle     7    Ground     NaN     1.2    15.5          0
Wartortle    8     Grass  Flying     1.3    17.0          0
Blastoise    9      Fire     NaN     1.4    18.5          0
Caterpie    10     Water     NaN     1.5    20.0          0
Metapod     11       Bug     NaN     1.6    21.5          0
'''
print(df.iloc[0:11:2])#every second rows
print(df.iloc[0:11:2,0:3])#print first 3 colunms
pokemon=input("Enter a Pokemon name: ")
try:
    print(df.loc[pokemon])
except keyError:
    print(f"{pokemon} not found")