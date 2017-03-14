import random 
import sys
import os 

# if else elif == != > >= < <=

age=21

if age > 16 :
	print('You are old enough to drive')
else : 
	print('You are not old enough to drive')

if (age<15):
	print('man')
elif (age==21):
	print('yes yes print this')
else:
	print('naah print this ! ... ')

'''
	LOOPS --- > --- > --- > --- > --- > --- > --- > --- > --- > --- > --- > --- > --- > --- > --- > 
'''

for i in range(0,10): #excluded the last one ! 
	print(i,end=' ')
print('')
A=[1,2,3]
for x in A:
	print(x)

for x in [1,4,'yaiks']:
	print(x)
A=[[1,2],[3,2,1]]
for x in A:
	for y in x:
		print(y,end=' , ')
	print('')

