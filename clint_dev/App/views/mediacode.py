# from flask import Blueprint, request
#
# from App.views import MyResponse
#
# mod = Blueprint('mod',__name__,template_folder='templates')
#
# """
# 多媒体上报同步查询接口
# //
# """
# @mod.route('/api/multimedia',methods = ['POST'])
# def multimedia():
#     if request.get_json() == None:
#         return MyResponse.responseErr(ERR_CODE_PARAM)
#     token = request.get_json().get('token')
#     #check token
#     devno = request.get_json().get('devno')
#     #查询这个设备
#     dev = Device.query.filter(Device.number == devno).first()
#     if(dev):
#         mediacode = dev.mediacode
#         # 'default'
#         #mediacode = 'm001'
#         if(mediacode == None or mediacode == 'None' or mediacode==''):
#             mediacode = 'm001'
#         multimediaresp =  MultiMediaResp(ERR_CODE_OK,mediacode)
#         print("devno:"+devno+",mediacode:"+mediacode)
#         return multimediaresp.JsonStr()
#     else:
#         return MyResponse.responseErr(ERR_CODE_NO_DEV)
# """
# 多媒体上报同步查询接口V2
# //
# """
# @mod.route('/api/multimedia2',methods = ['POST'])
# def multimedia2():
#     if(request.get_json() == None):
#         return MyResponse.responseErr(ERR_CODE_PARAM)
#     token = request.get_json().get('token')
#     #check token
#     devno = request.get_json().get('devno')
#     #查询这个设备
#     dev = Device.query.filter(Device.number == devno).first()
#     if(dev):
#         mediacode = dev.mediacode
#         # 'default'
#         # mediacode = 'm001'
#         if (mediacode == None or mediacode == 'None' or mediacode == ''):
#             mediacode = 'm001'
#         version = request.get_json().get('version')
#         #2版本支持主题
#         if(version == '2'):
#             multimediaresp =  MultiMediaRespV2(ERR_CODE_OK,mediacode)
#             print("v2 devno:"+devno+",mediacode:"+mediacode)
#             return multimediaresp.JsonStr()
#
#     else:
#         return MyResponse.responseErr(ERR_CODE_NO_DEV)
#
# """
# 多媒体文件下载接口
# // get
# """
# @mod.route('/api/multimedia/<string:mediacode>')
# def media(mediacode):
#     devno = request.args.get('devno')
#     filename = request.args.get('filename')
#     print("dev:%s get mediacode=%s, file=%s"%(devno,mediacode,filename))
#     logger_helper.logger.info("dev[%s] get mediacode=%s, file=%s", devno, mediacode, filename)
#     if request.method == 'GET':
#         if mediacode is None:
#             pass
#         else:
#             #logger.debug('filename is %s' % filename)
#             [dirname,fname] = os.path.split(filename)
#             if (fname.startswith("public_")):
#                 mediacode="public"
#             filename = "media/"+mediacode+"/"+request.args.get('filename')
#             if(mediacode != "public" and os.path.exists("media/"+mediacode+"/multimedia.json")):
#                 filename = "media/" + mediacode + "/v1/" + request.args.get('filename')
#             #image_data = open(os.path.join(app.config['UPLOAD_PATH'], 'files/%s' % filename), "rb").read()
#             image_data = open(filename, "rb").read()
#             response = make_response(image_data)
#             #'video/avi'
#             response.headers['Content-Type'] =  sltools.GetContentType(request.args.get('filename')) #'video/avi'
#             #response.headers['Content-Type'] = 'image/png'
#             return response
#     else:
#         pass
#     return  "ok"