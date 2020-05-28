from configparser import ConfigParser

class Base():
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('config.ini')