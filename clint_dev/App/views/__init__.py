from App.views.Client import client_api, client_add_api, client_put_api
from App.views.Device_v2 import devices_v2_api
from App.views.Devices_api import device_api
from App.views.MediasPags import mediaspags_api
from App.views.Themes_api import theme_api
from App.views.medias import medias_api
from App.views.mediasPag_themes import mediaspag_themes_api
from App.views.users_api import user_api, login_api, regist_api, index_api, user_admin_api, user_put_api, \
    device_admin_api, device_put_api, logout_api, device_add_api, mediapag_admin_api, mediapag_add_api, \
    mediapag_themes_api, theme_put_api, theme_add_api, test_api, theme_admin_api, new_theme_add_api, image_admin_api, \
    image_add_api, video_admin_api, video_add_api

__all__ = ['MyResponse','v1_0']

def init_blue(app):
    app.register_blueprint(blueprint=user_api)
    app.register_blueprint(blueprint=device_api)
    app.register_blueprint(blueprint=login_api)
    app.register_blueprint(blueprint=regist_api)
    app.register_blueprint(blueprint=index_api)
    app.register_blueprint(blueprint=user_admin_api)
    app.register_blueprint(blueprint=user_put_api)
    app.register_blueprint(blueprint=device_admin_api)
    app.register_blueprint(blueprint=device_put_api)
    app.register_blueprint(blueprint=logout_api)
    app.register_blueprint(blueprint=device_add_api)
    app.register_blueprint(blueprint=theme_api)
    app.register_blueprint(blueprint=medias_api)
    app.register_blueprint(blueprint=client_api)
    app.register_blueprint(blueprint=client_add_api)
    app.register_blueprint(blueprint=client_put_api)
    app.register_blueprint(blueprint=devices_v2_api)
    app.register_blueprint(blueprint=mediaspags_api)
    app.register_blueprint(blueprint=mediaspag_themes_api)
    app.register_blueprint(blueprint=mediapag_admin_api)
    app.register_blueprint(blueprint=mediapag_add_api)
    app.register_blueprint(blueprint=mediapag_themes_api)
    app.register_blueprint(blueprint=theme_put_api)
    app.register_blueprint(blueprint=theme_add_api)
    app.register_blueprint(blueprint=test_api)
    app.register_blueprint(blueprint=theme_admin_api)
    app.register_blueprint(blueprint=new_theme_add_api)
    app.register_blueprint(blueprint=image_admin_api)
    app.register_blueprint(blueprint=image_add_api)
    app.register_blueprint(blueprint=video_admin_api)
    app.register_blueprint(blueprint=video_add_api)

