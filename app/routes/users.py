from flask import Blueprint, flash, redirect, render_template, request, url_for

from app.database import db
from app.models.user import User

users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["GET"])
def index():
    users = User.query.all()
    return render_template("users/index.html", users=users)


@users_bp.route("/users/new", methods=["GET"])
def new():
    return render_template("users/new.html")


@users_bp.route("/users", methods=["POST"])
def create():
    user = User(
        dni=request.form["dni"],
        given_name=request.form["given_name"],
        family_name=request.form["family_name"],
        email=request.form["email"],
        phone_number=request.form["phone_number"],
        address=request.form["address"],
    )
    db.session.add(user)
    db.session.commit()
    flash("Usuario creado correctamente.")
    return redirect(url_for("users.index"))


@users_bp.route("/users/<int:id>", methods=["GET"])
def show(id):
    user = User.query.get_or_404(id)
    return render_template("users/show.html", user=user)


@users_bp.route("/users/<int:id>/edit", methods=["GET"])
def edit(id):
    user = User.query.get_or_404(id)
    return render_template("users/edit.html", user=user)


@users_bp.route("/users/<int:id>", methods=["POST"])
def update(id):
    user = User.query.get_or_404(id)
    user.dni = request.form["dni"]
    user.given_name = request.form["given_name"]
    user.family_name = request.form["family_name"]
    user.email = request.form["email"]
    user.phone_number = request.form["phone_number"]
    user.address = request.form["address"]
    db.session.commit()
    flash("Usuario actualizado correctamente.")
    return redirect(url_for("users.show", id=user.id))


@users_bp.route("/users/<int:id>/delete", methods=["POST"])
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash("Usuario eliminado correctamente.")
    return redirect(url_for("users.index"))
