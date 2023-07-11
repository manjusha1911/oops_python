class parent:
    a=10
    b=20
    def pf(self):
        print("this is a parent class")
class child(parent):
    c=30
    d=40
    def cf(self):
        print("this is child class")
class grandchild(child):
    x=15
    y=35
    def gf(self):
        print("this is a grandchild class")
# obj=parent()
# print(obj.a,obj.b)
# obj.pf() 

# obj=child()
# print(obj.a,obj.b)
# print(obj.c,obj.d)
# obj.pf()
# obj.cf()


obj=grandchild()
print(obj.a,obj.b)
obj.pf()
print(obj.c,obj.d)
obj.cf()
print(obj.x,obj.y)
obj.gf()