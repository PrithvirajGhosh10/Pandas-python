import pandas as pd
a=[1,2,3]
b=pd.Series(a,index=["a","b","c"])#this are levels

b.loc["c"]=10 #changing the value o findex c
print(b)
'''
output: 

a     1
b     2
c    10
dtype: int64
'''
print(b.loc["a"]) #location by level
#op: 1


print(b.iloc[0]) #location by integer