from flask import Flask,session
from config import  Config
from flask_script import  Manager
from flask_sqlalchemy import  SQLAlchemy
from flask_migrate import  Migrate,MigrateCommand
from flask_session import  Session
from config import  config_dict





app = Flask(__name__)
app.config.from_object(Config)
app.config.from_object(config_dict['production'])

db =SQLAlchemy(app)
Migrate = Migrate(app)
manage=Manager(app)
manage.add_command('db',MigrateCommand)
Session()

@app.route('/')



def index():
    return 'hello world2'


if __name__ == '__main__':
    # app.run(debug=True)
    manage.run()
