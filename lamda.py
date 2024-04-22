# Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.


# def double(x):
#     return x*2

# double = lambda x:x*2
# cube = lambda x: x*x*x
# avg= lambda x,y,z:(x+y+z)/3

# print(double(5))
# print(cube(5))
# print(avg(3,5,10))

# # Function to calculate the product of two numbers
# def multiply(x, y):
#     return x * y
# # Lambda function to calculate the product of two numbers
# lambda x, y: x * y


z=lambda x,y:x+y
result=z(6,7)
print(result)