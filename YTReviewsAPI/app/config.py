import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ytreviewsapi:a@database-2.cvebpou5jr9i.us-east-2.rds.amazonaws.com/ytreviewsapi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    APP_URL = os.environ.get('APP_URL') or 'http://localhost:5000'    