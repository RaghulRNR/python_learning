#if we want to execute with and without decorators for a function then use this method
def smartdivision(func):
    def inner(a, b):
        if (b == 0):
            return 'we can divide it by 0'
        else:
            return func(a, b)
    return inner

def division(a, b):
    return a / b

useDivisionWithDecorator=smartdivision(division)# need to pass the function as argument explictliy

print(division(10,2))
print(useDivisionWithDecorator(10,0))