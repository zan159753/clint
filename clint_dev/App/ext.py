from flask_caching import Cache
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
cache = Cache()


def init_ext(app):

    db.init_app(app=app)
    Session(app=app)
    migrate.init_app(app=app, db=db)
    cache.init_app(app=app)
