f=open('FH_read.txt','r')
data=f.read()
print(data)
print('*'*150)

f=open('FH_read.txt','r')
data=f.read(100)
print(data)
print('*'*150)

f=open('FH_read.txt','r')
data=f.readline()
print(data)
print('*'*150)

f=open('FH_read.txt','r')
data=f.readlines()
print(data)
print('*'*150)

f=open('FH_read.txt','r')
lines=f.readlines()
for line in lines:
    print(line,end='')
print('*'*150)