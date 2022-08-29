# Flask configuration

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

USER_APP_NAME = ""  
USER_ENABLE_EMAIL = True  
USER_ENABLE_USERNAME = True  
USER_EMAIL_SENDER_NAME = USER_APP_NAME
USER_EMAIL_SENDER_EMAIL = ""
USER_LOGIN_URL = '/login'
USER_LOGOUT_URL = '/logout'
SQLALCHEMY_DATABASE_URI ='postgresql://postgres:7928@localhost:5432/flask_logins'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SEND_FILE_MAX_AGE_DEFAULT = 0
TEMPLATES_AUTO_RELOAD = True
STATIC_AUTO_RELOAD = True
SECRET_KEY = environ.get('SECRET_KEY')
TEMPLATES= 'templates'
STATIC = 'static'
TESTING = True
DEBUG = True
FLASK_ENV = 'development'
BCRYPT_LOG_ROUNDS = 12
FLASK_APP = '/Users/mykahwalker/Desktop/app/app.py'
PORT = 5000
HOST = '127.0.0.1' 
DB_USER = 'postgres'
DB_PASSWORD = '7928'
ENV_PATH = '/Users/mykahwalker/Desktop/app/myvenv/lib/python3.10/site-packages'
SESSION_PERMANENT = False
SESSION_TYPE = "filesystem"
CORS_HEADERS = 'Content-Type'