# exception handling_ it is the process of responding to unwanted  or unexpected events when a computer program runs.
# it is deal with the events to avoid the program or system crashing.

# a=input("enter the number")
# print(f"Multiplication table of {a} is:")
# try:
#      for i in range(1,11):
#       print(f"{int(a)}X{i}={int(a)*i}")
# except Exception as e:       # or  except:
#    print("Invalid input")

# print("some imp line of code")
# print("end of program")


try:
     num=int(input("enter an integer: "))
     a=[6,3]
     print(a[num])
except ValueError:     
   print("enter no is not an integer.")
except IndexError:     
   print("Index Error")