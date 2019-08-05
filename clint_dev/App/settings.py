import os
from datetime import timedelta

import redis

BASEDIR = os.path.abspath('.')

def get_db_uri(DATABASE):
    ENGINE = DATABASE.get('ENGINE') or 'mysql'
    DRIVER = DATABASE.get('DRIVER') or 'pymysql'
    USER = DATABASE.get('USER') or 'root'
    PASSWORD = DATABASE.get('PASSWORD') or '1'
    HOST = DATABASE.get('HOST') or '127.0.0.1'
    PORT = DATABASE.get('PORT') or '3306'
    NAME = DATABASE.get('NAME') or 'develop_test'

    return "{}+{}://{}:{}@{}:{}/{}".format(ENGINE, DRIVER, USER, PASSWORD, HOST, PORT, NAME)

class Config():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRIT_KEY = 'ASDFGHJKL'





class DevelopConfig(Config):
    DEBUG = True
    SESSION_TYPE = 'redis'  # session类型为redis
    SESSION_PERMANENT = False  # 如果设置为True，则关闭浏览器session就失效。
    SESSION_USE_SIGNER = False  # 是否对发送到浏览器上session的cookie值进行加密
    SESSION_KEY_PREFIX = 'session:'  # 保存到session中的值的前缀
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379')  # 用于连接redis的配置
    PERMANENT_SESSION_LIFETIME = timedelta(days=3)

    CACHE_TYPE = 'redis'  # 使用redis作为缓存
    # CACHE_KEY_PREFIX  # 设置cache_key的前缀
    CACHE_REDIS_HOST = '127.0.0.1' # redis地址
    CACHE_REDIS_PORT = '6379' # redis端口
    # CACHE_REDIS_PASSWORD  # redis密码
    # CACHE_REDIS_DB  # 使用哪个数据库
    # # 也可以一键配置
    # CACHE_REDIS_URL
    # 连接到Redis服务器的URL。示例redis: // user: password @ localhost:6379 / 2

    DATABASE = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "clint"
    }


    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

envs = {
    'develop': DevelopConfig
}