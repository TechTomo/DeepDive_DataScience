#Encapsulation
#Access Modifiers
#Private, Protected and Public


class Person:
    def __init__(self,name,age) -> None:
        self.__name=name    #Private variable
        self._age=age       #Protected variable
    
    def display(self):
        print(f"The person name is {self.__name} and the age is {self._age}")
    
    
per=Person("Raj",26)
print(per._age)
per.display()


class Student(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
    
    def display(self):
        return super().display()
    

student=Student("Raj",26)
student.display()