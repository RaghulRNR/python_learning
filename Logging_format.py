import logging
logging.basicConfig(format= '%(asctime)s :%(levelname)s :%(message)s ' ,datefmt= '%d/%m/%Y %I: %M :%S %p')
print('logging module demo')
logging.debug('debug information')
logging.info(' info information')
logging.warning('warning information')
logging.error('error information')
logging.critical(' critical information')


#logging.basicConfig(format= '%(asctime)s :%(levelname)s :%(message)s ' ,datefmt= '%d/%m/%Y %I: %M :%S %p')
