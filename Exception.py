try:
    x=int(input('Enter the value X:'))
    y=int(input('Enter the value y:'))
    print('The result is ',x/y)
except BaseException as e:
    print('Exception Type',e.__class__)
    print('Exception class name',e.__class__.__name__)
    print('Exception description',e)
