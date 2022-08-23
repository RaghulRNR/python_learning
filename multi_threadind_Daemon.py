from threading import *

mt=current_thread()
print(mt.isDaemon())
print(mt.daemon)
#mt.setDaemon(True)#this will throw error because main threas has already strated