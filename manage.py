from project import create_app

flask_app = create_app()

def create_tinyurl_app():
    return flask_app
