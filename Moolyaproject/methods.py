x=5
y=10
print(x+y)
a=10
b=15
print(a+b)

def t1(x,y):
    print(x+y)

t1(20,30)

def s(a,b,c):
    '''

    :param a:
    :param b:
    :param c:
    :return:
    '''
    return a**2

z=s(1,2,3)
print(z)

# fibonacci number
def f1(a):       
    x=0 
    y=1
    for i in range(a): 
        print(x,end=" ")
        x=y 
        y=x+y
f1(15)
print("\n")
import math
def fi1(x):
    print("The value of x:",x,end="")
    root = math.isqrt(x)
    if root**2 == x:
        print("This is fibonacci number :",x,end=" ")
    else:
        print("\nThis is not a fibonacci number :",x,end=" ")
def perfectsquare(x):
    c=5*x*x-4
    print("\nThe value of c:",c)
    root = math.isqrt(c)
    if root**2 == c:
        print("This is perfect square",c,end=" ")
    else:
        print("This is not perfect square :",c,end=" ")
perfectsquare(20)

print("\n")
x=0
y=1
print(x,y)
x=y
y=x+y
print(x,y)
print("\n")
def f2(a):
    for i in range(-1,15):
        i=i+1
        print(i,end=" ")

f2(10)

# positional arguments
# keyword arguments
# required arguments
# optional arguments