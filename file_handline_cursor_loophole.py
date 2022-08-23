f=open('FH_read.txt','r')
#once file is open according to cursor only the methos will read the files
print(f.read(3))
print(f.readline())
print(f.read(3))
print('remaining data')
print(f.read())