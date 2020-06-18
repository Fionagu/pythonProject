import logging
from pytest import mark

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

logging.basicConfig(level=logging.DEBUG,format=LOG_FORMAT, datefmt=DATE_FORMAT)


# @mark.skip
def test_basic_log():
    logging.info('test basic log')


# logging.basicConfig(filename='test_file_log.txt',level=logging.DEBUG,format=LOG_FORMAT, datefmt=DATE_FORMAT)

# @mark.skip
# def test_file_log():
#     logging.info('test file log')