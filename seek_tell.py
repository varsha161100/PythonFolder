#the seek() and tell() functions are used to work with file objects and their positions within a file. These functions are part of the built-in io module, which provides a consistent interface for reading and writing to various file-like objects, such as files, pipes, and in-memory buffers.


#The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position. 

# with open('fileName.txt', 'r') as f:
#   print(type(f))
#   # Move to the 10th byte in the file
#   f.seek(10)
#   # Read the next 5 bytes
#   data = f.read(5)
#   print(data)

#The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position.

with open('fileName.txt', 'r') as f:
   print(type(f))
   f.seek(10)
   print(f.tell())
  # Read the first 10 bytes
   data = f.read(10)
   print(data)

  # Save the current position
  current_position = f.tell()
  # Seek to the saved position
  f.seek(current_position)


