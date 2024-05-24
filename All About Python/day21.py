#XML read and write using Pandas

import pandas as pd

df=pd.read_xml('sample.xml')

print(df)
print(type(df))

#Retrieve Row
print(df.loc[5])

#print(df.columns[0])