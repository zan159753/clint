import datetime
import os
from copy import copy, deepcopy

from flask import session, jsonify, redirect
from sqlalchemy import or_, and_

import App.config as cfg


import json
import random

import requests

from App.ext import db
from App.models import User, Devices


# 添加模拟用户数据
def info_user():
    user = User()
    user.u_name = 'ab{}'.format(random.randint(1,100))
    user.u_phone = random.randint(10000000000,200000000000)
    user.u_account = 'ab{}'.format(random.randint(1,1000))
    user.u_type = cfg.ADVERTISING_USERS
    user.regist_time = datetime.date.today()
    user.u_password = '123'
    user.u_statu = cfg.NORMAL_USER
    user.u_level = 1
    db.session.add(user)
    db.session.commit()



def send_msg(phone, ):  # 手机验证码

    PARAMS = cfg.YZX_PARAMS.copy()
    PARAMS['mobile'] = phone
    verify_code = str(random.randint(0, 999999)).zfill(6)
    PARAMS['param'] = verify_code

    PARAMS = json.dumps(PARAMS)
    print('验证码：' + verify_code)
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=utf-8',
    }
    resp = requests.post(url=cfg.YZX_URL, data=PARAMS, headers=headers)
    print(resp.json())
    return verify_code


def get_user_paginate(page, per_page, args):  # 查询用户分页
    page = page
    per_page = per_page
    pages = User.query.filter(or_(User.u_account == args, User.u_name == args, User.u_phone == args,
                                       User.u_wechat == args, User.u_qq == args, User.u_statu == args,
                                       User.u_type == args)).paginate(page=page, per_page=per_page,
                                                                       error_out=False)

    users = pages.items
    page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                'has_next': pages.has_next,'next_num':pages.next_num,"prev_num":pages.prev_num}
    data = []
    for user in users:
        data.append(user.model_to_dict())

    return data, page_msg

# def get_device_paginate(page, per_page, d_code=None,d_name=None,d_address=None,u_id=None,
#                   d_statu=None,d_sex=None,u_statu=None):  # 查询设备分页
#     page = page
#     per_page = per_page
#     if d_code:
#         pages = Devices.query.filter(Devices.d_code==d_code).paginate(page=page, per_page=per_page,
#                                                                                 error_out=False)
#
#     # elif ad:
#     #     pages = Devices.query.filter(and_(Devices.d_name == d_name,
#     #                              Devices.d_address == d_address, Devices.u_id == u_id,
#     #                              Devices.d_statu == d_statu, Devices.d_sex == d_sex,
#     #                               Devices.d_statu == u_statu)).paginate(page=page, per_page=per_page,
#     #                                                                error_out=False)
#
#     devices = pages.items
#     page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
#                 'has_next': pages.has_next}
#     data = []
#     for device in devices:
#         data.append(device.model_to_dict())
#
#     return data, page_msg

def get_device_paginate(pages):
    devices = pages.items
    page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                'has_next': pages.has_next}
    data = []
    for device in devices:
        data.append(device.model_to_dict())

    return data, page_msg

#登陆验证
def check_login(func):
    def wraps():
        try:
            u_id = session['u_id']
            return func()
        except:
            return redirect('/',code=302)
    return wraps

#创建theme文件夹
def make_theme_file(t_name):
    file_name = ['/mainpic','/video','/largepic']
    theme_path = os.path.join(cfg.THEMES_DIR,t_name)
    f = os.path.exists(theme_path)
    if not f:
        os.makedirs(theme_path)
        for name in file_name:
            os.mkdir(theme_path+name)
        config_file = os.path.join(theme_path,'config.json')
        with open(config_file,'w') as f:
            f.write(json.dumps(cfg.BASE_THEME_CONFIG))
        return theme_path
    else:
        return 0

def add_config(pic_loop=None,vedio_loop=None,theme_url=None):
    pic_loop = pic_loop
    vedio_loop = vedio_loop
    theme_url = theme_url
    THEME_CONFIG = deepcopy(cfg.BASE_THEME_CONFIG)
    THEME_CONFIG['mainpic']['loop'] = int(pic_loop)
    THEME_CONFIG['video']['loop'] = int(vedio_loop)
    try:
        config_file = os.path.join(theme_url, 'config.json')
        with open(config_file, 'w') as f:
            f.write(json.dumps(THEME_CONFIG))
    except:
        return False
    return True
