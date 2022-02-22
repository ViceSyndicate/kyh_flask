from app import app
from dotenv import load_dotenv


def setup():
    from app.blueprints.admin import bp_admin
    app.register_blueprint(bp_admin, url_prefix='/admin')
    return app


load_dotenv()
setup()


if __name__ == '__main__':
    app.run()
