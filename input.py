
import os 
import sys
import random

x=input("hello:")

y= x.split(' ')


print('x:',x)

print('y:',y)

print('')

a='12'
print(int(a)+2)

for x in y:
	i=int(x)
	print(i*i,end=' ')


x=("%d" % (1))
print(("%d" % (1)),("%s" % "hagg"))

y="{} is {}."
print(y.format('yes','no'))
print('')
print(y)


yo='   hey   '
print('yo :',yo,"\n",len(yo))
yo=yo.strip()
print('yo :',yo,"\n",len(yo))
print('a'+'b','c')