import json

from flask import Blueprint, Response

from app.routes.api import api

docs_bp = Blueprint("docs", __name__)

SWAGGER_UI_HTML = """<!DOCTYPE html>
<html>
<head>
    <title>Tarea1 Flask API</title>
    <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css">
</head>
<body>
    <div id="swagger-ui"></div>
    <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
    <script>
        SwaggerUIBundle({url: "/api/swagger.json", dom_id: "#swagger-ui"});
    </script>
</body>
</html>"""


@docs_bp.route("/docs")
def swagger_ui():
    return Response(SWAGGER_UI_HTML, content_type="text/html")


@docs_bp.route("/api/swagger.json")
def swagger_json():
    return Response(json.dumps(api.__schema__), content_type="application/json")
