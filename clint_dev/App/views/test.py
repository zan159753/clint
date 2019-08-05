import datetime
import json
import random

import requests
from flask import request, jsonify
from sqlalchemy import or_, and_

from App.ext import db
from App.models import User
from App import config as cfg


def info_user():
    user = User()
    user.u_name = 'ab{}'.format(random.randint(1,100))
    user.u_phone = random.randint(10000000000,200000000000)
    user.u_account = 'ab{}'.format(random.randint(1,1000))
    user.u_type = cfg.ADVERTISING_USERS
    user.regist_time = datetime.date.today()
    user.u_password = '123'
    user.u_statu = cfg.NORMAL_USER
    user.u_level = 1
    db.session.add(user)
    db.session.commit()

