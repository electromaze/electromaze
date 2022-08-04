import logging
from logging.handlers import RotatingFileHandler


def AppLogger(logger_name, log_file, level=logging.ERROR):
    log_formatter = logging.Formatter('%(asctime)s %(message)s')
    my_handler = RotatingFileHandler(log_file, mode='a', maxBytes=100*1024*1024, backupCount=5, encoding=None, delay=False)
    my_handler.setFormatter(log_formatter)
    my_handler.setLevel(level)
    l = logging.getLogger(logger_name)
    l.addHandler(my_handler)
