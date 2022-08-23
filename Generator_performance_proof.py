import random
from datetime import *
names=[ ' sunny' , ' bunny' , ' chinny' , ' vinny' ]
subjects=['Python ' , ' Java ' , 'Blockchain' ]
def people_list(num) :
    results=[]
    for i in range(num) :
             person={
            'id' :i,
            ' name ' :random.choice(names),
            'subject' :random.choice(subjects)
            }
             results.append(person)
    return results

def people_generator(num) :
    for i in range(num) :
        person={
        ' id' :i,
        ' name ' : random.choice(names),
        ' subject' : random.choice(subjects)
        }
    yield person

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

t1=current_time
people_list(100000)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
t2=current_time
print('Time taken For List: ' ,t2-t1)
 
t1=current_time
people_generator(100000)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
t2=current_time
print('Time taken For List: ' ,t2-t1)