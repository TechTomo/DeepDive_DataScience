#Pandas (StrinIO and read_csv)

import io 
import pandas as pd


df=pd.read_csv("student.csv",usecols=["name","class","mark"],sep=',')
print(df.head())
#print(df.info())


data=('Col1,Col2,Col3\n1,2,3\n4,5,6')
d=pd.read_csv(io.StringIO(data))
print(d)

#Datatypes in csv
data1=('Col1,Col2,Col3\n1,2,3.5\n4,5,6.8')
d1=pd.read_csv(io.StringIO(data1), dtype={'Col1': 'int32', 'Col2': 'float64', 'Col3': 'float32'})
print(d1)


