#operator overloading
class Book:
    def __init__(self,pages):
        self.pages=pages

    '''this called magic function with this function we can override operators we can override any operators in python
        with specific operator magic method'''
    def __add__(self, other):
        return  Book(self.pages+other.pages)


    def __str__(self):
        return str(self.pages)

    def __mul__(self, other):
        return Book(self.pages * other.pages)


b1=Book(100)
b2=Book(200)
b3=Book(300)
b4=Book(400)

print(b1+b2)

''' the above code this will return error because unsupported operand type(s) for +: 'int' and 'Book',
To resolve this error we need to change return type of the reference object--->changed the return type in __add__ method'''
#print(b1+b2+b3) try this code  by commenting ___str__ method
'''if we change the type of the object then interger value will not displayed, so we need to overwrite default 
    ___str__ method '''
print(b1+b2+b3)

print(b1+b2*b3+b4)