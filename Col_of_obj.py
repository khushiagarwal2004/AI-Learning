# Collection of Objects just like you parse list of integers,strings you can also parse list of objects.
# Work for all Mutable Datatypes List,Dict,Tuple

class Customer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print(f"I am {self.name} and my age is {self.age}")
    
c1=Customer("khushi",21)
c2=Customer("Muskan",21)
c3=Customer("Swara",20)

L=[c1,c2,c3]

for i in L:
    i.intro()

