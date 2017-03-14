import os
import random
import sys

test_file = open('test.txt','wb') # write to a file 
# use ab+ to read and append to the file 

print(test_file.mode) # prints file mode 
print(test_file.name) # prints file name 

test_file.write(bytes('Write me to the file\n','UTF-8')) # yes very odd

test_file.close()

x=open('test','r+')
msg=x.read()
print('inside file material:',msg)
x.close()

# to remove the file
x=open('yahu','wb+')
x.write(bytes('info to be written\n','UTF-8'))
x.close()

