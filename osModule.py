
# create folder
# import os

# if(not os.path.exists("data")):
#  os.mkdir("data")


# for i in range (0,100):
#  os.mkdir(f"data/day{i+1}")
 


 #remane the module  

# import os


# for i in range (0,100):
#  os.rename(f"data/tutorial{i+1}",f"data/tutorial {i+1}")
 

# print all the folders name

import os
folders = os.listdir("data")

print(folders)

for folder in folders:
    print(os.listdir(f"data/{folder}"))



