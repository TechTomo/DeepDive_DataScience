#JSON read_write from pandas

import pandas as pd

#Nested Dict
data=[{"name":"raj", "email":"test@wyn.com","phone":"12345","dept":"CS","job":{"title1":"PAT","title2":"QEA"}}]

#df=pd.read_json(data,orient='records')
#print(df)
print(pd.json_normalize(data))

df1=pd.DataFrame([['a','b'],['c','d']],
                 index=['r1','r2'],
                 columns=['c1','c2'])

df2=df1.to_json(orient="columns")
print(df2)

