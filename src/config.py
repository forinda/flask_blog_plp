""" Application configuration """


class ProductionConfig:
    """ Production configuration """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init__(self):
        pass

    def configure_app(self, app):
        """ Configure the application """
        app.config.from_object(self)

    def __str__(self) -> str:
        return 'Production'

    def __repr__(self) -> str:
        return 'ProductionConfig'

    def get_configs(self):
        """ Get the configuration """
        return self.__dict__


class DevelopmentConfig:
    """ Development configuration """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init__(self):
        pass

    def configure_app(self, app):
        """ Configure the application """
        app.config.from_object(self)

    def __str__(self) -> str:
        return 'Development'

    def __repr__(self) -> str:
        return 'DevelopmentConfig'

    def get_configs(self):
        """ Get the configuration """
        return self.__dict__


class TestingConfig:
    """ Testing configuration """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db.sqlite3'
    PRESERVE_CONTEXT_ON_EXCEPTION = False

    def __init__(self):
        pass

    def configure_app(self, app):
        """ Configure the application """
        app.config.from_object(self)

    def __repr__(self):
        """ String representation """
        return '<TestingConfig>'

    def __str__(self) -> str:
        """ String representation """
        return 'TestingConfig'

    def get_configs(self):
        """ Get the configuration """
        return self.__dict__


class StagingConfig:
    """ Staging configuration """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db.sqlite3'

    def __init__(self):
        pass

    def configure_app(self, app):
        """ Configure the application """
        app.config.from_object(self)

    def __repr__(self):
        return '<StagingConfig>'

    def __str__(self):
        return 'Staging configuration'

    def __unicode__(self):
        return 'Staging configuration'

    def get_configs(self):
        """ Get the configuration """
        return self.__dict__


config = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig,
    "test": TestingConfig,
    "stage": StagingConfig
}
