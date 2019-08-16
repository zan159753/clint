from flask import Blueprint, request

mediaspag_themes_api = Blueprint("mediaspag_themes_api", __name__, url_prefix='/api/mediaspag_themes/')

@mediaspag_themes_api.route('/',methods=['GET','POST','PUT','DELETE'])
def mediaspag_themes_control():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        pass