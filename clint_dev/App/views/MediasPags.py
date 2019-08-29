from flask import Blueprint, request, jsonify

from App.ext import db
from App.models import MediasPags, MediasPag_themes

mediaspags_api = Blueprint("mediaspags_api", __name__, url_prefix='/project1/api/mediaspags/')

@mediaspags_api.route('/',methods=['GET','POST','PUT','DELETE'])
def mediapags_control(page=None,per_page=None,p_code=None):
    if request.method == 'GET':
        page = int(request.args.get('page',1))
        per_page = int(request.args.get('per_page',20))
        p_code = request.args.get('p_code')
        if p_code:
            mediapage = MediasPags.query.filter_by(p_code=p_code).first()
            print(mediapage.model_to_dict())
            data = []
            data.append(mediapage.model_to_dict())
            return jsonify(data=data),200
        else:
            pages = MediasPags.query.paginate(page=page, per_page=per_page,error_out=False)
            mediaspags = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next, 'next_num': pages.next_num, "prev_num": pages.prev_num}
            data = []
            for mediapage in mediaspags:
                data.append(mediapage.model_to_dict())
            return jsonify(data=data, page_msg=page_msg)

    elif request.method == 'POST':
        p_code = request.form.get('p_code')
        mediaspag = MediasPags.query.filter_by(p_code=p_code).first()
        if not mediaspag:
            if p_code:
                mediapag = MediasPags()
                mediapag.p_code = p_code
                db.session.add(mediapag)
                db.session.commit()
                return jsonify({"msg": 'add success' }),200
            else:
                return jsonify({'msg':'not found p_code','code':1004}),400
        else:
            return jsonify({'msg':'重复编号'}),400
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        p_id = request.form.get('id')
        mediasPag = MediasPags.query.get(p_id)
        mediasPag_themes = MediasPag_themes.query.filter_by(p_id=p_id).all()
        if mediasPag:
            if mediasPag_themes:
                for mediasPag_theme in mediasPag_themes:
                    db.session.delete(mediasPag_theme)
                    db.session.commit()
                db.session.delete(mediasPag)
                db.session.commit()
                return jsonify({"msg":'delete success'}),200
            else:
                db.session.delete(mediasPag)
                db.session.commit()
                return jsonify({"msg": 'delete success'}),200
        else:
            return jsonify({"msg": "mediasPag not found"}),400
    else:
        return jsonify({'msg':'method not allowed','code':1004}),400