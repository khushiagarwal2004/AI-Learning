class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d

# Few magic methods in python which help to create our own datatype
# Magic methods are called automatically with some triggers and can't be called by any method you create. 

    def __str__(self):
        return f"Fraction is {self.num}/{self.den}"
    def __add__(self,other):
        temp_num=self.num*other.den+other.num*self.den
        temp_den=self.den*other.den
        return f"Sum is:{temp_num}/{temp_den}"
    def __sub__(self,other):
        temp_num=self.num*other.den-other.num*self.den
        temp_den=self.den*other.den
        return f"Diff is:{temp_num}/{temp_den}"
    def __mul__(self,other):
        temp_num=self.num*other.num
        temp_den=self.den*other.den
        return f"Product is:{temp_num}/{temp_den}"
    def __truediv__(self,other):
        temp_num=self.num*other.den
        temp_den=self.den*other.num
        return f"Division is:{temp_num}/{temp_den}"

x=Fraction(2,3)
y=Fraction(4,3)
print(x+y)
print(x-y)
print(x*y)
print(x/y)