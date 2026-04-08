# Aggregation : Represents a "has-a" relationship between classes
# Here each customer has a address 
# One class contains another class
class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
    
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name=new_name
        self.address.edit_address(new_city,new_pin,new_state)

class Address:
    def __init__(self,city,pin,state):
        self.city=city
        self.pin=pin
        self.state=state
    
    def edit_address(self,new_city,new_pin,new_state):
        self.city=new_city
        self.pin=new_pin
        self.state=new_state

add1=Address("Vadodara",390014,"Gujarat")
cust1=Customer("Khushi","F",add1)

print(cust1.name)
print(cust1.gender)

cust1.edit_profile("Khushboo","Gurgaon",390015,"UP")

print(cust1.name)
print(cust1.address.city)
