class Test:
    def sum(self,*a):
       # total=''
        total=0
        for x in a:
            total=total+x
        return total


t1=Test()
print(t1.sum(10,20,30))
#t1.sum(10,20,'rahul') it raise error because arguments passes as TUPLE same type of args only it support

#print(t1.sum('Rahul',' ','Natarajan','173')) use total=''