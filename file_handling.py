# # reading a file

# f=open('fileName.txt','r')

# print(f)
# text=f.read()
# print(text)
# f.close()

# # writing a file

# f=open('fileName.txt','w')    #  // add data to the file and remove all the previous data form the file
# f.write("hello world!")

# f.close()


# append  a file

f=open('fileName.txt','a')  # // add a data to the file
f.write("hello world!")

f.close()

with open('fileName.txt','a') as f:
    f.write("hi i am the queen of the world")