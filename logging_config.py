import logging
import colorlog

def logging_setup():   
    logging.basicConfig(    
        level=logging.INFO, 
        format="%(filename)s:%(lineno)d | [%(levelname)s] | %(message)s"
    )

def log_blank(logger):
    if  logger.isEnabledFor(logging.DEBUG):
        print("Test")