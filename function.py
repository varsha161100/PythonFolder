# function -> is a block of code that performs a specific task whenever it is called.

# 1.build in function  -> deifined and pre-coded in python
#     max(), min(), sum(), len(), list(), tuple(), set(), print(), type(), range()

# 2. user-defined function  ->  user create function to perform specific task as per our needs.

       


#_______________function arguments and return statement_______________________

# there are 4 types of argument
# default argument
# keyword argument
# variable length argument
# required argument

#________________________default argument_________________________

# while creating a default value creating a function. this way the function assumes a default value even if a value is not provided in the function call for that argument

def average(a=3,b=6):                 # default value
   print("the avg value is" , (a+b)/2)

average(4,2)


#________________________keyword argument_________________________

#we can provide argument with key=value, this way the interpreter recognizes by the prameter name . hence the order in which the argument are passed does not matter.


# average(a=2,b=8)  #________-with using keyword

#_______________________variable length argument____________________

def aa(*numbers): #  parameter
   sum=0
   for i in numbers:
      sum=sum+i
      print("Average is: ",sum/len(numbers))


aa(5,6)  #arguments


#________________________required argument__________
def average1(a,b=6):                 # default value
   print("the avg value is" , (a+b)/2)

average1(a=21)