class Human:
    def __init__(self,c,h,w):
        self.color=c
        self.height=h
        self.weight=w
    def eat(self):
        print("she can eat")
    def run(self):
        print("she can run")
    def walk(self):
        print("she can walk")
manjusha=Human("brown",5.1,55)
son=Human("white",3.1,25)
daughter=Human("Black",4.1,34)
print(manjusha.color,manjusha.weight,manjusha.height)
print(son.color,son.weight,son.height)
print(daughter.color,daughter.weight,daughter.height)


 