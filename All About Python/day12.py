#Classes -> Real world entity
'''
class Car:
    pass

car1=Car()
car2=Car()


car1.windows=4
car1.tyres=4
car1.engine="diesel"

car2.windows=6
car2.tyres=3
car2.engine="petrol"

print(car1.engine)

'''

class Car:
    #Constructor
    def __init__(self,windows,tyres,engine):
        self.windows=windows
        self.tyres=tyres
        self.engine=engine
    
    def self_driving(self):
        print("The car type is "+self.engine)
    
    
    def self_model(self,model):
        print("The model of the car "+model)   
        
car1=Car(4,4,"Petrol")        
car1.self_driving()   
car1.self_model("A1")     