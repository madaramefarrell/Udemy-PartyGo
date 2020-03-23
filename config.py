import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

basedir = os.path.dirname(os.path.abspath(__file__))


class Config:
    MONGODB_SETTINGS = os.environ.get('MONGODB_SETTINGS')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    PROJECT_ID = os.environ.get('PROJECT_ID')
    CLOUD_STORAGE_BUCKET = os.environ.get('CLOUD_STORAGE_BUCKET')
    API_KEY = os.environ.get('API_KEY')
    GOOGLE_APPLICATION_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
