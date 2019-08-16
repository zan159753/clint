import datetime
import os

from moviepy.editor import VideoFileClip
from PIL import Image
from flask import Blueprint, request, jsonify

from App.ext import db
from App.models import Themes, Medias

medias_api = Blueprint("medias_api", __name__, url_prefix='/api/medias/')

@medias_api.route('/',methods=['GET','POST','PUT','DELETE'])
def media_contro(page=None, per_page=None):
    if request.method == 'GET':
        t_id = request.args.get('t_id')
        media = Medias.query.filter_by(t_id=int(t_id))
        if media:
            data = []
            for m in media:
                data.append(m.model_to_dict())
            return jsonify(data=data)
        else:
            return jsonify({'msg':'media not found','code':1006}),200
    elif request.method == 'POST':
        t_id = request.form.get('t_id')
        m_type = request.form.get('m_type')
        mainpic = request.files.get('mainpic')
        video = request.files.get('video')
        largepic = request.files.get('largepic')
        if t_id:
            theme = Themes.query.get(t_id)
            theme_path = theme.t_url
            if m_type == '0':
                if mainpic:
                    pic_formate = mainpic.filename.split('.')[1]
                    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.' + pic_formate
                    file_path = theme_path + '/mainpic/' + filename
                    mainpic.save(file_path)
                    file_size = os.path.getsize(file_path)
                    im = Image.open(file_path)
                    media = Medias()
                    try:
                        media.m_type = 0
                        media.m_name = filename
                        media.m_size = str(im.size)
                        media.m_format = pic_formate
                        media.m_url = file_path
                        media.m_memory = str((file_size//1024))
                        media.t_id = t_id
                        db.session.add(media)
                        db.session.commit()
                        return jsonify({"msg": 'success'})
                    except:
                        os.remove(file_path)
                        return jsonify({"msg": "mysql error"})
                else:
                    return jsonify({'msg': 'not file'}), 400
            if m_type == '1':
                if video:
                    m_format = video.filename.split('.')[1]
                    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.' + m_format
                    file_path = theme_path + '/video/' + filename
                    video.save(file_path)
                    file_size = os.path.getsize(file_path)
                    media = Medias()
                    try:
                        media.m_type = 1
                        media.m_name = filename
                        media.m_format = m_format
                        media.m_url = file_path
                        media.m_memory = str((file_size // 1024))
                        media.t_id = t_id
                        db.session.add(media)
                        db.session.commit()
                        return jsonify({"msg": 'success'})
                    except:
                        os.remove(file_path)
                        return jsonify({"msg": "mysql error"})
                else:
                    return jsonify({'msg': 'not file'}), 400
        else:
            return jsonify({'msg': 'theme not found'}), 400
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        m_id = request.form.get('m_id')
        media = Medias.query.get(m_id)
        if media:
            m_url = media.m_url
            os.remove(m_url)
            db.session.delete(media)
            db.session.commit()
            return jsonify({"msg": "delete success"}), 200
        else:
            return jsonify({"msg": "media not found"}), 400
    else:
        return jsonify({'msg':'method not allowed'}), 400