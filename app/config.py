import os


class BaseConfig:
    def __init__(self):
        self.SECRET_KEY = os.environ["SECRET_KEY"]
        self.SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
        self.DEBUG = False
        self.TESTING = False


class DevelopmentConfig(BaseConfig):
    def __init__(self):
        super().__init__()
        self.DEBUG = True


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    def __init__(self):
        super().__init__()
        self.TESTING = True


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}


def get_config():
    env = os.environ.get("FLASK_ENV", "development")
    return config_by_name.get(env, DevelopmentConfig)()
