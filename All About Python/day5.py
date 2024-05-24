#List



print(type([]))

str="Raj"       #Immutable
print(type(str))
print(str[0])   #Indexing

#List   Mutable
lst1=[1,2,3,4,"Hello",6,"Hi",8,9,"Bye"]
print(lst1)
lst1[5]="Raj"
print(lst1)
print(lst1[5])

lst1.append(["Back","Bye Again"])       #Nested List
print(lst1)
print(lst1[10][1])      

print(len(lst1))        #Lenth of list
print(lst1[2:6])          #Slicing
lst1.insert(1,"CS")
print(lst1[:]) 
print(lst1.count("Raj"))    #Count number of items present in a list
print(lst1.index("Hi"))   #Returns the index of first matching item


