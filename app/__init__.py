from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

from app.config import get_config
from app.database import db

load_dotenv()

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.api import api
    from app.routes.docs import docs_bp
    from app.routes.htmx import htmx_bp
    from app.routes.main import main_bp
    from app.routes.users import users_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(htmx_bp)
    app.register_blueprint(docs_bp)
    api.init_app(app)

    return app
