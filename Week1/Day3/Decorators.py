#decorators are the functions that takes another function as input and returns a new function
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