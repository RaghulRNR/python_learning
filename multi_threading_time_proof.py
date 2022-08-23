import time
from threading import *

def square(numbers):
    for n in numbers:
        time.sleep(1)
        print(n*n)

def double(numbers):
    for n in numbers:
        time.sleep(1)
        print(2*n)

numbers=[1,2,3,4,5,6]
start_time=time.time()

t1=Thread(target=square,args=(numbers,))
t2=Thread(target=double,args=(numbers,))

t1.start()
t2.start()
#join is used,main thread will wait untill child threads got completed
t1.join()
t2.join()

end_time=time.time()

print('Toatl_time',end_time-start_time)

