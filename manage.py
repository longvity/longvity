from flask import Flask,session

from flask_script import  Manager

from flask_session import  Session


from redis import  StrictRedis



app = Flask(__name__)
app.config['SECRET_KEY']='9CDgVJOpsP6pPdDfh+IAVxryAIj7ofuGCogzGCUS'
app.config['SESSION_TYPE']='redis'
app.config['SESSION_REDIS']=StrictRedis(host='127.0.0.1',port=6379)
app.config['SEEION_USE_SIGNER']=True
app.config['PERMANENT_SESSION_LIFETIME']=86400

manage=Manager(app)
Session()

@app.route('/')



def index():
    return 'hello world2'


if __name__ == '__main__':
    # app.run(debug=True)
    manage.run()
