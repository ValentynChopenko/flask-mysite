class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db'
    SQLALCHEMY_ECHO = True
    SECRET_KEY = ''

class DevConfig(BaseConfig):
    DEBUG = True

class TestConfig(BaseConfig):
    TESTING = True

class ProdConfig(BaseConfig):
    SQLALCHEMY_ECHO = False

def runtime_config(conf):
    if conf == "dev":
        return DevConfig
    if conf == "test":
        return TestConfig
    if conf == "pro":
        return ProdConfig