import argparse
import logging
import logging.handlers #Required for some LoggingHandler
import os

LOG_FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "logging_example.log")
LOG_FILE_LEVEL = logging.INFO

parser = argparse.ArgumentParser(description='Logging with more handler example')
parser.add_argument(
    '--log',
    action = 'store',
    default = 'DEBUG',
    dest = 'loglevel',
    help = "Console Log level: DEBUG | INFO | WARNING | ERROR | CRITICAL | NOTSET (default: DEBUG)"
)
args = parser.parse_args()

# get console logging level
numeric_loglevel = getattr(logging, args.loglevel.upper(), None)
if not isinstance(numeric_loglevel, int):
    raise ValueError('Invalid log level: %s' % args.loglevel)

# create formatter
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s", '%Y.%m.%d %H:%M:%S')

# set up root logger
root_logger = logging.getLogger()
root_logger.setLevel(min(numeric_loglevel, LOG_FILE_LEVEL))

# set up logging to console
console_handler = logging.StreamHandler()
console_handler.setLevel(numeric_loglevel)
console_handler.setFormatter(formatter)
root_logger.addHandler(console_handler)

# set up logging to file
file_handler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setLevel(LOG_FILE_LEVEL)
file_handler.setFormatter(formatter)
root_logger.addHandler(file_handler)


# "application" code
logger = logging.getLogger("logging_example")

logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")