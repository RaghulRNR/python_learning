import logging
logging.basicConfig(filename= 'log.txt' ,level=logging.DEBUG,filemode= 'w')
print('logging module demo')
logging.debug('debug information')
logging.info('info information')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')

#logging.basicConfig(filename= 'log.txt' ,level=logging.DEBUG,filemode= 'w')
#Defaullt filemode=append
#default logging=Warning
#if we dont pass any parameter then it will store log into console
