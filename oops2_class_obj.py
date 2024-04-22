#class

class Person:
    name="varsha"
    occupation="tester"
    networth=10
def info(self):
    print(f"{self.name} is  a {self.occupation}")

a=Person()
# a.name="shubham"
# a.occupation="Accountant"
print(a.name,a.occupation)



a.info()