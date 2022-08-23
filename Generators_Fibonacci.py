def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
g=fib()#this decorator object store 
'''for x in g:
    print(next(g))'''
for n in g:
    if n>100:
        break
    print(n)
