# #encoding: utf-8
# import json
# from  models import  Device
# from  models import DevDynamic
# import GLOBAL
#
# def responseJson(errcode,errmsg):
#     resp = {}
#     resp['errCode'] = errcode
#     resp['errMsg'] = errmsg
#     json_str = json.dumps(resp)
#     print("json_str:"+json_str)
#     return json_str
#
# def responseSearchDev(errcode,errmsg,devs):
#     # {
#     # “errCode”: xx, ”errMsg”: ”xxxx”, "devs":[
#     #  { “lat”: ””, ”lng”: ””, ”loc”: ””, ”name”: ””},
#     # { “lat”: ””, ”lng”: ””, ”loc”: ””, ”name”: ””}
#     # ]
#     # }
#     resp = {}
#     resp['errCode'] = errcode
#     resp['errMsg'] = errmsg
#     resp['devs'] = []
#     for index in range(len(devs)):
#         obj = {}
#         obj['lat'] = str(devs[index].latitude/GLOBAL.GEO_FLOAT_TO_INT)
#         obj['lng'] = str(devs[index].longitude/GLOBAL.GEO_FLOAT_TO_INT)
#         obj['loc'] = devs[index].location
#         obj['name'] = devs[index].name
#         obj['number']=devs[index].number
#         dev = DevDynamic.query.filter(DevDynamic.number == devs[index].number).first()
#         if (dev):
#             obj['online'] = dev.state
#         else:
#             obj['online'] = 0
#         resp['devs'].append(obj)
#     json_str = json.dumps(resp)
#     print("json_str:"+json_str)
#     return json_str
#
# def responseUpdateMedia(result,mediacode,configcode,mainpic=None,video=None,subpic=None):
#     resp = {}
#     resp['result'] = result
#     resp['mediacode'] = mediacode
#     resp['mainpic'] = mainpic
#     resp['video'] = video
#     resp['subpic'] = subpic
#     json_str = json.dumps(resp)
#     return json_str
# def responseErr(result):
#     resp = {}
#     resp['result'] = result
#     json_str = json.dumps(resp)
#     return json_str
# # {“result”:1, ”mediacode”:”xxxx”, ”confilecode”:”xxxx”,
# # “mainpic”:[{“filename”:””}],
# # “video”:[{“filename”:””}],
# # “subpic”:[{“filename”:””}]
# # }
