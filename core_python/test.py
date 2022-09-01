import sys
#PYTHONPATH='C:\\Users\\Rahul Natarajan\\Desktop\\Python_testing\\'
sys.path.append('C:\\Users\\Rahul Natarajan\\Desktop\\Python_testing\\')
print(sys.path)

import testingPythonPath as p
t=p.test3(10,20)
print(t.mul())