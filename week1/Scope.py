x = 100  # Global variable

def demo(a,b=10,*args,**kwargs):
    global x
    x = x + 1  # modifying global

    print("Positional:", a)
    print("Default:", b)
    print("Args:", args)
    print("Kwargs:", kwargs)

    # Lambda inside function
    multiply = lambda p, q: p * q
    print("Lambda result:", multiply(a, b))

demo(5, 20, 1, 2, 3, name="Khushi", city="Ahmedabad")

print("Global x:", x)