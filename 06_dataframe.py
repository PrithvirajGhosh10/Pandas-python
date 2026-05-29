import pandas as pd
#DataFrame= A tabular data structure with rows AND columns. (2 dimenitional)
#               similar toan excel spreadsheet

data={"Name":["Spongebob","Pateick","Squidward"],
      "Age":[30,35,50]
      }
df= pd.DataFrame(data)
print(df)
'''
output:
        Name  Age
0  Spongebob   30
1    Pateick   35
2  Squidward   50
'''
data={"Name":["Spongebob","Pateick","Squidward"],
      "Age":[30,35,50]
      }
df= pd.DataFrame(data,index=["Employee 1","Employee 2","Employee 3"]) #with index
print(df)
'''
output:
                 Name  Age
Employee 1  Spongebob   30
Employee 2    Pateick   35
Employee 3  Squidward   50
'''

#data of Employee 1 #call by index
print(df.loc["Employee 1"])
'''
output:

Name    Spongebob
Age            30
Name: Employee 1, dtype: object
'''
print(df.loc["Employee 2"])
print(df.loc["Employee 3"])
 
#by integer location 
print(df.iloc[0])
'''
output:

Name    Spongebob
Age            30
Name: Employee 1, dtype: object
'''
print(df.iloc[1])
print(df.iloc[2])
print(df) #print entire dataframe

#Add a new cloumn
df["Job"]=["cook","N/A","cashier"]
print(df)
'''
output:

                 Name  Age      Job
Employee 1  Spongebob   30     cook
Employee 2    Pateick   35      N/A
Employee 3  Squidward   50  cashier
'''
#Add a new row
new_row=pd.DataFrame([{"Name":"Harry","Age":28,"Job":"Engineer"}],
                     index=["Employee 4"])
df=pd.concat([df,new_row])  #concatination
print(df)
'''
output:

                 Name  Age       Job
Employee 1  Spongebob   30      cook
Employee 2    Pateick   35       N/A
Employee 3  Squidward   50   cashier
Employee 4      Harry   28  Engineer
'''
#create another row
new_rows=pd.DataFrame([
                      {"Name":"Rohim","Age":30,"Job":"Manager"}],
                     index=["Employee 5"])
df=pd.concat([df,new_rows])  #concatination
print(df)

'''
output:

 Name  Age       Job
Employee 1  Spongebob   30      cook
Employee 2    Pateick   35       N/A
Employee 3  Squidward   50   cashier
Employee 4      Harry   28  Engineer
Employee 5      Rohim   30   Manager
'''