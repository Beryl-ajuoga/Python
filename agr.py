
def hello(name ,age):
    year = 2022 - age
    print( f" hello {name} you were born in {year}")

def greet_multiple(**kwargs):
    keys = kwargs.keys()
    if "country" in keys:
        return f"hello {kwargs['name']} from {kwargs['country']}"
    elif "age" in keys:
        year = 2022 - kwargs ["age" ]
        return f"hello {kwargs['name']} you were born in{year}"
    elif "name" in keys:
        return f"hello{kwargs['name']}"
    else:
        return f"hello anonymous"    
def hello(name ,age):
    year = 2022 - age
    print( f" hello {name} you were born in {year}")

def greet_multiple(**kwargs):
    keys = kwargs.keys()
    if "country" in keys:
        return f"hello {kwargs['name']} from {kwargs['country']}"
    elif "age" in keys:
        year = 2022 - kwargs ["age" ]
        return f"hello {kwargs['name']} you were born in{year}"
    elif "name" in keys:
        return f"hello{kwargs['name']}"
    else:
        return f"hello anonymous" 