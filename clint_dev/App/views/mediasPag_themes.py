from flask import Blueprint, request, jsonify
from sqlalchemy import and_

from App.ext import db
from App.models import MediasPags, MediasPag_themes, Themes

mediaspag_themes_api = Blueprint("mediaspag_themes_api", __name__, url_prefix='/project1/api/mediaspag_themes/')

@mediaspag_themes_api.route('/',methods=['GET','POST','PUT','DELETE'])
def mediaspag_themes_control():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        p_id = request.form.get('p_id')
        print(p_id)
        t_name = request.form.get('t_name')
        print(t_name)
        mediaspag = MediasPags.query.get(p_id)
        theme = Themes.query.filter_by(t_name = t_name).first()
        if mediaspag and theme:
            if MediasPag_themes.query.filter(and_(MediasPag_themes.p_id == p_id,MediasPag_themes.t_id == theme.t_id)).first():
                return jsonify({"msg": "repeat"}),200
            else:
                mediaspag_themes = MediasPag_themes()
                mediaspag_themes.p_id = p_id
                mediaspag_themes.t_id = theme.t_id
                db.session.add(mediaspag_themes)
                db.session.commit()
                return jsonify({'msg':'add succese'}),200
        else:
            return jsonify({"msg": "error"}),400
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        p_id = request.form.get('p_id')
        t_id = request.form.get('t_id')
        mediaspag_theme = MediasPag_themes.query.filter(and_(MediasPag_themes.p_id==p_id,MediasPag_themes.t_id==t_id)).first()
        if mediaspag_theme:
            db.session.delete(mediaspag_theme)
            db.session.commit()
            return jsonify({"msg": "succese"}), 200
        else:
            return jsonify({"msg": "not found mediaspag_theme"}),400
    else:
        return jsonify({"msg": "method not allowed"}), 400