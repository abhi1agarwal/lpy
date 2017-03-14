import random
import sys
import os
print("Hello World")
#single and double quotes are exactly the same 
name="abhinadan agarwal"
print(name)
# Numbers strings Lists Tuples Dictionaries 
name = 15
'''
	+ - * / % **(expo) // (floor division)
'''

print (3//2)
print (3/2)
# OBSERVE THE DIFFERENCE BETWEEN THE TWO

print("1+2-3*2=",1+2-3*2)
#comma helps in concatenation 
"asda"
multi='''
yaaro
dosti  '''

print("yuki " + multi)
#above shows multi line strings 

print("i dont like it ",end="") # gets rid of the new lines for once
print("newlines")
print("are there still new lines ?")

# multiple replications
print('Abhinandan '*5,end="haaaa\n\n")
# obsrve the above 

grocery_list=['tiing tong','bing bong','ferocious']
print('firs item',grocery_list[0])
grocery_list[0]="assa"
print('firs item',grocery_list[0])
print(grocery_list[1:3]) # excludes the last index
other_evs=['Wash Car','Pickupkids','CashCheck']
total=[other_evs,grocery_list] #creatioon of a nested list 
print(total) # list inside of list 
# to get out the secon item 
print(total[0][1])
grocery_list.append('bollocks')
print(total) #change in grocery reflected in total, u c

grocery_list.insert(0,'aah i am at the beginning now')
print(total)
grocery_list.remove('ferocious')
other_evs.sort()
print('after removal and sorting',total)
total.sort() #kindda sorts all
#to reverse the list 
grocery_list.reverse()
print(total)

#to delete an item 
del grocery_list[2] #deleting assa
print(total)

print(len("asd"))
print(len(total))
print(max(grocery_list))
print(min(grocery_list))




A=[1,2,3]
B=[2,3,4]
C=A+B
D=[A,B]
print('C:',C,'D:',D);