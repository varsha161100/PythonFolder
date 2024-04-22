#  dictionary are ordered collection of data items, they stored multiple items in a single variable 
#   dic items are key value pairs that are separated by commas and enclosed within curly brackets


# dic={
#     1611: "varsha",   # key:value
#     2323:"pratigya",
#     8798:"akash",
#     8454:"jayveer"
# }
# print(dic[1611])
# print(dic[8798])


  
# info= {'name':'varsha', 'age':22, 'eligible':True}
# print(info)
# print(info['name'])
# print(info.keys())
# print(info.values())

# for key in info.keys():
#     print(f"the value of corresponding to the key {key} is { info[key]}")
#     # print(info[key])


# print(info.items())
# for key, value in info.items():
#     print(f"the value of corresponding to the key {key} is {value}") 

#___________________________dictonary methods______________________________

ep1={122:45, 123:89,567:69,670:69}
ep2={34:23,568:78,989:45}

ep1.update(ep2)   #add ep1 and ep2
print(ep1)

ep1.popitem()  # last element delete

print(ep1)

#del ep1["122"] # KeyError: '122'  because it string not int ,in our list 122 is num not int
del ep1[122]
