#List Comprehension

lst=[9,3,62,7]
lst.sort()
print(lst)

lst1=[1,2,3,4,5]
lst2=[]
for i in lst1:
    lst2.append(i**2)

print(lst2)

#Example1
num=[12,3,4,5]
sqr=[i**2 for i in num]
print(sqr)

#Example2
num1=[1,2,3,4,5,6]
evene=[n for n in num1 if n%2==0]
print(evene)

#Example3
lst3=[[1,2,3],[4,5,6]]
items=[item for sublist in lst3 for item in sublist]
print(items)

#Example4
words=['apple','banana','cherry','orange','grape']
letter=[w[0] for w in words]
print(letter)