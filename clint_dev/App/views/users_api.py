# import os
import datetime
import random

from flask import Blueprint, request, jsonify, session, render_template, send_file
# from PIL import Image
from sqlalchemy import and_

from App.ext import db, cache
from App.logics import send_msg, get_user_paginate
from App.models import User
# from App.settings import BASEDIR


user_api = Blueprint("user_api", __name__, url_prefix='/api/users/')

login_api = Blueprint("login_api", __name__, url_prefix='/')
regist_api = Blueprint("regist_api", __name__, url_prefix='/regist/')
index_api = Blueprint("index_api", __name__, url_prefix='/index/')
user_admin_api = Blueprint("user_admin_api", __name__, url_prefix='/user_admin/')
user_put_api = Blueprint("user_put_api", __name__, url_prefix='/user_put/')

@login_api.route('/')
def to_login():
    info_user()
    return render_template('page-login.html')

@regist_api.route('/')
def to_regist():
    return render_template('page-register.html')

@index_api.route('/')
def to_index():
    return render_template('index.html')

@user_admin_api.route('/')
def to_user_admin():
    return render_template('user-admin.html')

@user_put_api.route('/')
def to_user_put():
    return render_template('user-put.html')

@user_api.route('/', methods=['GET', 'POST', "DELETE", "PUT","PATCH"])
# @api.route('/users/<int:page><int:per_page><u_account>/', methods=['GET', 'POST'])
def userContro(page=None, per_page=None,u_id=None, u_account=None, u_name=None, u_phone=None,
               u_wechat=None, u_qq=None, u_type=None, u_statu=None):
    if request.method == 'GET':

        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 15))
        u_id = request.args.get('u_id')
        u_account = request.args.get('u_account')
        u_name = request.args.get('u_name')
        u_phone = request.args.get('u_phone')
        u_wechat = request.args.get('u_wechat')
        u_qq = request.args.get('u_qq')
        u_type = request.args.get('u_type')
        u_statu = request.args.get('u_statu')
        if u_name and u_type and u_statu:
            pages = User.query.filter(and_(User.u_name == u_name,User.u_statu == u_statu,
                                          User.u_type == u_type)).paginate(page=page, per_page=per_page,
                                                                         error_out=False)
            users = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next}
            data = []
            for user in users:
                data.append(user.model_to_dict())

            return jsonify(data=data, page_msg=page_msg), 200
        elif u_id:
            pages = User.query.filter_by(u_id=u_id).paginate(page=page, per_page=per_page,
                                                                            error_out=False)
            users = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next}
            data = []
            for user in users:
                data.append(user.model_to_dict())

            return jsonify(data=data, page_msg=page_msg), 200

        elif u_account:
            data, page_msg = get_user_paginate(page, per_page, args=u_account)
            return jsonify(data=data, page_msg=page_msg), 200
        elif u_name:
            data, page_msg = get_user_paginate(page, per_page, args=u_name)
            return jsonify(data=data, page_msg=page_msg), 200
        elif u_phone:
            data, page_msg = get_user_paginate(page, per_page, args=u_phone)
            return jsonify(data=data, page_msg=page_msg), 200
        elif u_wechat:
            data, page_msg = get_user_paginate(page, per_page, args=u_wechat)
            return jsonify(data=data, page_msg=page_msg), 200
        elif u_qq:
            data, page_msg = get_user_paginate(page, per_page, args=u_qq)
            return jsonify(data=data, page_msg=page_msg), 200
        elif u_statu:
            data, page_msg = get_user_paginate(page, per_page, args=u_statu)
            return jsonify(data=data, page_msg=page_msg), 200
        elif u_type:
            data, page_msg = get_user_paginate(page, per_page, args=u_type)
            return jsonify(data=data, page_msg=page_msg), 200
        else:
            pages = User.query.paginate(page=page, per_page=per_page,error_out=False)
            users = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next, 'next_num': pages.next_num, "prev_num": pages.prev_num}
            data = []
            for user in users:
                data.append(user.model_to_dict())
            return jsonify(data = data, page_msg=page_msg),200


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
        elif request.form.get('u_account'):
            account = request.form.get('u_account')
            password = request.form.get('u_password')
            repassword = request.form.get('u_repassword')
            user = User.query.filter_by(u_account=account).first()
            if user:
                u_password = user.u_password
                if password == u_password:
                    session['u_id'] = user.u_id
                    return jsonify({'msg': 'login success', 'code': 1000},
                                   user.model_to_dict()), 200
                else:
                    return jsonify(
                        {'msg': 'wrong password', 'code': 1001}), 200
            else:
                if password == repassword:
                    user = User()
                    user.u_account = account
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
def info_user():
    user = User()
    user.u_name = 'ab{}'.format(random.randint(1,100))
    user.u_phone = random.randint(10000000000,200000000000)
    user.u_account = 'ab{}'.format(random.randint(1,1000))
    user.u_type = 1
    user.regist_time = datetime.date.today()
    user.u_password = '123'
    user.u_statu = 1
    user.u_level = 1
    db.session.add(user)
    db.session.commit()