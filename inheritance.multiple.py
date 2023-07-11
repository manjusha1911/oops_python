class mother:
    a=10
    b=20
    def  mf(self):
        print("mother class")
class father:
    c=11
    d=12
    def ff(self):
        print("father class")
class child(mother,father):
    x=5
    y=15
    def cf(self):
        print("child class")
# obj=mother()
# print(obj.a,obj.b)
# obj.mf()


# obj=father()
# print(obj.c,obj.d)
# obj.ff()


obj=child()
print(obj.x,obj.y)
obj.cf()