from flask import request
from flask_restx import Api, Namespace, Resource, fields

from app.models.user import User

api = Api(
    title="Tarea1 Flask API",
    version="1.0",
    description="API de gestión de usuarios",
    doc=False,
)

ns = Namespace("users", description="Operaciones con usuarios")
api.add_namespace(ns, path="/api/users")

user_model = ns.model("User", {
    "id": fields.Integer(readonly=True),
    "dni": fields.String(required=True),
    "given_name": fields.String(required=True),
    "family_name": fields.String(required=True),
    "email": fields.String(required=True),
    "phone_number": fields.String(required=True),
    "address": fields.String(required=True),
    "created_at": fields.DateTime(readonly=True),
    "updated_at": fields.DateTime(readonly=True),
})


@ns.route("/")
class UserList(Resource):
    @ns.doc("list_users")
    @ns.marshal_list_with(user_model)
    def get(self):
        """ Retorna todos los usuarios """
        return User.query.all()


@ns.route("/<int:id>")
class UserItem(Resource):
    @ns.doc("get_user")
    @ns.marshal_with(user_model)
    @ns.response(404, "Usuario no encontrado")
    def get(self, id):
        """ Retorna un usuario por ID """
        return User.query.get_or_404(id)


@ns.route("/search")
class UserSearch(Resource):
    @ns.doc("search_users")
    @ns.marshal_list_with(user_model)
    @ns.param("given_name", "Nombre a buscar")
    def get(self):
        """ Busca usuarios por nombre """
        given_name = request.args.get("given_name", "")
        return User.query.filter(User.given_name.ilike(f"%{given_name}%")).all()
