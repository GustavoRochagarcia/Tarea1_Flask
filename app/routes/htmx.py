from flask import Blueprint, render_template, request

from app.models.user import User

htmx_bp = Blueprint("htmx", __name__)


@htmx_bp.route("/htmx")
def index():
    return render_template("htmx/index.html")


@htmx_bp.route("/htmx/users")
def users_list():
    users = User.query.all()
    return render_template("htmx/partials/users_table.html", users=users)


@htmx_bp.route("/htmx/users/search")
def users_search():
    given_name = request.args.get("given_name", "")
    users = User.query.filter(User.given_name.ilike(f"%{given_name}%")).all()
    return render_template("htmx/partials/users_table.html", users=users)
