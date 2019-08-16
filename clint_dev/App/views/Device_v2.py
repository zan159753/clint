from flask import Blueprint, request, jsonify
from sqlalchemy import and_

from App.logics import get_device_paginate
from App.models import Device

devices_v2_api = Blueprint('devices_v2_api', __name__, url_prefix='/api/devices_v2/')


@devices_v2_api.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
# @check_login
def device_contro(page=None, per_page=None, number=None, name=None, city=None, clientNumber=None,state=None,gender=None):
    if request.method == 'GET':
        page = int(request.args.get('page',1))
        per_page = 50
        number = request.args.get('number')
        name = request.args.get('name')
        city = request.args.get('city')
        clientNumber = request.args.get('clientNumber')
        state = request.args.get('state')
        gender = request.args.get('gender')
        if name and city and clientNumber and state and gender:
            pages = Device.query.filter(
                and_(
                    Device.name == name,
                    Device.city == city,
                    Device.clientNumber == clientNumber,
                    Device.state == state,
                    Device.gender == gender,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 201
        elif name and city and clientNumber and state:
            pages = Device.query.filter(
                and_(
                    Device.name == name,
                    Device.city == city,
                    Device.clientNumber == clientNumber,
                    Device.state == state,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif name and city and clientNumber and gender:
            pages = Device.query.filter(
                and_(
                    Device.name == name,
                    Device.city == city,
                    Device.clientNumber == clientNumber,
                    Device.gender == gender,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif name and city and state and gender:
            pages = Device.query.filter(
                and_(
                    Device.name == name,
                    Device.city == city,
                    Device.state == state,
                    Device.gender == gender,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif name and clientNumber and state and gender:
            pages = Device.query.filter(
                and_(
                    Device.name == name,
                    Device.clientNumber == clientNumber,
                    Device.state == state,
                    Device.gender == gender,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif city and clientNumber and state and gender:
            pages = Device.query.filter(
                and_(
                    Device.city == city,
                    Device.clientNumber == clientNumber,
                    Device.state == state,
                    Device.gender == gender,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif name and city and clientNumber:
            pages = Device.query.filter(
                and_(
                    Device.city == city,
                    Device.name == name,
                    Device.clientNumber == clientNumber,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif name and city and state:
            pages = Device.query.filter(
                and_(
                    Device.city == city,
                    Device.name == name,
                    Device.state == state,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif name and city and gender:
            pages = Device.query.filter(
                and_(
                    Device.city == city,
                    Device.name == name,
                    Device.gender == gender,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif name and clientNumber and gender:
            pages = Device.query.filter(
                and_(
                    Device.clientNumber == clientNumber,
                    Device.name == name,
                    Device.gender == gender,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif name and clientNumber and state:
            pages = Device.query.filter(
                and_(
                    Device.clientNumber == clientNumber,
                    Device.name == name,
                    Device.state == state,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif name and gender and state:
            pages = Device.query.filter(
                and_(
                    Device.gender == gender,
                    Device.name == name,
                    Device.state == state,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif city and clientNumber and gender:
            pages = Device.query.filter(
                and_(
                    Device.city == city,
                    Device.clientNumber == clientNumber,
                    Device.gender == gender,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif city and state and gender:
            pages = Device.query.filter(
                and_(
                    Device.city == city,
                    Device.state == state,
                    Device.gender == gender,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif name and city:
            pages = Device.query.filter(
                and_(
                    Device.city == city,
                    Device.name == name,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif name and clientNumber:
            pages = Device.query.filter(
                and_(
                    Device.clientNumber == clientNumber,
                    Device.name == name,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif name and gender:
            pages = Device.query.filter(
                and_(
                    Device.gender == gender,
                    Device.name == name,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif name and state:
            pages = Device.query.filter(
                and_(
                    Device.state == state,
                    Device.name == name,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif city and clientNumber:
            pages = Device.query.filter(
                and_(
                    Device.clientNumber == clientNumber,
                    Device.city == city,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif city and gender:
            pages = Device.query.filter(
                and_(
                    Device.gender == gender,
                    Device.city == city,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif city and state:
            pages = Device.query.filter(
                and_(
                    Device.state == state,
                    Device.city == city,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif clientNumber and state:
            pages = Device.query.filter(
                and_(
                    Device.state == state,
                    Device.clientNumber == clientNumber,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif clientNumber and gender:
            pages = Device.query.filter(
                and_(
                    Device.gender == gender,
                    Device.clientNumber == clientNumber,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif state and gender:
            pages = Device.query.filter(
                and_(
                    Device.gender == gender,
                    Device.state == state,
                )).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif name:
            pages = Device.query.filter(
                    Device.name == name,
                ).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif city:
            pages = Device.query.filter(
                    Device.city == city,
                ).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif clientNumber:
            pages = Device.query.filter(
                    Device.clientNumber == clientNumber,
                ).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif state:
            pages = Device.query.filter(
                    Device.state == state,
                ).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif gender:
            pages = Device.query.filter(
                    Device.gender == gender,
                ).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        elif number:
            pages = Device.query.filter(
                    Device.number == number,
                ).paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 200
        else:
            pages = Device.query.paginate(
                page=page,
                per_page=per_page,
                error_out=False)
            data, page_msg = get_device_paginate(pages)
            return jsonify(data=data, page_msg=page_msg), 208

    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify({'msg':'method not allowed'}),200