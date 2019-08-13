from flask import Blueprint, request

medias_api = Blueprint("medias_api", __name__, url_prefix='/api/medias/')

@medias_api.route('/',methods=['GET','POST','PUT','DELETE'])
def media_contro():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        mainpic = request.files.get('mainpic')
        video = request.files.get('video')
        largepic = request.files.get('largepic')
        pass

    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        pass