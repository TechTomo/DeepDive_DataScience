#HTML read and write using Pandas

import pandas as pd

df=pd.read_html("https://en.wikipedia.org/wiki/Mobile_country_code")
print(type(df))

print(df[0])
df[0].to_html('test.html')

#html=pd.read_html('https://en.wikipedia.org/wiki/Kolkata',match='Kolkata urban agglomeration population growth')

#print(html[0])