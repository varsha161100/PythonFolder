# final keyword   
# it is a part of exception handling when we handle exception using the try and except block we can include a finally block at the end . the finally block it always exceuted so it is generally used  doing the concuding task like closing the resourse or closing database  connection or may be ending the program excution with a delightful message.

try:
    l=[1,5,6,7]
    i=int(input("enter the index: "))
    print(l[i])
except:
    print("some error occurred")

finally:
    print("i am always executed")

print("I am always executed")

x=func1()
print(xu)