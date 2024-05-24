#Pandas 
#Dataframes(Multiple row and column), series(one column and row), basic operations

from operator import index
import pandas as pd
import numpy as np

#Create DataFrames
data=np.arange(0,20).reshape(5,4)

p=pd.DataFrame(data,index=["Row1","Row2","Row3","Row4","Row5"],columns=["Col1","Col2","Col3","Col4"])
print(p)
print(p.head(2))
print(p.tail(2))

print(p.info())
print(p.describe())

#Indexing by Column name, rowindex[loc],rowindex columnindex [.iloc]
#print(p["Col1"])
print(p[["Col1","Col2","Col3"]])    #ColumnName
print(p.loc[["Row1","Row2"]])    #RowIndex
print(p.iloc[::,::3])     #RowIndex, ColumnIndex

#Convert dataframes into arrays
#using p.iloc[].values

df=pd.DataFrame(data=[[1,np.nan,2],[2,3,4]],index=["Row1","Row2"],columns=["Col1","Col2","Col3"])
print(df)
print(df.isnull())    #Check null values
