#Pickling and Unpickling

import seaborn as sns
import pandas as pd

df=sns.load_dataset('tips')

print(df.head())

import pickle

filename="file.pkl"

#Serialize
pickle.dump(df,open(filename,"wb"))

#Unserialize
df1=pickle.load(open(filename,"rb"))
print(df1.tail())

#Example1
dict={"Raj" : "CS", "Sachin" : "Cricket", "Messi" : "Football"}
pickle.dump(dict,open("file1.pkl","wb"))

df2=pickle.load(open('file1.pkl','rb'))
print(df2)

#Exmaple2
df3=pd.read_csv("student.csv",sep=',')
pickle.dump(df3,open('stud.pkl','wb'))
df4=pickle.load(open('stud.pkl','rb'))
print(df4.head(2))


