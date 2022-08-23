#exclusive operation

f=open('FH_read.txt','x')
print('File Name',f.name)
print('File Mode',f.mode)
print('Is Readable',f.readable())
print('Is Writable',f.writable())
print('Is File closed',f.closed)
f.close()
print('Is File closed',f.closed)
print('*'*70)

#Read Operation
f=open('FH_read.txt','r')
print('File Name',f.name)
print('File Mode',f.mode)
print('Is Readable',f.readable())
print('Is Writable',f.writable())
print('Is File closed',f.closed)
f.close()
print('Is File closed',f.closed)

print('*'*70)
#Write Operation
f=open('FH_read.txt','w')
print('File Name',f.name)
print('File Mode',f.mode)
print('Is Readable',f.readable())
print('Is Writable',f.writable())
print('Is File closed',f.closed)
f.close()
print('Is File closed',f.closed)

print('*'*70)

#append Operation
f=open('FH_read.txt','a')
print('File Name',f.name)
print('File Mode',f.mode)
print('Is Readable',f.readable())
print('Is Writable',f.writable())
print('Is File closed',f.closed)
f.close()
print('Is File closed',f.closed)

print('*'*70)

#Read write Operation
f=open('FH_read.txt','r+')
print('File Name',f.name)
print('File Mode',f.mode)
print('Is Readable',f.readable())
print('Is Writable',f.writable())
print('Is File closed',f.closed)
f.close()
print('Is File closed',f.closed)

print('*'*70)

#write read Operation
f=open('FH_read.txt','w+')
print('File Name',f.name)
print('File Mode',f.mode)
print('Is Readable',f.readable())
print('Is Writable',f.writable())
print('Is File closed',f.closed)
f.close()
print('Is File closed',f.closed)

print('*'*70)

#append read Operation
f=open('FH_read.txt','a+')
print('File Name',f.name)
print('File Mode',f.mode)
print('Is Readable',f.readable())
print('Is Writable',f.writable())
print('Is File closed',f.closed)
f.close()
print('Is File closed',f.closed)
print('*'*70)

