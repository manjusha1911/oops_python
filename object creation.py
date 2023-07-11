class human:
    height=5.1
    weight=55
    color="brown"
    def run(self):
        print("she can run")
    def walk(self):
        print("she can walk")
    def eat(self):
        print("she can eat")
manjusha=human()  #object
print(manjusha.color,manjusha.height)
manjusha.eat()
manjusha.run()
print(manjusha.weight)