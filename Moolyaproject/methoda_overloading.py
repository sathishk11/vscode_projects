from multipledispatch import dispatch
@dispatch(int,int)
def sum(a,b):
    print(a+b)

@dispatch(int,int,int)
def sum(a,b,c):
    print(a+b+c)

sum(12,40)
sum(20,30,40)