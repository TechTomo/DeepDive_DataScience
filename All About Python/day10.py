#Functions in python

#Parameterized Function
def func(msg):
  return(msg +" Welcome to python")



print(func("Hello")) 

#Function to print even or odd in a list
def sum_evenodd(lst):
    sume=0
    sumo=0
    for i in lst:
        if(i%2==0):
            sume=sume+i
        else:
            sumo=sumo+i
    return sume,sumo

sum1,sum2=sum_evenodd([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9])
print(sum1,sum2)
