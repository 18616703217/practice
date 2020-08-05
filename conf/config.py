import os

BASEDIR = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))


class Config:
    """base config"""
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret key'
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # SQLALCHEMY_TRACK_MODIFICATIONS = True
    # FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    FLASKY_MAIL_SENDED = 'jianghan@julanling.com'  # 发件人地址
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'  # 邮件主题前缀


class ProductionConfig(Config):
    """运行环境配置"""
    DEBUG = True
    DIALCT = 'mysql'
    DRIVER = "pymysql"
    USERNAME = 'root'
    PASSWORD = '111111'
    HOST = 'localhost'
    PORT = '3306'
    DBNAME = 'practice'
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(DIALCT, USERNAME, PASSWORD, HOST,PORT, DBNAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 没有此配置会导致警告



class DevelopmentConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': ProductionConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

if __name__ == "__main__":
    print(ProductionConfig.SQLALCHEMY_DATABASE_URI)