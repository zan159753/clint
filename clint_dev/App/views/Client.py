from flask import Blueprint, request, jsonify, render_template
from sqlalchemy import and_

from App.ext import db
from App.models import ClientInfo

client_api = Blueprint("client_api", __name__, url_prefix='/project1/api/client/')
client_add_api = Blueprint("client_add_api", __name__, url_prefix='/project1/client_add/')
client_put_api = Blueprint("client_put_api", __name__, url_prefix='/project1/client_put/')

@client_put_api.route('/')
def to_client_put():
    return render_template('client-put.html')

@client_add_api.route('/')
def to_client_add():
    return render_template('client-add.html')

@client_api.route('/',methods=['GET','POST','PUT','DELETE','PATCH'])
def client_contro(page=None,per_page=None, id=None, loginName=None, number=None, phone=None, email=None, type=None, nature=None, salemanId=None):
    if request.method == 'GET':
        page = int(request.args.get('page',1))
        per_page = int(request.args.get('per_page',10))
        id = request.args.get('id')
        number = request.args.get('number')
        loginName = request.args.get('loginName')
        phone = request.args.get('phone')
        email = request.args.get('email')
        type = request.args.get('type ')
        nature = request.args.get('nature')
        salemanId = request.args.get('salemanId')
        level = request.args.get('level')
        if nature and type and level:
            pages = ClientInfo.query.filter_by(and_(nature=nature,type=type,level=level)).paginate(page=page, per_page = per_page, error_out=False)
            clients = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next}
            data = []
            for client in clients:
                data.append(client.model_to_dict())
            return jsonify(data=data, page_msg=page_msg), 200
        elif nature and type:
            pages = ClientInfo.query.filter_by(and_(nature=nature, type=type)).paginate(page=page, per_page=per_page, error_out=False)
            clients = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next}
            data = []
            for client in clients:
                data.append(client.model_to_dict())
            return jsonify(data=data, page_msg=page_msg), 200
        elif nature and level:
            pages = ClientInfo.query.filter_by(and_(nature=nature, level=level)).paginate(page=page, per_page=per_page,
                                                                                        error_out=False)
            clients = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next}
            data = []
            for client in clients:
                data.append(client.model_to_dict())
            return jsonify(data=data, page_msg=page_msg), 200
        elif type and level:
            pages = ClientInfo.query.filter_by(and_(type=type, level=level)).paginate(page=page, per_page=per_page,
                                                                                        error_out=False)
            clients = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next}
            data = []
            for client in clients:
                data.append(client.model_to_dict())
            return jsonify(data=data, page_msg=page_msg), 200
        elif level:
            pages = ClientInfo.query.filter_by(level=level).paginate(page=page, per_page=per_page,
                                                                                        error_out=False)
            clients = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next}
            data = []
            for client in clients:
                data.append(client.model_to_dict())
            return jsonify(data=data, page_msg=page_msg), 200
        elif type:
            pages = ClientInfo.query.filter_by(type=type).paginate(page=page, per_page=per_page,
                                                                                        error_out=False)
            clients = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next}
            data = []
            for client in clients:
                data.append(client.model_to_dict())
            return jsonify(data=data, page_msg=page_msg), 200
        elif nature:
            pages = ClientInfo.query.filter_by(nature=nature).paginate(page=page, per_page=per_page,
                                                                                        error_out=False)
            clients = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next}
            data = []
            for client in clients:
                data.append(client.model_to_dict())
            return jsonify(data=data, page_msg=page_msg), 200
        elif number:
            pages = ClientInfo.query.filter_by(number=number).paginate(page=page, per_page=per_page,
                                                                                      error_out=False)
            clients = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next}
            data = []
            for client in clients:
                data.append(client.model_to_dict())
            return jsonify(data=data, page_msg=page_msg), 200
        elif phone:
            pages = ClientInfo.query.filter_by(phone=phone).paginate(page=page, per_page=per_page,
                                                                                      error_out=False)
            clients = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next}
            data = []
            for client in clients:
                data.append(client.model_to_dict())
            return jsonify(data=data, page_msg=page_msg), 200
        elif loginName:
            pages = ClientInfo.query.filter_by(loginName=loginName).paginate(page=page, per_page=per_page,
                                                                                      error_out=False)
            clients = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next}
            data = []
            for client in clients:
                data.append(client.model_to_dict())
            return jsonify(data=data, page_msg=page_msg), 200
        elif email:
            pages = ClientInfo.query.filter_by(email=email).paginate(page=page, per_page=per_page,
                                                                                      error_out=False)
            clients = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next}
            data = []
            for client in clients:
                data.append(client.model_to_dict())
            return jsonify(data=data, page_msg=page_msg), 200
        elif salemanId:
            pages = ClientInfo.query.filter_by(salemanId=salemanId).paginate(page=page, per_page=per_page,
                                                                                      error_out=False)
            clients = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next}
            data = []
            for client in clients:
                data.append(client.model_to_dict())
            return jsonify(data=data, page_msg=page_msg), 200
        else:
            pages = ClientInfo.query.paginate(page=page, per_page=per_page,
                                                                             error_out=False)
            clients = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next}
            data = []
            for client in clients:
                data.append(client.model_to_dict())
            return jsonify(data=data, page_msg=page_msg), 200

    elif request.method == 'POST':
        loginName = request.form.get('loginName')
        number = request.form.get('number')
        phone = request.form.get('phone')
        loginPwd = request.form.get('loginPwd')
        if loginName and number and phone and loginPwd:
            if ClientInfo.query.filter_by(number=number).all():
                return jsonify(
                    {'msg': '{} is using'.format(number), 'code': 1005}), 404
            elif ClientInfo.query.filter_by(loginName=loginName).all():
                return jsonify(
                    {'msg': '{} is using'.format(loginName), 'code': 1005}), 404
            else:
                client = ClientInfo()
                client.loginName = loginName
                client.number = number
                client.phone = phone
                client.loginPwd = loginPwd
                db.session.add(client)
                db.session.commit()
                return jsonify({'msg':'create client success'}),200
        else:
            return jsonify({'msg': 'error'}), 200
    elif request.method == 'PUT':
        id = request.form.get('id')
        loginPwd = request.form.get('loginPwd')
        phone = request.form.get('phone')
        email = request.form.get('email')
        type = request.form.get('type')
        level = request.form.get('level')
        nature = request.form.get('nature')
        chId = request.form.get('chId')
        chKey = request.form.get('chKey')
        remark = request.form.get('remark')
        client = ClientInfo.query.get(id)
        if client:
            if loginPwd:
                client.loginPwd = loginPwd
                db.session.add(client)
            if phone:
                client.phone = phone
                db.session.add(client)
            if email:
                client.email = email
                db.session.add(client)
            if type:
                client.type = type
                db.session.add(client)
            if level:
                client.level = level
                db.session.add(client)
            if nature:
                client.nature = nature
                db.session.add(client)
            if chKey:
                client.chKey = chKey
                db.session.add(client)
            if chId:
                client.chId = chId
                db.session.add(client)
            if remark:
                client.remark = remark
                db.session.add(client)
            db.session.commit()
            return jsonify({'msg': 'success'})
        else:
            return jsonify({'msg': 'no client'}), 200
    elif request.method == 'DELETE':
        id = request.form.get('id')
        client = ClientInfo.query.get(id)
        if client:
            client.level = 99
            db.session.add(client)
            db.session.commit()
            return jsonify({'msg':'delete success'}),200
        else:
            return jsonify({'msg': 'no client'}), 400
    elif request.method == 'PATCH':
        if request.form.get('id'):
            id = request.form.get('id')
            client = ClientInfo.query.get(id)
            if client:
                client.level = 0
                db.session.add(client)
                try:
                    db.session.commit()
                    return jsonify(
                        {'msg': 'client write-off', 'code': 1000}), 202
                except:

                    return jsonify({'msg': 'delete error', 'code': 1004}), 404
            else:

                return jsonify({'msg': 'no client', 'code': 1004}), 404
        else:

            return jsonify({'msg': 'no id', 'code': 1004}), 404
    else:
        return jsonify({'msg':'no method'}), 400