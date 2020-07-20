'''
log level
    [ low ]
 - debug
 - info
 - warning
 - error
 - critical(fatal)
    [ high ]
scenario
 - develope
 - deploy

'''
import logging

def say_hello(msg):
    return (msg)

## logging setting

## different output!! (level difference)
# logging.basicConfig(level = logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')

## different output!! (level difference)
# logging.basicConfig(level = logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s')

## different output!! (level difference)
logging.basicConfig(level = logging.WARN, format= '%(asctime)s - %(levelname)s - %(message)s')
logging.debug("Start of Program")
logging.debug(say_hello("debug mode"))
logging.info(say_hello("info mode"))
logging.debug("End of Program")