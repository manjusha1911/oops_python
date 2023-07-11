class parent:
    a=10
    b=20
    def pf(self):
        print("this is a parent class")
class child1(parent):
    c=30
    d=40
    def cf(self):
        print("this is child1 class")
class child2(parent):
    x=15
    y=35
    def cf2(self):
        print("this is a child2 class")

# obj=parent()
# print(obj.a,obj.b)
# obj.pf()
# obj.cf()

# obj=child1()
# print(obj.a,obj.b)
# obj.pf()
# print(obj.c,obj.d)
# obj.cf()
obj=child2()
print(obj.x,obj.y)
obj.cf2()