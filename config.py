import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

#Gives access to the project in ANY OS we find ourselves in
#Allows outside files/folders to be added to the project
#from the base directory

load_dotenv(os.path.join(basedir, '.env'))

class Config():
    """
    Set Config vars for the flask app
    using envrioment vars where avail otherwise
    create the config vars if not done already
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #turn off update messages from sql