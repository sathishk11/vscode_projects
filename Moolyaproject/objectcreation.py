class myclass:
    x,y = 10,20
    def s1(self, a,b):
        self.y = a
        self.x = b
        print(a+b)
        print(self.x+self.y)

obj = myclass()
obj.s1(3,6)
