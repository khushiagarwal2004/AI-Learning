# DRY : Don't repeat yourself signifies code reusability  
# Inheritance : Parent class propeties i.e. data as wel as methods are being used by child class.
# Scenario : Udemy 
# Class 1 : Student inherits Users class
# Class 2 : Instructor inherits Users class
# Class 3 : User which has methods like login and registration 
# Note : Private members of Parent class are not inherited in child class
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
