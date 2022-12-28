# list1=[1,2,3,4,5,6,7,8,9,10]
# print(list1)
# for x in list1:
#     print(x)
for x in range(1,11):
    print(x, end=" ")
print("\n")
print("Odd Num:")
for x in range(1,100):
    if x % 2 != 0:
        print(x, end=" ")
print("\n")
print("Even Num:")
for x in range(1,100):
    if x % 2 == 0:
        print(x, end=" ")
print("\n")


for i in range(0, 11):
    print ("%d * %d = %d" % (23, i, 23* i))


for x in range(1,101,2):
    print(x,end=" ")
print("\n")

for x in range(2,101,2):
    print(x, end=" ")
print("\n")