from App.views.Devices_api import device_api
from App.views.users_api import user_api, login_api, regist_api, index_api, user_admin_api, user_put_api


def init_blue(app):
    app.register_blueprint(blueprint=user_api)
    app.register_blueprint(blueprint=device_api)
    app.register_blueprint(blueprint=login_api)
    app.register_blueprint(blueprint=regist_api)
    app.register_blueprint(blueprint=index_api)
    app.register_blueprint(blueprint=user_admin_api)
    app.register_blueprint(blueprint=user_put_api)
