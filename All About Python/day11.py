#Positional and Keyword

'''
def hello(name,age):
    print("Hello "+name+ " you are "+ str(age)+" years old")
    
    
hello("Raj",27)
'''

def hello(*args,**kwargs):
    print(args)
    print(kwargs)
 
lst = ["Raj",27]
dic = {"name":"John","age":30}
#hello("Raj","Anand",age=27,city="Delhi")
hello(*lst,**dic)