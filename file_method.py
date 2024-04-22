

# read a file

# f=open('fileName.txt','r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)


# read line by line


# f=open('fileName.txt','r')
# i=0
# while True:
#  line=f.readline()
#  i=i+1
#  if not line:
#   break
   
#  m1=int(line.split(",")[0])
#  m2=int(line.split(",")[1])
#  m3=int(line.split(",")[2])

#  print(f"Marks of student {i} in maths is: {m1}")
#  print(f"Marks of student {i} in english is: {m2}")
#  print(f"Marks of student {i} in science is: {m3}")
   
# print(line)

# add lines to the file

# f=open('fileName.txt','w')
# lines=['line 1\n' , 'line2\n' , 'line 3\n']
# f.writelines(lines)
# f.close()