# # map function applies a function to each element in a sequence and return a new sequence . these function are known as higher order function, as they take other function as arguments.




# def cube(x):
#     return x*x*x

# print(cube(2))   # answer 8

# l=[1,2,4,6,4,3]


# # one way of cubing the list

# # newl=[]

# # for item in l:
# #  newl.append(cube(item))
# # print(newl)

# # 2nd way of cubing the list

# newl =list(map(cube,l))

# print(newl)


# #filter

# def filter_function(a):
#     return a>4

# newnewl = list(filter(filter_function,l))

# print(new)


#reduce

from functools import reduce

#list of number

numbers=[1,2,3,4,5]
numbers=[1,2,3,4,5]

#calculate the sum of the numbers using the reduce function

def mysum(x,y):
    return x+y

sum=reduce(mysum,numbers)


