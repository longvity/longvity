from flask import Flask,session

from flask_script import  Manager

from flask_migrate import  Migrate,MigrateCommand

from  info import  create_app,db

app = create_app('development')



Migrate = Migrate(app)
manage=Manager(app)
manage.add_command('db',MigrateCommand)

@app.route('/')



def index():
    return 'hello world2'


if __name__ == '__main__':
    # app.run(debug=True)
    manage.run()
