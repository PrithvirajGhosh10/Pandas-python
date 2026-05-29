import pandas as pd
#series = A pandas 1-dimentional labeled array that can hold any data type 
#             think of it like a single column in a spreadsheet (1-dimentional)
data =[100,102,104]
series=pd.Series(data)
print(series)

'''
output:

0    100
1    102
2    104
dtype: int64

'''

data =[100.1,102.2,104.3]
series=pd.Series(data)
print(series) #change the data type

'''
output:

0    100.1
1    102.2
2    104.3
dtype: float64

'''
a=["Prithvi","Harry","bro"]
b=pd.Series(a)
print(b) #string

'''
output:

0    Prithvi
1      Harry
2        bro
dtype: str

'''

bool=[True,False]
a=pd.Series(bool)
print(a) #boolean

'''
output:

0     True
1    False
dtype: bool

'''
data =[100,102,104,89]
series=pd.Series(data,index=["a","b","c","d"])  #set index with custom levels 😎, default is 0,1,2... it can be in list, touple, string,set, dictionary, numpy array
print(series)

'''
output:

a    100
b    102
c    104
d     89
dtype: int64
'''

d=[1,2,3]
b=pd.Series(d,index=["apartment 1","apartment 2","apartment 3"])
print(b)
'''
output:

apartment 1    1
apartment 2    2
apartment 3    3
dtype: int64

'''