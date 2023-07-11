
#method overrinding

class parent:
    a=10
    b=20
    def run(self):
        print("manjusha can run")
class child(parent):
    def run(self):
        print("manjusha can walk")
obj=child()
print(obj.a,obj.b)
obj.run() 