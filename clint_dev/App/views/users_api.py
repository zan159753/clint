# import os
import datetime
import random

from flask import Blueprint, request, jsonify, session, render_template, send_file, redirect, url_for
# from PIL import Image
from sqlalchemy import and_

from App.ext import db, cache
from App.logics import send_msg, get_user_paginate, check_login
from App.models import User
# from App.settings import BASEDIR

user_api = Blueprint("user_api", __name__, url_prefix='/api/users/')
login_api = Blueprint("login_api", __name__, url_prefix='/')
regist_api = Blueprint("regist_api", __name__, url_prefix='/regist/')
index_api = Blueprint("index_api", __name__, url_prefix='/index/')
user_admin_api = Blueprint("user_admin_api", __name__, url_prefix='/user_admin/')
user_put_api = Blueprint("user_put_api", __name__, url_prefix='/user_put/')
device_admin_api = Blueprint("device_admin_api", __name__, url_prefix='/device_admin/')
device_put_api = Blueprint("device_put_api", __name__, url_prefix='/device_put/')
logout_api = Blueprint("logout_api", __name__, url_prefix='/logout/')
device_add_api = Blueprint("device_add_api", __name__, url_prefix='/device_add/')

@login_api.route('/')
def to_login():
    return render_template('page-login.html')

@regist_api.route('/')
def to_regist():
    return render_template('page-register.html')

@index_api.route('/')
@check_login
def to_index():
    return render_template('index.html')

@user_admin_api.route('/')
def to_user_admin():
    return render_template('user-admin.html')

@user_put_api.route('/')
def to_user_put():
    return render_template('user-put.html')

@device_admin_api.route('/')
def to_device_admin():
    return render_template('devices-admin.html')

@device_put_api.route('/')
def to_device_put():
    return render_template('device-put.html')

@logout_api.route('/')
def to_logout():
    session.clear()
    return redirect('/',code=302)

@device_add_api.route('/')
def to_device_add():
    return render_template('device-add.html')


@user_api.route('/', methods=['GET', 'POST', "DELETE", "PUT","PATCH"])
# @api.route('/users/<int:page><int:per_page><u_account>/', methods=['GET', 'POST'])
def userContro(page=None, per_page=None,u_id=None, u_account=None, u_name=None, u_phone=None,
               u_wechat=None, u_qq=None, u_type=None, u_statu=None):
    if request.method == 'GET':

        pass


    # 登陆接口
    elif request.method == 'POST':

        # 管理员添加用户

        if request.form.get('u_account') and request.form.get('u_name') and request.form.get(
                'u_type') and request.form.get('u_phone') and request.form.get('u_password') and request.form.get('u_repassword'):
            # elif request.form.get('u_type'):
            account = request.form.get('u_account')
            name = request.form.get('u_name')
            type = request.form.get('u_type')
            phone = request.form.get('u_phone')
            password = request.form.get('u_password')
            repassword = request.form.get('u_repassword')
            if User.query.filter(User.u_account == account).first():
                return jsonify({'msg': 'u_account repeat', 'code': 1005}), 404
            elif User.query.filter(User.u_phone == phone).first():
                return jsonify({'msg': 'u_phone repeat', 'code': 1005}), 404
            elif password != repassword:
                return jsonify({'msg': 'wrong repassword', 'code': 1003}), 404
            else:
                user = User()
                user.u_phone = phone
                user.u_account = account
                user.u_type = type
                user.u_password = password
                user.u_name = name
                user.regist_time = datetime.date.today()
                db.session.add(user)
                db.session.commit()
                return jsonify({'msg': 'login success', 'code': 1000},
                               user.model_to_dict()), 200
        # 帐号密码登陆
        elif request.form.get('name'):
            print(1)
            name = request.form.get('name')
            password = request.form.get('password')
            repassword = request.form.get('repassword')
            user = User.query.filter_by(name=name).first()
            print(2)
            if user:
                print(user.password)
                print(password)
                if password == user.password:
                    print(3)
                    session['u_id'] = user.id
                    return jsonify({'msg': 'login success', 'code': 1000},
                                   user.model_to_dict()), 200
                else:
                    return jsonify(
                        {'msg': 'wrong password', 'code': 1001}), 200
            else:
                if password == repassword:
                    user = User()
                    user.u_account = name
                    user.u_password = password
                    user.regist_time = datetime.date.today()
                    db.session.add(user)
                    db.session.commit()
                    return jsonify(
                        {'msg': 'regist success', 'code': 1000},
                        user.model_to_dict()), 200
                else:
                    return jsonify(
                        {'msg': 'wrong repassword', 'code': 1003}), 200

        # 短信登陆
        elif request.form.get('u_phone') and request.form.get('u_verify_code'):
            phone = request.form.get('u_phone')
            u_verify_code = request.form.get('u_verify_code')
            user = User.query.filter_by(u_phone=phone).first()
            if user:
                verify_code = cache.get(phone)
                if verify_code == u_verify_code:
                    session['u_id'] = user.u_id
                    return jsonify({'msg': 'login success', 'code': 1000}
                                   ), 200
                else:
                    return jsonify(
                        {'msg': 'wrong verify_code', 'code': 1003}), 404
            else:
                verify_code = cache.get(phone)
                if verify_code == u_verify_code:
                    user = User()
                    user.u_phone = phone
                    user.regist_time = datetime.date.today()
                    db.session.add(user)
                    db.session.commit()
                    return jsonify({'msg': 'regist success', 'code': 1000},
                                   user.model_to_dict()), 200
                else:
                    return jsonify(
                        {'msg': 'wrong verify_code', 'code': 1003}), 404
        # 发送验证码
        elif request.form.get('u_phone'):
            phone = request.form.get('u_phone')
            verify_code = send_msg(phone)
            cache.set(phone, verify_code, 180)
            return jsonify({'msg': 'send_msg success', 'code': 1001}), 200

        else:
            return jsonify({'msg': 'error', 'code': 1005}), 404

    elif request.method == 'PUT':
        if request.form.get('u_id'):
            u_id = request.form.get('u_id')
            user = User.query.get(u_id)
            u_phone = user.u_phone
            u_wechat = user.u_wechat
            u_chid = user.u_chid
            u_chkey = user.u_chkey
            print(u_id,u_phone,u_wechat,u_qq)

            if user:
                if request.form.get('u_name'):
                    user.u_name = request.form.get('u_name')
                    db.session.add(user)


                if request.form.get('u_phone'):
                    phone = request.form.get('u_phone')
                    if phone == u_phone:
                        pass
                    elif User.query.filter_by(u_phone=phone).first():
                        return jsonify(
                            {'msg': 'u_phone repeat', 'code': 1005}), 404
                    else:
                        user.u_phone = phone
                        db.session.add(user)


                if request.form.get('u_company'):
                    user.u_company = request.form.get('u_company')
                    db.session.add(user)


                if request.form.get('u_wechat'):
                    wechat = request.form.get('u_wechat')
                    u = User.query.filter_by(u_wechat=wechat).first()

                    if not u:
                        user.u_wechat = wechat
                        db.session.add(user)
                    elif int(u_id) == u.u_id:
                        pass
                    else:
                        return jsonify(
                            {'msg': 'u_wechat repeat', 'code': 1005}), 400


                if request.form.get('u_qq'):
                    qq = request.form.get('u_qq')
                    u = User.query.filter_by(u_qq=qq).first()
                    if not u:
                        user.u_qq = qq
                        db.session.add(user)
                    elif int(u_id) == u.u_id:
                            pass
                    else:
                        return jsonify(
                            {'msg': 'u_qq repeat', 'code': 1005}), 412


                if request.form.get('u_chid'):
                    user.u_chid = request.form.get('u_chid')
                    db.session.add(user)


                if request.form.get('u_chkey'):
                    user.u_chkey = request.form.get('u_chkey')
                    db.session.add(user)


                if request.form.get('u_type'):
                    user.u_type = request.form.get('u_type')
                    db.session.add(user)


                if request.form.get('u_password'):
                    user.u_password = request.form.get('u_password')
                    db.session.add(user)


                if request.files.get('u_icon'):
                    user.u_icon = request.files.get('u_icon')
                    db.session.add(user)


                if request.form.get('u_statu'):
                    user.u_statu = request.form.get('u_statu')
                    db.session.add(user)


                if request.form.get('u_statu'):
                    user.u_statu = request.form.get('u_statu')
                    db.session.add(user)
                    db.session.commit()
                return jsonify(
                    {'msg': 'change success', 'code': 1000}), 200

                # else:
                #     return jsonify({'msg': 'no change', 'code': 1000}), 200
            else:
                return jsonify({'msg': 'no user', 'code': 1004}), 404
        else:
            return jsonify({'msg': 'no u_id', 'code': 1004}), 405

    elif request.method == 'DELETE':
        if request.form.get('u_id'):
            u_id = request.form.get('u_id')
            user = User.query.get(u_id)
            if user:
                user.u_statu = 2
                db.session.add(user)
                try:
                    db.session.commit()
                    return jsonify(
                        {'msg': 'user write-off', 'code': 1000}), 202
                except:

                    return jsonify({'msg': 'delete error', 'code': 1004}), 404
            else:

                return jsonify({'msg': 'no user', 'code': 1004}), 404
        else:

            return jsonify({'msg': 'no u_id', 'code': 1004}), 404
    elif request.method == 'PATCH':
        if request.form.get('u_id'):
            u_id = request.form.get('u_id')
            user = User.query.get(u_id)
            if user:
                user.u_statu = 1
                db.session.add(user)
                try:
                    db.session.commit()
                    return jsonify(
                        {'msg': 'user write-off', 'code': 1000}), 202
                except:

                    return jsonify({'msg': 'delete error', 'code': 1004}), 404
            else:

                return jsonify({'msg': 'no user', 'code': 1004}), 404
        else:

            return jsonify({'msg': 'no u_id', 'code': 1004}), 404
    else:

        return jsonify({'msg': 'Method Error', 'code': 1004}), 404





# @api.route('/medias/', methods=['GET', 'POST'])
# def medias():
#     if request.method == 'POST':
#         file = request.files['abc']
#         filename = file.filename
#         save_path = os.path.join(BASEDIR, 'static', 'uploads', filename)
#         im = Image.open(file)
#         print(im.size)
#         print(im.format)
#         file.save(save_path)
#
#         return 'success'
#
#     if request.method == 'GET':
#         filename = request.args.get('filename')
#         file_path = os.path.join('static', 'uploads', filename)
#         return file_path

# 添加模拟用户数据
# def info_user():
#     user = User()
#     user.u_name = 'ab{}'.format(random.randint(1,100))
#     user.u_phone = random.randint(10000000000,200000000000)
#     user.u_account = 'ab{}'.format(random.randint(1,1000))
#     user.u_type = 1
#     user.regist_time = datetime.date.today()
#     user.u_password = '123'
#     user.u_statu = 1
#     user.u_level = 1
#     db.session.add(user)
#     db.session.commit()
