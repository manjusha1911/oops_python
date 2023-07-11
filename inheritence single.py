class parent:
    a=5
    b=10
    def pf(self):
        print("parent class")
class child(parent):
    c=10
    d=9
    def cf(self):
        print("child class")
obj=child()
print(obj.a,obj.b)
obj.pf()
print(obj.c,obj.d)
obj.cf()
