#we need import with path to rach required file name
#from core_python import myModule as M
import core_python as M

print(M.add(10,20))
print(M.pow(10,20))
print(M.var1)
print(M.var2)
#to use class methods initialize construtor and store it in reference variable and use refrence variable to call methods
#use module.classname() to call class
t=M.test(10,5)
t.mul()
print(t.mul())
print(t.sub())
t2=M.test1(196,98)
print(t2.mul())
print(t2.div())
