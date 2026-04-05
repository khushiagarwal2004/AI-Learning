#decorators are the functions that takes another function as input and returns a new function
# Types of decorators:
# class method : (cls) : when we want to change class attribute 
# instance method : (self) : when we want to change object attribute
# static method : () : when it doesn't get effected by any class or instace
# property decorator : when some vale change based on other parameter value so this will help in sync that change (eg: if marks of phy change then this change percentage itself w/o recalling percentage fun)

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@my_decorator
def display(a, b, c=10, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("Extra args:", args)
    print("Extra kwargs:", kwargs)

display(1, 2, 3, 4, 5, name="Khushi", age=21)