<<<<<<< HEAD
import logging,os
os.chdir('./Practice/Day_4')
=======
import logging
>>>>>>> d2f2eff7bb1951c00d379b614a15b75abaf18597
def echo(msg):
    return msg
'''
# Process (Multiple handler)
Make logger -> Set log level 
-> Make logger handler each -> Make loggin formatter
-> Binding handler and formatter for each
-> Finally, binding handlers to logger

'''
# Make logger
root_logger = logging.getLogger()

# Set log level
root_logger.setLevel(logging.DEBUG) ## DEBUG > INFO > WARN > ERROR > CRITICAL

# Make logger file handler 
file_handler = logging.FileHandler('test.log','w','utf-8')

# Make logger console handler
stream_handler = logging.StreamHandler()

# Make logging formatter
stream_formatter = logging.Formatter('%(asctime)s- %(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(asctime)s- %(levelname)s \
    %(filename)s:%(lineno)s - %(message)s')

# Binding handler and formatter
file_handler.setFormatter(file_formatter)
stream_handler.setFormatter(stream_formatter)

# Finally, binding handlers to logger
root_logger.addHandler(file_handler)
root_logger.addHandler(stream_handler)

root_logger.debug('Start of Program')
root_logger.debug(echo('debug mode'))
root_logger.info(echo('info mode'))
root_logger.warning(echo('warn mode'))
root_logger.error(echo('error mode'))
root_logger.critical(echo('critical mode'))
root_logger.debug('End of Program')


'''
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename = 'myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s- %(levelname)s - %(message)s')
logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total
print(factorial(5))
logging.debug('End of program')
'''