from threading  import *

print(current_thread().getName())

current_thread().setName('rahul')

print(current_thread().name)