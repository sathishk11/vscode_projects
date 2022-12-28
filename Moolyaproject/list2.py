a=[1,3,6,9,3,5,7]
a.pop(2) # it removes the index value of 2
print(a)
a.pop() # it removes the last index
print(a)
# set operators{}
s={50,30,44,76,"A", "M", "M"} # no duplicates are allowed
print(s)
print(len(s))
print(30 in s)
s.add(121)
print(s)
s.pop() # set pop operator removes the index value randomly
print(s)
s.pop()
print(s)
l={12,43,78,34,54}
r={21,43,68, 27}
z=l.union(r)
print(z)
x=l.symmetric_difference(r)
print(x)
y={12,43}
print(y.issubset(l)) #compare the value of y and l
y1={12,33}
print(y1.issubset(l))
y2={43,68}
print(r.issuperset(y2))
y.discard(12)
print(y)
