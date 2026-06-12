PANDAS SESSION
import pandas as pd
data={
    "Name":["Rajesh","Ram","Rahul"],
    "Marks":[25,36,28]
}

df=pd.DataFrame(data)

print(df)
print(df["Name"])
print(df["Marks"])
print(df.head(2))
print(df["Marks"].mean())
print(df.info())

df["Grade"]=["B","A","B"]
df["Passed"]=["No","Yes","Yes"]

print(df)
print(df.sort_values(by="Marks",ascending=False))
print(df.sort_values(by="Marks"))



-----------OUTPUT----------------

     Name  Marks
0  Rajesh     25
1     Ram     36
2   Rahul     28
0    Rajesh
1       Ram
2     Rahul
Name: Name, dtype: str
0    25
1    36
2    28
Name: Marks, dtype: int64
     Name  Marks
0  Rajesh     25
1     Ram     36
29.666666666666668
<class 'pandas.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Name    3 non-null      str  
 1   Marks   3 non-null      int64
dtypes: int64(1), str(1)
memory usage: 194.0 bytes
None
     Name  Marks Grade Passed
0  Rajesh     25     B     No
1     Ram     36     A    Yes
2   Rahul     28     B    Yes
     Name  Marks Grade Passed
1     Ram     36     A    Yes
2   Rahul     28     B    Yes
0  Rajesh     25     B     No
     Name  Marks Grade Passed
0  Rajesh     25     B     No
2   Rahul     28     B    Yes
1     Ram     36     A    Yes
PS C:\Users\Rajesh G R\Documents\pythonpractise> 
