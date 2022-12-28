l1=["moolya","python","class","monday"]
for x in l1:
    for y in x:
        print(y)

s="welcome"
for z in s:
    print(z)

l2=[["india","tamilnadu"],["usa","newjersy"],["canada","vancouver"]] #nested list
for a in l2:
    for b,c in l2:
        print("My country is:",b , "\nand i live in:",c)

dict1= dict(l2)    # nested list typecasted into dictionary
print(dict1)
for x,y in dict1.items(): # to iterate over a dictionary is to give dict1.items()
    print(x,y)

l3=["monday","tuesday","wednesday"]
set1=set(l3) #normal list can be typcasted into set , nested list cant be typecasted into set
print(set1)
tuple=tuple(l2) # nested list typecasted into tuple
print(tuple)
