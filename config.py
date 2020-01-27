class Config(object):
    # Common configuration
    SECRETE_KEY = 'anysecretekey'

    # SQLALCHEMY_DATABASE_URL= 'mysql://<username>:<password>@IP/<database_name>'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/ecom_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    # Development Configuration
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    # Production Configuration
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
