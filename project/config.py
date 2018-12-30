import os


class BaseConfig:

    # BASE_URL = "http://www.uRshort.us/"
    basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # MongoDB setup
    MONGODB_HOST = "localhost"
    MONGODB_PORT = 27017

    SERVER_NAME = "0.0.0.0:80"


