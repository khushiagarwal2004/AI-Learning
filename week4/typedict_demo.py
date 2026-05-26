# Type Dict 
# Just for adding structure to our dict no validation here
from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

new_person:Person={'name':'Khushi','age':21}
new_person2:Person={'name':'Khushi','age':'31'}
print(new_person)
print(new_person2)