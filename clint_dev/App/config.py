# BASEDIR

# 云之信配置
import os

from flask import json

YZX_URL = 'https://open.ucpaas.com/ol/sms/sendsms'
YZX_PARAMS = {
    "sid": "f70ffabee988e3df52d8455eedcd665f",
    "token": "8bb3e7f236ae48c2180d4a8b4a124c26",
    "appid": "f85427a7245745ffbb5132fdbce3f4db",
    "templateid": "455001",
    "param": "123456",
    "mobile": "18011984299",
    "uid": "2d92c6132139467b989d087c84a365d8",
}

# u_type 常量

ADVERTISING_USERS = 1
U_TYPE_2 = 2
U_TYPE_3 = 3
U_TYPE_4 = 4
U_TYPE_5 = 5
U_TYPE_6 = 6

# u_statu 常量

NORMAL_USER = 1
INVALID_USER = 2
U_STATU_3 = 3
U_STATU_4 = 4
U_STATU_5 = 5

# 项目根路径
BASE_DIR = os.getcwd()
# 主题文件夹路径
THEMES_DIR = os.path.join(BASE_DIR, 'static', 'themes')

# 主题初始配置
BASE_THEME_CONFIG = {"mainpic":{"window": {"x": 0,"y": 608,"w": 1080,"h": 712},"loop": 5},"video": {"window": {"x": 0,"y": 0,"w": 1080,"h": 608},"loop": 15}}

