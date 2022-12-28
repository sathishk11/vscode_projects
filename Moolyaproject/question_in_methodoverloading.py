from multipledispatch import dispatch
import math
@dispatch(int)
def act(a):
    print("Squareroot:", a**2)
@dispatch(int,int)
def act(a,b):
    print("addition:", a+b)

@dispatch(int,int,int)
def act(a,b,c):
    print("mutiplication:", a*b*c)

@dispatch(int,int,int,int)
def act(a,b,c,d):
    x=a*b*c*d
    if x<0:
        print("not possible")
        print("\n")
    else:
        r = math.isqrt(x)
        if r**2 == x:
            print(x,"is perfect square",end=" ")
        else:
            print(x,"is not perfect square",end=" ")
act(1,3,3,3)
act(1,2,4,6)
act(2,3,4)
act(2,3)
act(4)
