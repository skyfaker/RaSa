from flask_restful import Resource

from ..buleprint_factory import web_bp


class PingApi(Resource):
    def get(self):
        """
        For connection health check
        """
        return {"result": "pong"}


web_bp.add_resource(PingApi, "/ping")
