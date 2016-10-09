# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'mathon'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <ibengo0929@163.com>'
    FLASKY_MAIL_TO = '837374908@qq.com'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    BEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    MAIL_SERVER = 'smtp.163.com'
    MAIL_POTR = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'ibengo0929@163.com'
    MAIL_PASSWORD = 'mcc0929'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
