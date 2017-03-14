import sys
import os
import random
def sqr(x):
	return x*x
def addup(x,y):
	return x+y
def conca(x,y):
	return str(x)+str(y)
print(sqr(2))
print(addup(11,23));
print(conca(11,23));

print('what is your name')
x=sys.stdin.readline()
print('Hello ',x)

long_string ="I'll catch you if you fall - The floor"
print(long_string[0:3])
print(long_string[-5:]) ## last five characters

print(long_string[0:-4]) ## awesome

print('%d' % (1) ) 

x="hEllo my name is Abhinandan Agarwal. My work is awesome."
print(x.capitalize())
print(long_string.find('catch'))

x='asdsa'
print(x.isalpha())
y=1232
print(str(y).isalnum())
print(len(x))

print(long_string.replace('you','me'))

qlist=long_string.split(' ')
print(qlist)
