
def smartdivision(func):
    def inner(a,b):
        if (b==0):
           return  'we can divide it by 0'
            
        else:
            return func(a,b)
    return inner


@smartdivision
def division(a,b):
    return  a/b

print(division(10,2))
print(division(10,0))