'''
Dictionaries are quite like lists but you cant join Dictionaries with a plus sign

'''

super_villains={1:1,2:4,3:9,'3':10}

print(super_villains,end="\n")


del super_villains[1]

print(super_villains)
print(super_villains[3]) # notice the differnece in type
print(super_villains['3']) # notice the differnece in type
# print(super_villains['2']) #note that this is invalid 
super_villains[10]=100
print(super_villains)
print(len(super_villains))
print(super_villains.get(2))
print(super_villains.keys())
print(super_villains.values())
print(super_villains)
