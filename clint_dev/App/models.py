import datetime

from App.ext import db


class User(db.Model):
    u_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    u_account = db.Column(db.String(32), unique=True)
    u_name = db.Column(db.String(32))
    u_phone = db.Column(db.String(32), unique=True)
    u_company = db.Column(db.String(64))
    u_wechat = db.Column(db.String(32), unique=True)
    u_qq = db.Column(db.String(32), unique=True,)
    u_chid = db.Column(db.String(256))
    u_chkey = db.Column(db.String(256))
    u_icon = db.Column(db.String(256))
    u_type = db.Column(db.Integer(),default=1)
    u_password = db.Column(db.String(256))
    regist_time = db.Column(db.Date)
    u_statu = db.Column(db.Integer(),default=1)
    u_level = db.Column(db.Integer(),default=1)

    def model_to_dict(self):
        # a = self.regist_time
        # a.strftime('%Y-%m-%d')
        return {'u_id': self.u_id, 'u_account': self.u_account, 'u_name': self.u_name,
                'u_phone': self.u_phone, 'u_company': self.u_company, 'u_wechat': self.u_wechat,
                'u_qq': self.u_qq, 'u_chid': self.u_chid, 'u_chkey': self.u_chkey, 'u_icon': self.u_icon,
                'u_type': self.u_type, 'u_password': self.u_password, 'regist_time': self.regist_time.strftime('%Y-%m-%d'),
                'u_statu': self.u_statu, 'u_level': self.u_level}


class Devices(db.Model):
    d_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_id = db.Column(db.Integer)
    d_code = db.Column(db.String(128), unique=True)
    d_name = db.Column(db.String(32))
    d_sex = db.Column(db.Integer)
    d_address = db.Column(db.String(32))
    d_type = db.Column(db.Integer)
    start_time = db.Column(db.Date)
    end_time = db.Column(db.Date)
    d_statu = db.Column(db.Integer)
    d_scheme_size = db.Column(db.String(32))
    m_id = db.Column(db.Integer)
    def model_to_dict(self):
        return {'d_id': self.d_id, 'u_id': self.u_id, 'd_code': self.d_code,
                'd_name': self.d_name, 'd_sex': self.d_sex, 'd_address': self.d_address,
                'd_type': self.d_type, 'start_time': self.start_time.strftime('%Y-%m-%d'), 'end_time': self.end_time.strftime('%Y-%m-%d'),
                'd_statu': self.d_statu, 'd_scheme_size': self.d_scheme_size, 'm_id':self.m_id
                }

class MediasPags:
    p_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_code = db.Column(db.String(64))

class MediasPag_Schemes:
    p_s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_id = db.Column(db.Integer)
    s_id = db.Column(db.Integer)


# class Medias(db.Model):
#     m_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     m_name = db.Column(db.String(32))
#     m_type = db.Column(db.Integer)
#     m_size = db.Column(db.String(32))
#     m_format = db.Column(db.String(16))
#     m_url = db.Column(db.String(256))
#     m_memory = db.Column(db.String(8))
#     u_id = db.Column(db.Integer)


class Schemes(db.Model):
    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(32))
    u_id = db.Column(db.Integer)


class AdvertisingOrders(db.Model):
    a_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_id = db.Column(db.Integer)
    a_life_time = db.Column(db.Integer)
    a_price = db.Column(db.Integer)
    a_pay_statu = db.Column(db.Integer)
    a_check_scheme_statu = db.Column(db.Integer)
    a_apply_time = db.Column(db.Date)
    a_pay_time = db.Column(db.Date)
    s_id = db.Column(db.Integer)
