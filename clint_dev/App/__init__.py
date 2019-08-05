from flask import Flask

from App.ext import init_ext
from App.settings import envs, DevelopConfig
from App.views import init_blue


def create_app():
    app = Flask(__name__,  template_folder='../templates', static_folder='../static')

    app.config.from_object(DevelopConfig)

    # 注册蓝图
    init_blue(app=app)

    init_ext(app=app)

    return app
