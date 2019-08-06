import datetime
import random
import time

from flask import Blueprint, request, jsonify, session
from sqlalchemy import and_

from App.ext import db
from App.logics import get_device_paginate, info_user, check_login
from App.models import Devices, User

device_api = Blueprint('device_api', __name__, url_prefix='/api/devices/')


@device_api.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
# @check_login
def device_contro(page=None, per_page=None,d_id=None, d_code=None, d_name=None,
                  d_address=None, u_id=None, d_statu=None, d_sex=None):
    if request.method == 'GET':
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 50))
        d_code = request.args.get('d_code')
        d_name = request.args.get('d_name')
        d_address = request.args.get('d_address')
        u_id = request.args.get('u_id')
        d_statu = request.args.get('d_statu')
        d_sex = request.args.get('d_sex')

        if d_name and d_address and u_id and d_statu and d_sex:
            pages = Devices.query.filter(
                and_(
                    Devices.d_name == d_name,
                    Devices.d_address == d_address,
                    Devices.u_id == u_id,
                    Devices.d_statu == d_statu,
                    Devices.d_sex == d_sex,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_name and d_address and u_id and d_statu:
            pages = Devices.query.filter(
                and_(
                    Devices.d_name == d_name,
                    Devices.d_address == d_address,
                    Devices.u_id == u_id,
                    Devices.d_statu == d_statu,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_name and d_address and u_id and d_sex:
            pages = Devices.query.filter(
                and_(
                    Devices.d_name == d_name,
                    Devices.d_address == d_address,
                    Devices.u_id == u_id,
                    Devices.d_sex == d_sex,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_name and d_address and d_statu and d_sex:
            pages = Devices.query.filter(
                and_(
                    Devices.d_name == d_name,
                    Devices.d_address == d_address,
                    Devices.d_statu == d_statu,
                    Devices.d_sex == d_sex,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_name and u_id and d_statu and d_sex:
            pages = Devices.query.filter(
                and_(
                    Devices.d_name == d_name,
                    Devices.u_id == u_id,
                    Devices.d_statu == d_statu,
                    Devices.d_sex == d_sex,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_address and u_id and d_statu and d_sex:
            pages = Devices.query.filter(
                and_(
                    Devices.d_address == d_address,
                    Devices.u_id == u_id,
                    Devices.d_statu == d_statu,
                    Devices.d_sex == d_sex,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_name and u_id and d_address:
            pages = Devices.query.filter(
                and_(
                    Devices.d_name == d_name,
                    Devices.u_id == u_id,
                    Devices.d_address == d_address,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_statu and u_id and d_address:
            pages = Devices.query.filter(
                and_(
                    Devices.d_statu == d_statu,
                    Devices.u_id == u_id,
                    Devices.d_address == d_address,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_sex and u_id and d_address:
            pages = Devices.query.filter(
                and_(
                    Devices.d_sex == d_sex,
                    Devices.u_id == u_id,
                    Devices.d_address == d_address,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_statu and d_name and d_address:
            pages = Devices.query.filter(
                and_(
                    Devices.d_statu == d_statu,
                    Devices.d_name == d_name,
                    Devices.d_address == d_address,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_statu and u_id and d_name:
            pages = Devices.query.filter(
                and_(
                    Devices.d_statu == d_statu,
                    Devices.u_id == u_id,
                    Devices.d_name == d_name,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_sex and d_name and d_address:
            pages = Devices.query.filter(
                and_(
                    Devices.d_sex == d_sex,
                    Devices.d_name == d_name,
                    Devices.d_address == d_address,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_sex and d_name and u_id:
            pages = Devices.query.filter(
                and_(
                    Devices.d_sex == d_sex,
                    Devices.d_name == d_name,
                    Devices.u_id == u_id,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_name and u_id:
            pages = Devices.query.filter(
                and_(
                    Devices.d_name == d_name,
                    Devices.u_id == u_id,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_name and d_address:
            pages = Devices.query.filter(
                and_(
                    Devices.d_name == d_name,
                    Devices.d_address == d_address,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_name and d_statu:
            pages = Devices.query.filter(
                and_(
                    Devices.d_name == d_name,
                    Devices.d_statu == d_statu,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_name and d_sex:
            pages = Devices.query.filter(
                and_(
                    Devices.d_name == d_name,
                    Devices.d_sex == d_sex,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif u_id and d_address:
            pages = Devices.query.filter(
                and_(
                    Devices.u_id == u_id,
                    Devices.d_address == d_address,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif u_id and d_statu:
            pages = Devices.query.filter(
                and_(
                    Devices.u_id == u_id,
                    Devices.d_statu == d_statu,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif u_id and d_sex:
            pages = Devices.query.filter(
                and_(
                    Devices.u_id == u_id,
                    Devices.d_sex == d_sex,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_statu and d_address:
            pages = Devices.query.filter(
                and_(
                    Devices.d_statu == d_statu,
                    Devices.d_address == d_address,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_sex and d_address:
            pages = Devices.query.filter(
                and_(
                    Devices.d_sex == d_sex,
                    Devices.d_address == d_address,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_statu and d_sex:
            pages = Devices.query.filter(
                and_(
                    Devices.d_statu == d_statu,
                    Devices.d_sex == d_sex,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_code:
            pages = Devices.query.filter(
                Devices.d_code == d_code
            ).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_name:
            pages = Devices.query.filter(
                Devices.d_name == d_name
            ).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_address:
            pages = Devices.query.filter(
                Devices.d_address == d_address,
            ).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif u_id:
            pages = Devices.query.filter(
                Devices.u_id == u_id).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_statu:
            pages = Devices.query.filter(
                Devices.d_statu == d_statu,
            ).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif d_sex:
            pages = Devices.query.filter(
                Devices.d_sex == d_sex,
            ).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        # elif d_id:
        #     pages = Devices.query.filter(
        #         Devices.d_id == d_id,
        #     ).paginate(
        #         page=page,
        #         per_page=per_page,
        #         error_out=False)
        #     data, page_msg = get_device_paginate(pages)
        #     return jsonify(data=data, page_msg=page_msg), 200
        else:
            pages = Devices.query.filter().paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200

    elif request.method == 'POST':
        device = Devices()
        code = request.form.get('d_code')
        name = request.form.get('d_name')
        sex = request.form.get('d_sex')
        address = request.form.get('d_address')
        type = request.form.get('d_type')
        statu = request.form.get('d_statu')
        start_time = datetime.date.today()
        if name and sex and address and type and statu and start_time and code:
            if Devices.query.filter_by(d_code=code).all():
                return jsonify(
                    {'msg': '{} is using'.format(code), 'code': 1005}), 404
            else:
                device.d_code = code
                device.d_sex = sex
                device.d_type = type
                device.start_time = start_time
                device.d_name = name
                device.d_statu = statu
                device.d_address = address
                db.session.add(device)
                db.session.commit()
                return jsonify({'msg':'添加成功','code':1000}),200

    elif request.method == 'PUT':

        d_name = request.form.get('d_name')
        d_sex = request.form.get('d_sex')
        d_address = request.form.get('d_address')
        d_statu = request.form.get('d_statu')
        d_type = request.form.get('d_type')
        end_time = request.form.get('end_time')
        u_id = request.form.get('u_id')
        d_id = request.form.get('d_id')
        m_id = request.form.get('m_id')
        d_scheme_size = request.form.get('d_scheme_size')
        device = Devices.query.get(d_id)

        if device:
            if d_name:
                device.d_name = d_name
                db.session.add(device)
            if d_sex:
                device.d_sex = int(d_sex)
                db.session.add(device)
            if d_address:
                device.d_address = d_address
                db.session.add(device)
            if d_statu:
                device.d_statu = int(d_statu)
                db.session.add(device)
            if d_type:
                device.d_type = int(d_type)
                db.session.add(device)
            if end_time:
                device.end_time = time.strptime(end_time, "%Y-%m-%d")
                db.session.add(device)
            if u_id:
                device.u_id = u_id
                db.session.add(device)
            if m_id:
                device.m_id = int(m_id)
                db.session.add(device)
            if d_scheme_size:
                device.d_scheme_size = d_scheme_size
                db.session.add(device)
            db.session.commit()
            return jsonify({'msg': 'success'})
        else:
            return jsonify({'msg': 'no device'}), 200

    elif request.method == 'DELETE':
        u_id = session['u_id']
        user = User.query.get(u_id)
        u_level = user.u_level
        print(user.u_name,user.u_level)
        if u_level == 0:
            d_id = request.form.get('d_id')
            device = Devices.query.get(d_id)
            if device:
                device.u_id = None
                device.d_statu = 0
                db.session.add(device)
                db.session.commit()
            else:
                return jsonify({'msg': 'no device', 'code': 1001}), 404
            return jsonify({'msg': 'delete sccuess', 'code': 1000}), 200
        else:
            return jsonify({'msg': 'no root'}), 200
    else:
        return jsonify({'msg': 'wrong method', 'code': 1009}), 404

# def add_device():
#     l = [1,2]
#     l2 = [1,2,3,4]
#     l3 = [1,2,3,4]
#     l4 = [i for i in range(1,31)]
#     d = Devices()
#     d.d_name = 'ab{}'.format(random.randint(1,100))
#     d.d_code = random.randint(10000000000,200000000000)
#     d.d_sex = random.choice(l)
#     d.d_address = random.choice(l2)
#     d.d_type = random.choice(l3)
#     d.u_id = random.choice(l4)
#     d.start_time = datetime.date.today()
#     d.end_time = d.start_time + datetime.timedelta(days=30)
#     d.d_statu = random.choice(l)
#     db.session.add(d)
#     db.session.commit()
