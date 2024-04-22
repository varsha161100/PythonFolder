# it is the process of defining something in terms of itself

def fact(num):
    if(num==1 or num==0):
     return 1
    else:
       return(num * fact(num-1))
    

print(fact(3))

#_________fabonacci number___________


f0=0
f1=1
f2=f1+f0
fn=f(n-1)+f(n-2)