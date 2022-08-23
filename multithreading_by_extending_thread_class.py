from threading import *
class Mythread(Thread):
    def run(self):
        for  i in range(10):
            print('hello world',current_thread().getName())

t1=Mythread()
t1.start()
for i in range(10):
    print('hello world', current_thread().getName())