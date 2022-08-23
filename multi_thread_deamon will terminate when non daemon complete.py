from  threading import *
import  time
def job1():
    for i in range (10):
        time.sleep(2)
        print('Daemon')
t1=Thread(target=job1)
t1.setDaemon(True)
t1.start()
time.sleep(10)
print('Mian thread completed')