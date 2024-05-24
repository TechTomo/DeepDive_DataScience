#Multiple Constructor

from os import name


class Animal:
    
    def __init__(self,*args) -> None:
        if(len(args)==1):
            self.name=args[0]
        else:
            self.name=args[0]
            self.type=args[1]   
        
    '''
    def __init__(self,name,species):
        self.name=name
        self.species=species
        
    def __init__(self,name,species,age):
        self.name=name
        self.species=species
        self.age=age
    '''    
    def make_sound(self,sound):
        return ("The animal is {} and says {}".format(self.name,sound))
    
    
dog=Animal("dog","mammal")
print(dog.make_sound("huff"))