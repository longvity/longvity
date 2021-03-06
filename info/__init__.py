from flask import  Flask
from config import  config_dict
from flask_sqlalchemy import  SQLAlchemy

from flask_session import  Session

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_dict[config_name])

    db.init_app(app)

    Session(app)

    from  info.modules.news import  news_blue
    app.register_blueprint(news_blue)




    return  app
