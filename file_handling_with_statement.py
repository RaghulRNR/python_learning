#opening single file with python:
with open('FH_read.txt','r') as f:
    data=f.read()
    #print(data)
#opening multiple file in with statement
with open('FH_read.txt','r') as f1,open('FH_writeLines.txt','r') as f2:
    data=f1.read()
    print(data)
    print("*"*155)
    data = f2.read()
    print(data)