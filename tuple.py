'''
Unlike list tuple cannot be changed after it is built 
'''

pi_tuple=(3,1,4,1,5,9)

new_tuple=list(pi_tuple)
tupleagain=tuple(new_tuple)
print(pi_tuple) # a tuple
print(new_tuple) # a list 

A=[1,2,3]
B=[2,3,4]
C=A+B
D=[A,B]
print('C:',C,'D:',D);

