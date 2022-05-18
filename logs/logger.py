import logging
from logging.handlers import TimedRotatingFileHandler

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logname = "logs/my_app.log"


def get_logger():

    logger = logging.getLogger('my_app')
    logger.setLevel(logging.DEBUG)

    logger = time_handler(logger)
    return logger


def time_handler(logger):

    handler = TimedRotatingFileHandler(filename=logname, when="midnight", interval=1)
    handler.suffix = "%Y-%m-%d"
    formatter = logging.Formatter(LOG_FORMAT)

    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger