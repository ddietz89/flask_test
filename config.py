import ConfigParser

class Config(object):
    configp = ConfigParser.ConfigParser()
    configp.read('config.ini')
    SECRET_KEY = configp.get('common', 'secret_key')
