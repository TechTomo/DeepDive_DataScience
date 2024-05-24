#Data Classes

from dataclasses import dataclass

from sympy import true

@dataclass
class Person:
    name:str
    age:int
    profession:str
    
person=Person("Raj",26,"IT")
print(person.age)


@dataclass(frozen=True)
class Rectange:
    width:int
    height:int
    color:str="white"
    
rec=Rectange(12,14)
rec1=Rectange(10,20,"red")
print(rec1.color)


@dataclass
class Employye(Person):
    empid:str
    dept=str

per=Person("raj",26,"IT")
emp=Employye("raj",26,"it","007")
print(emp.name)

