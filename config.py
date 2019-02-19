import os

class Config:
    '''
    General configuration parent class
    '''
    pass
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:psql@localhost/notebook'
    API_BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
     SQLALCHEMY_DATABASE_URI= os.environ.get('HEROKU_POSTGRESQL_BROWN_URL')

__    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
