import pandas as pd
calories={"Day 1":1750,"Day 2":2100,"Day 3":1700}
series=pd.Series(calories) #we do not need to use the index porperty as in dictionary it has aldready have  set and value pairs
print(series)
'''
output: 

Day 1    1750
Day 2    2100
Day 3    1700
dtype: int64

'''
print(series.loc["Day 1"])
print(series.loc["Day 2"])
print(series.loc["Day 3"])
'''
output: 

1750
2100
1700
'''

#update values

series.loc["Day 3"] +=500 #increment the value by 500
print(series)
series.loc["Day 3"]=1500 #change the value
print(series)


#filteration

print(series[series>=2000]) #op:  Day 2    2100
print(series[series<2000]) 
'''
output:
Day 1    1750
Day 3    1500
dtype: int64
''' 