#compile time#

# class  myclass:
#     def add(self):
#         a=10
#         b=20
#         print(a,b)
#     def add(self,a,b):
#         print(a, b)
# obj=myclass()
# obj.add(100,200)
# obj.add(1000,200)


class  myclass:
    def add(self,a,b=10,c=19):
        print(a,b,c)
obj=myclass()
obj.add(100,200)
obj.add(100)
obj.add(1000,200,120)