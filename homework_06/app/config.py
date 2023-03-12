

class Config(object):
    DEBUG = False
    TESTING = False
    ENV = ""
    SECRET_KEY = "QWERTY"
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://username:passwd!@localhost:5432/postgres"
    SQLALCHEMY_ECHO = False

class ProductionConfig(Config):
    ENV = "production"

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_ECHO = True

class TestingConfig(Config):
    TESTING = True
    ENV = "testing"
    SQLALCHEMY_ECHO = True