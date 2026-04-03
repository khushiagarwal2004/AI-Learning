class Phone:
    def __init__(self,brand,price,camera):
        self.brand=brand
        self.price=price
        self.camera=camera
    def buy(self):
        print("Buy a Phone")

class SmartPhone(Phone):
    def buy(self):
        print("Buy a Smartphone")

P1=SmartPhone("Apple",20000,13)
print(P1.brand)
P1.buy()

# Compile-time Polymorphism : Include method Overloading
# Run-time Polymorphism : Include method Overriding
# Operator Overloading 