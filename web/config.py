import os

class Config(object):
    SECRET_KEY         = os.environ.get("SECRET_KEY")
    
    MONGO_USERNAME     = os.environ.get("MONGO_USERNAME")
    MONGO_PASSWORD     = os.environ.get("MONGO_PASSWORD")
    MONGO_DATABASE     = os.environ.get("MONGO_DATABASE")
    MONGO_COLLECTION   = os.environ.get("MONGO_COLLECTION")
    MONGO_URI          = os.environ.get("MONGO_URI")
