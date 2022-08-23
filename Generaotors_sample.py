def genmy():
    yield 'A'
    yield 'B'
    yield 'c'

g=genmy()#iterate generator using next() method
print(type(g))
print(next(g))
print(next(g))
print(next(g))




