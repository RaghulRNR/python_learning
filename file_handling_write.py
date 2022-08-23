f=open('FH_write.txt','w')
f.write('this is \n')
f.write('samples')
f.close()

f=open('FH_writeLines.txt','w')
l=['rahul','rnr','1703']#if you want spaces in between each element add logic to that
f.writelines(l)
f.close()



