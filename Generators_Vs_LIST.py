
'''l=[x*x for x in range(1000000000000000000000000000000000000000)]
print(l)#this code will rise memory allocation error'''

# if we use generators we can overcome this memory allocation error problem:
# List comprehension will internally consider as Generators

g=(x*x for x in range(1000000000000000000000000000000000000000))
print(type(g))
while True:
    print(next(g))