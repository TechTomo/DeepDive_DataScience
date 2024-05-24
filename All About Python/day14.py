#Inheritance

class Car:
  def __init__(self,name,model,year):
      self.name=name
      self.model=model
      self.year=year
      
  def driving(self): 
          print("Car is used for driving")
          

#Audi inherits Car
class Audi(Car):
  def __init__(self,name,model,year,color):
      super().__init__(name,model,year)
      self.color=color

  def self_driving(self):
    print("Audi is a self driving car")
    

audia7=Audi("audi","A1",2024,"Black")
print(audia7.year)
audia7.driving()
audia7.self_driving()      
print(dir(audia7))