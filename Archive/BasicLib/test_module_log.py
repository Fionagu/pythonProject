import logging
import datetime
from pytest import mark

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

@mark.skip
def test_module_logger_1():
    log_name = 'test_module_logger_1'
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)

    f_handler = logging.FileHandler(log_name+'.txt')
    f_handler.setFormatter(logging.Formatter(fmt=LOG_FORMAT,datefmt= DATE_FORMAT))
    f_handler.setLevel(logging.INFO)

    c_handler = logging.StreamHandler()
    c_handler.setFormatter(logging.Formatter(fmt=LOG_FORMAT,datefmt= DATE_FORMAT))
    c_handler.setLevel(logging.CRITICAL)

    logger.addHandler(f_handler)
    logger.addHandler(c_handler)

    logger.debug('this is log debug ')
    logger.info('this is log info')
    logger.critical('this is log critical')


@mark.skip
def test_module_logger_2():
    log_name = 'test_module_logger_2'
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)

    log_file_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + " " +log_name+".txt"
    f_handler = logging.FileHandler(log_file_name+'.txt')
    f_handler.setFormatter(logging.Formatter(fmt=LOG_FORMAT,datefmt= DATE_FORMAT))

    logger.addHandler(f_handler)

    logger.info('this is use Logger module to log')
