# DRY : Don't repeat yourself signifies code reusability  
# Inheritance : Parent class propeties i.e. data as wel as methods are being used by child class.
# Scenario : Udemy 
# Class 1 : Student inherits Users class
# Class 2 : Instructor inherits Users class
# Class 3 : User which has methods like login and registration 
# Note : Private members of Parent class are not inherited in child class
# supper method is used to inherit properties of parent class to child class
# Types of Inheritance : 
# Single-Level : One Parent ka ek child
# Multi-Level : Ek dada ka bete ka beta
# Hierarchical : Do Parent ka ek child
# Multiple : Ek Child ke do parent 
# Hybrid : Combination of above 4
# MRO : Method Resolution Order : In case of conflict that class method will execute first whose inheritance is first 
class User:
    def login(self):
        print("login")
    def register(self):
        print("Register")

class Student(User):
    def view(self):
        print("Viewed")
    def review(self):
        print("Reviewed")
    
class Instructor(User):
    def create(self):
        print("Created")
    def answer(self):
        print("Answered")

stu=Student()
ins=Instructor()

ins.create()
ins.answer()
ins.login()
ins.register()

stu.view()
stu.review()
stu.login()
stu.register()
