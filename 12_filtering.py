import pandas as pd

#FILTERING = KEEPING THE ROWS THAT MATCH A CONDITION

df=pd.read_csv("data.csv")


tall_pokemon=df[df["height"]>2]
print(tall_pokemon) #print all pokemon above height 2

heavy_pokemon=df[df["weight"]>100]
print(heavy_pokemon)#print all pokemon above weight 100

legendary_pokemon=df[df["legendary"]==1] #all legendary pokemon
print(legendary_pokemon)

water_pokemon=df[df["type1"]=="Water"] #all water type1 pokemon
print(water_pokemon)


water_pokemon=df[(df["type1"]=="Water")| #or logical operator
                 (df["type2"]=="Water")] #all water type1 or type 2 pokemon
print(water_pokemon)

ff_pokemon=df[(df["type1"]=="Fire")& #and logical operator
              (df["type2"]=="Flying")] #all fire type1 or flying type pokemon
print(ff_pokemon)