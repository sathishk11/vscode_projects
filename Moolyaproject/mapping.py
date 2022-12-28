# a=[1,2,3,4,5,6,7,8,9]
# b=[100,200,300,400,500,600,700,800,900]
# c=zip(a,b) # using zip function pair a & b
# #print(list(c))
#
# a=("a","b","c")
# b=("A","B","C")
# c=zip(a,b)
# #print(tuple(c))
#
# for x,y in c:
#     print(x,y)

a=(10,25,45)
b=(12,30,40)
for a,b in zip(a,b): # here
    if a<b:
        x=b-a
        print("profit:",x)
    elif a>b:
        d=a-b
        print("loss:",d)
