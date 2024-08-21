# import logging
# import os.path
#
#
# class LogGen():
#     @staticmethod
#     def loggen():
#         path=os.path.abspath(os.curdir)+'\\logs\\automation.log'
#         logging.basicConfig(filename=path,format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%y %I:%M:%S %p')
#         logger=logging.getLogger()
#         logger.setLevel(logging.DEBUG)
#         return logger

# import logging
# import os
#
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         log_dir = os.path.join(os.getcwd(), 'logs')
#         os.makedirs(log_dir, exist_ok=True)  # Create logs directory if it doesn't exist
#
#         log_file = os.path.join(log_dir, 'automation.log')
#
#         logging.basicConfig(filename=log_file,
#                             format='%(asctime)s: %(levelname)s: %(message)s',
#                             datefmt='%m/%d/%y %I:%M:%S %p',
#                             level=logging.DEBUG)  # Set logging level to DEBUG
#
#         logger = logging.getLogger()
#
#         return logger


# import logging
# import os
#
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         log_dir = os.path.join(os.getcwd(), 'logs')
#         os.makedirs(log_dir, exist_ok=True)  # Create logs directory if it doesn't exist
#
#         log_file = os.path.join(log_dir, 'automation.log')
#
#         try:
#             logging.basicConfig(filename=log_file,
#                                 format='%(asctime)s: %(levelname)s: %(message)s',
#                                 datefmt='%m/%d/%y %I:%M:%S %p',
#                                 level=logging.DEBUG)  # Set logging level to DEBUG
#
#             logger = logging.getLogger()
#             return logger
#         except Exception as e:
#             print(f"Error setting up logging: {e}")
#             return None

import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# from tests.conftest import setup

from selenium.webdriver.support.ui import Select


class LogGen:
    @staticmethod
    def loggen():
        filehandler = logging.FileHandler('Logsfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger = logging.getLogger(__name__)
        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)
        # logger.debug("A debug statment is executed ")
        # logger.info("information statment")
        # logger.warning("something is in warning mode")
        # logger.error("A major error has happend")
        return logger
