import datetime

from App.ext import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'mysql_collate':'utf8_general_ci'}
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50),nullable=False,unique=True)
    password = db.Column(db.String(100),nullable=False)

    def model_to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'password':self.password
                }


class ClientInfo(db.Model):
    __tablename__ = 'client'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(32), nullable=False, unique=True)
    loginName = db.Column(db.String(50), nullable=False, unique=True)
    loginPwd = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(32), default='')
    email = db.Column(db.String(100), default='')
    type = db.Column(db.Integer, default=0)
    level = db.Column(db.Integer, default=0)
    nature = db.Column(db.String(50), default='')
    chId = db.Column(db.String(50), default='')
    chKey = db.Column(db.String(50), default='')
    salemanId = db.Column(db.String(32), default='')
    remark = db.Column(db.Text)
    devices = db.relationship('Device', backref=db.backref('clientInfo'))

    def __repr__(self):
        return '<client:%s %s %s>' % (self.number, self.loginName, self.loginPwd)

    def model_to_dict(self):
        return {
            'id': self.id,
            'number': self.number,
            'loginName': self.loginName,
            'loginPwd': self.loginPwd,
            'phone': self.phone,
            'email': self.email,
            'type': self.type,
            'level': self.level,
            'nature': self.nature,
            'chId': self.chId,
            'chKey': self.chKey,
            'salemanId': self.salemanId,
            'remark': self.remark,

        }


class Device(db.Model):
    __tablename__ = 'device'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    clientNumber = db.Column(db.String(32), db.ForeignKey('client.number'))
    number = db.Column(db.String(32), nullable=False, unique=True)
    name = db.Column(db.String(32), nullable=False)
    province = db.Column(db.String(50))
    city = db.Column(db.String(50))
    district = db.Column(db.String(50))
    location = db.Column(db.String(50))
    # float小数点的位数精度不够改为Int型
    latitude = db.Column(db.Integer, default=0)
    longitude = db.Column(db.Integer, default=0)
    state = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    type = db.Column(db.String(50), default='')
    mediacode = db.Column(db.String(50), default='m001')
    # 销售城市
    salecity = db.Column(db.String(50), default='')
    # clientNumber varchar(32) , product_time datetime, carnum varchar(50) default '',gender int(11) default 2, remark TEXT
    product_time = db.Column(db.DateTime, default=datetime.datetime.now)
    carnum = db.Column(db.String(50), default='')
    gender = db.Column(db.Integer, default=2)
    version = db.Column(db.String(50), default='')
    updatefile = db.Column(db.String(128), default='')
    # 规格 15寸，21寸，24寸
    spec = db.Column(db.String(50), default='')
    remark = db.Column(db.Text)

    def getRegistData(self):
        msg = {}
        msg["devno"] = self.number
        msg['ctime'] = self.create_time.strftime("%Y-%m-%d %H:%M:%S")
        locat = {}
        locat['p'] = self.province
        locat['c'] = self.city
        locat['s'] = self.district
        msg['location'] = locat
        return msg

    def checkRegCity(self):
        if (self.salecity == None or self.salecity == '' or self.city == self.salecity or (
                -1 != self.location.find(self.salecity))):
            return 1
        return 0

    def model_to_dict(self):
        try:
            create_time = self.create_time.strftime('%Y-%m-%d')
        except:
            create_time = None
        try:
            product_time = self.product_time.strftime('%Y-%m-%d')
        except:
            product_time = None
        return {
            'id': self.id,
            'clientNumber': self.clientNumber,
            'number': self.number,
            'name': self.name,
            'province': self.province,
            'city': self.city,
            'district': self.district,
            'location': self.location,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'state': self.state,
            'create_time': create_time,
            'type': self.type,
            'mediacode': self.mediacode,
            'salecity': self.salecity,
            'product_time': product_time,
            'carnum': self.carnum,
            'gender': self.gender,
            'version': self.version,
            'updatefile': self.updatefile,
            'spec': self.spec,
            'remark': self.remark,
        }

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


class MediasPags(db.Model):
    p_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_code = db.Column(db.String(64),unique=True)
    p_type = db.Column(db.Integer(), default=0)
    def model_to_dict(self):
        return {
            'p_id': self.p_id,
            'p_code': self.p_code,
            'p_type': self.p_type,
        }

class MediasPag_themes(db.Model):
    p_t_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_id = db.Column(db.Integer())
    t_id = db.Column(db.Integer())
    p_t_week = db.Column(db.Integer(),default=0)

    def model_to_dict(self):
        return {
            'p_t_id': self.p_t_id,
            'p_id': self.p_id,
            't_id': self.t_id,
            'p_t_week': self.p_t_week,
        }

#
class Medias(db.Model):
    m_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    m_name = db.Column(db.String(32))
    m_type = db.Column(db.Integer)
    m_size = db.Column(db.String(32))
    m_format = db.Column(db.String(16))
    m_url = db.Column(db.String(256))
    m_memory = db.Column(db.String(32))
    u_id = db.Column(db.Integer)
    t_id = db.Column(db.Integer())
    m_upload_time = db.Column(db.DateTime(), default=datetime.datetime.now())

    def model_to_dict(self):
        try:
            m_upload_time = self.m_upload_time.strftime('%Y-%m-%d')
        except:
            m_upload_time = None

        return {
            'm_id':self.m_id,
            'm_name':self.m_name,
            'm_type':self.m_type,
            'm_size':self.m_size,
            'm_format':self.m_format,
            'm_url':self.m_url,
            'm_memory':self.m_memory,
            'u_id':self.u_id,
            't_id':self.t_id,
            'm_upload_time':self.m_upload_time,
        }


class Themes(db.Model):
    t_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    t_name = db.Column(db.String(32), unique=True)
    u_id = db.Column(db.Integer())
    t_url = db.Column(db.String(256))
    t_pic_loop = db.Column(db.Integer(),default=5)
    t_vedio_loop = db.Column(db.Integer(),default=15)
    t_type = db.Column(db.Integer(),default=0)
    def model_to_dict(self):
        return {'t_id': self.t_id, 't_name': self.t_name, 'u_id': self.u_id,
                't_url': self.t_url, 't_pic_loop': self.t_pic_loop ,
                't_vedio_loop': self.t_vedio_loop ,'t_type':self.t_type,
                }


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
