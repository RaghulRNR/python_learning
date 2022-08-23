from threading import *
def display():
    print('child thread')
t=Thread(target=display)
t.start()
print(current_thread().ident)
print(t.ident)