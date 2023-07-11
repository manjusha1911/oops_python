# class parent:
#     a=10    #public
#     b=20
#     def display(self):
#         print("its a demo class")
# obj=parent()
# obj.display()
# print(obj.a,obj.b)


class parent:
    __a=10  #private
    b=20
    def display(self):
        print("its a demo class")
obj=parent()
obj.display()
print(obj.a,obj.b)  #error will come


