l=[10,"sathish", 2.6, True] # list (collection of different data types)
print(type(1))
print(l[1])
a=[10, 9, "rishi", "mark","run", 23] # list can accept duplicate values also
print(a[-1])
print(a[0:4:3])
print(type(a))
w=[1,2,3,4,5,6,7,8,9]
print(w[0:8:2])
#list methods
#append() add item at end of the list
a.append(222)
print(a)
a.insert(3, "moolya") # here we change the 1st index as moolya and shifting the index value to right
print(a)
a.remove("mark") # remove the string from list
print(a)
b=["one", "two", "three", "four", "five"]
b.sort() # it will arrange the ascending order
print(b)
print(b.count("five")) # to print how many "five" is there
c=[1,2,3,43,25,16,7,8,9]
c.sort()
c.reverse() # it will arrange the descending order
print(c)
c.clear()
print(c)

