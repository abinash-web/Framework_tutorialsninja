import configparser
import os


import configparser
import os

import configparser
import os

class ReadConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'configurations', 'config.ini'))
        self.config.read(config_path)
    def getApplicationURL(self):
        url = self.config.get('commonInfo', 'baseURL')
        return url
    @staticmethod
    def getUseremail():
        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), '..', 'configurations', 'config.ini')
        config.read(config_path)
        username = config.get('commonInfo', 'email')
        return username

    @staticmethod
    def getPassword():
        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), '..', 'configurations', 'config.ini')
        config.read(config_path)
        password = config.get('commonInfo', 'password')
        return password

    @staticmethod
    def getconformPassword():
        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), '..', 'configurations', 'config.ini')
        config.read(config_path)
        conformpassword = config.get('commonInfo', 'conformpassword')
        return conformpassword
