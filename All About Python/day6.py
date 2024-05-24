# Tuple, Dictionary, Set

#List has  duplicate , Set has no duplicate
st={1,2,3}
print(type(st))
for i in st:
    print(i)

print(st)
st.add(0)
print(st)

dic={1:"Raj"}
print(dic)

dict={"carname1":"Audi","carname2":"BMW","carname3":"Mercedes"}
print(dict)
print(dict["carname1"])
print(dict.items())
print(dict.keys())
print(dict.values())

dict["carname4"]="Ambassador"
print(dict)

car1_model={"BMW":1960}
car2_model={"Ambassador":2000}
car_type={"carname4":car2_model,"carname2":car1_model}
print(car_type)
print(car_type["carname4"]["Ambassador"])


tup=(1,2,3)
print(tup)
print(type(tup))

