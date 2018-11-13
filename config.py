from redis import  StrictRedis
class Config:
    DEBUG= True
    SECRET_KEY='9CDgVJOpsP6pPdDfh+IAVxryAIj7ofuGCogzGCUS'
    SQLALCHEMY_DATABASE_URI ='mysql://root:mysql@localhost/info18'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SESSION_TYPE='redis'
    SESSION_REDIS = StrictRedis(host='127.0.0.1',port=6379)
    SEEION_USE_SIGNER=True
    PERMANENT_SESSION_LIFETIME=86400

class DevelopmentCongfig(Config):
    DEBUG =  True

class ProductionConfig(Config):
    DEBUG =  False

config_dict = {
    'development': DevelopmentCongfig,
    'production': ProductionConfig
}