import os
import shutil

from flask import Blueprint, request, jsonify

from App.ext import db
from App.logics import make_theme_file, add_config
from App.models import Themes, Medias, MediasPag_themes

theme_api = Blueprint("theme_api", __name__, url_prefix='/project1/api/themes/')

@theme_api.route('/',methods=['GET','POST','PUT','DELETE'])
def themes_contro(page=None,per_page=None,t_name=None,p_id=None,u_id=None):
    if request.method == 'GET':
        t_id = request.args.get('t_id')
        t_name = request.args.get('t_name')
        p_id = request.args.get('p_id')
        u_id = request.args.get('u_id')
        page = int(request.args.get('page',1))
        per_page = int(request.args.get('per_page',20))
        if t_id:
            theme = Themes.query.get(t_id)
            if theme:
                data = []
                data.append(theme.model_to_dict())
                return jsonify(data=data),200
            else:
                return jsonify({'msg':'not found'}),200
        elif t_name:
            theme = Themes.query.filter_by(t_name = t_name).first()
            if theme:
                data = []
                data.append(theme.model_to_dict())
                return jsonify(data=data),200
            else:
                return jsonify({'msg': 'not found'}),200
        elif u_id:
            theme = Themes.query.filter_by(u_id=u_id).first()
            if theme:
                data = []
                data.append(theme.model_to_dict())
                return jsonify(data=data),200
            else:
                return jsonify({'msg': 'not found'}),200
        elif p_id:
            mediaspag_themes = MediasPag_themes.query.filter_by(p_id=p_id).all()
            t_ids = []
            for mediaspag_theme in mediaspag_themes:
                 t_ids.append(mediaspag_theme.t_id)
            try:
                pages = Themes.query.filter(Themes.t_id.in_(t_ids)).paginate(page=page,per_page=per_page,error_out=False)
            except:
                return jsonify({"msg": "error"}), 200
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next, 'next_num': pages.next_num, "prev_num": pages.prev_num}
            themes = pages.items
            if themes:
                data = []
                for theme in themes:
                    data.append(theme.model_to_dict())
                return jsonify(data=data,page_msg=page_msg),200
            else:
                return jsonify({'msg': 'not found'}),200
        else:
            pages = Themes.query.paginate(page=page,per_page=per_page,error_out=False)
            themes = pages.items
            page_msg = {'total_page': pages.pages, 'current_page': pages.page, 'has_prev': pages.has_prev,
                        'has_next': pages.has_next, 'next_num': pages.next_num, "prev_num": pages.prev_num}
            data = []
            for theme in themes:
                data.append(theme.model_to_dict())
            return jsonify(data=data,page_msg=page_msg),200
    elif request.method == 'POST':
        t_name = request.form.get('t_name')
        u_id = request.form.get('u_id')
        if t_name:
            theme = Themes()
            theme.t_name = t_name
            theme_path = make_theme_file(t_name)
            theme_static_path = theme_path.split('clint_dev')[1]
            if theme_path :
                theme.t_url = theme_static_path
                db.session.add(theme)
                db.session.commit()
                return jsonify({'msg':'create theme success','code':1000}),200
            else:
                return jsonify({'msg':'repeat','code':1004}),200
    elif request.method == 'PUT':
        t_name = request.form.get('t_name')
        pic_loop = request.form.get('t_pic_loop')
        vedio_loop = request.form.get('t_vedio_loop')
        t_id = request.form.get('t_id')
        try:
            theme = Themes.query.get(t_id)
        except:
            theme = None
        if theme:
            if pic_loop != theme.t_pic_loop:
                add_config(pic_loop=pic_loop,vedio_loop=vedio_loop,theme_url=os.getcwd()+theme.t_url)
                theme.t_pic_loop = pic_loop
                theme.t_vedio_loop = vedio_loop
                db.session.add(theme)
            db.session.commit()
            return jsonify({'msg': 'success'}), 200
        else:
            return jsonify({"msg": "error"}), 400
    elif request.method == 'DELETE':
        t_id = request.form.get('t_id')
        medias = Medias.query.filter(Medias.t_id == t_id)
        theme = Themes.query.get(t_id)
        mediaspage_themes = MediasPag_themes.query.filter_by(t_id=t_id).all()
        if theme:
            if mediaspage_themes:
                for mediaspage_theme in mediaspage_themes:
                    db.session.delete(mediaspage_theme)
                    db.session.commit()
            if medias:
                for media in medias:
                    db.session.delete(media)
                    db.session.commit()
                    theme = Themes.query.get(t_id)
                shutil.rmtree(os.getcwd() + theme.t_url)
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
