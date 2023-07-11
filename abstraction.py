#hiding the implimentation
from abc import ABC,abstractmethod
class abstract(ABC):
    @abstractmethod
    def houserent(self):
        None
    @abstractmethod      
    def officerent(self):
        None
class expence(abstract):
    def houserent(self):
        print(10000)
    def officerent(self):
        print(25000)
class god(abstract):
    def houserent(self):
        print("fevorite god 1")
    def officerent(self):
        print("fevorite god 2")
obj=expence()
obj.houserent()
obj.officerent()

obj2=god()
obj2.houserent()
obj2.officerent()