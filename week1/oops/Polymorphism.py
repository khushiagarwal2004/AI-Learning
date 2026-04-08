class Phone:
    def __init__(self,brand,price,camera):
        self.brand=brand
        self.price=price
        self.camera=camera
    def buy(self):
        print("Buy a Phone")

class SmartPhone(Phone):
    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera)
        self.os=os
        self.ram=ram
    def buy(self):
        print("Buy a Smartphone")

P1=SmartPhone("Apple",20000,13,"Android",2)
print(P1.os)
print(P1.brand)
P1.buy()

# Compile-time Polymorphism : Include method Overloading : Dont work in python  
# Run-time Polymorphism : Include method Overriding
# Operator Overloading