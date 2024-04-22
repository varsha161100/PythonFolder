# custom error
#_____________________we can define custom exception by creating a new class that is derived from the build in exception class

a=int(input("enter any value between 5 and 9"))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")

