import os
import shutil

from flask import Blueprint, request, jsonify

from App.ext import db
from App.logics import make_theme_file
from App.models import Themes, Medias

theme_api = Blueprint("theme_api", __name__, url_prefix='/api/themes/')

@theme_api.route('/',methods=['GET','POST','PUT','DELETE'])
def themes_contro(page=None,per_page=None):
    if request.method == 'GET':
        t_id = request.args.get('t_id')
        t_name = request.args.get('t_name')
        u_id = request.args.get('u_id')
        page = request.args.get('page',1)
        per_page = request.args.get('per_page',20)
        if t_id:
            theme = Themes.query.get(t_id)
            if theme:
                return jsonify(theme.model_to_dict())
            else:
                return jsonify({'msg':'not found'})
        elif t_name:
            theme = Themes.query.filter_by(t_name = t_name).first()
            if theme:
                return jsonify(theme.model_to_dict())
            else:
                return jsonify({'msg': 'not found'})
        elif u_id:
            theme = Themes.query.filter_by(u_id=u_id).first()
            if theme:
                return jsonify(theme.model_to_dict())
            else:
                return jsonify({'msg': 'not found'})
        else:
            pages = Themes.query.paginate(page=page,per_page=per_page,error_out=False)
            themes = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next, 'next_num': pages.next_num, "prev_num": pages.prev_num}
            data = []
            for theme in themes:
                data.append(theme.model_to_dict())
            return jsonify(data=data,page_msg=page_msg)
    elif request.method == 'POST':
        t_name = request.form.get('t_name')
        u_id = request.form.get('u_id')
        if t_name:
            theme = Themes()
            theme.t_name = t_name
            theme_path = make_theme_file(t_name)
            if theme_path :
                theme.t_url = theme_path
                db.session.add(theme)
                db.session.commit()
                return jsonify({'msg':'create theme success','code':1000}),200
            else:
                return jsonify({'msg':'repeat','code':1004}),400
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        t_id = request.form.get('t_id')
        medias = Medias.query.filter(Medias.t_id == t_id)
        theme = Themes.query.get(t_id)
        if theme:
            if medias:
                for media in medias:
                    db.session.delete(media)
                    db.session.commit()
                    theme = Themes.query.get(t_id)
                shutil.rmtree(theme.t_url)
                db.session.delete(theme)
                db.session.commit()
                return jsonify({'msg':'delete success'})
            else:
                shutil.rmtree(theme.t_url)
                db.session.delete(theme)
                db.session.commit()
                return jsonify({'msg': 'delete success'})
        else:
            return jsonify({'msg': 'no found theme'})

    else:
        return jsonify({'msg': 'method not allowed','code':1004}),404
