from app import create_app
from app.database import db
from app.models import User  # noqa: F401 — ensure models are registere

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()
