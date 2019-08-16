from flask import Blueprint, request, jsonify

from App.ext import db
from App.models import MediasPags

mediaspags_api = Blueprint("mediaspags_api", __name__, url_prefix='/api/mediaspags/')

@mediaspags_api.route('/',methods=['GET','POST','PUT','DELETE'])
def mediapags_control():
    if request.method == 'GET':
        p_code = request.args.get('p_code')
        page = request.args.get('page')
        per_page = request.args.get('per_page')
        if p_code:
            mediapage = MediasPags.query.filter(p_code=p_code).first()
            return jsonify({mediapage.model_to_dict()}),200
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
        if p_code:
            mediapag = MediasPags()
            mediapag.p_code = p_code
            db.session.add(mediapag)
            db.session.commit()
        else:
            return jsonify({'msg':'not found p_code','code':1004}),400
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify({'msg':'method not allowed','code':1004}),400