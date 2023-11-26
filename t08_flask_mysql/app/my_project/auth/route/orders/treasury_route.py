from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import treasury_controller
from t08_flask_mysql.app.my_project.auth.domain import Treasury
treasury_bp = Blueprint('treasury', __name__, url_prefix='/treasuries')

@treasury_bp.get('')
def get_all_treasuries() -> Response:
    treasuries = treasury_controller.find_all()
    return make_response(jsonify(treasuries), HTTPStatus.OK)

@treasury_bp.post('')
def create_treasury() -> Response:
    content = request.get_json()
    treasury = Treasury.create_from_dto(content)
    treasury_controller.create(treasury)
    return make_response(jsonify(treasury.put_into_dto()), HTTPStatus.CREATED)

@treasury_bp.get('/<int:treasury_id>')
def get_treasury(treasury_id: int) -> Response:
    treasury = treasury_controller.find_by_id(treasury_id)
    if treasury:
        return make_response(jsonify(treasury), HTTPStatus.OK)
    return make_response(jsonify({"error": "Treasury not found"}), HTTPStatus.NOT_FOUND)

@treasury_bp.put('/<int:treasury_id>')
def update_treasury(treasury_id: int) -> Response:
    content = request.get_json()
    treasury = Treasury.create_from_dto(content)
    treasury_controller.update(treasury_id, treasury)
    return make_response("Treasury updated", HTTPStatus.OK)

@treasury_bp.patch('/<int:treasury_id>')
def patch_treasury(treasury_id: int) -> Response:
    content = request.get_json()
    treasury_controller.patch(treasury_id, content)
    return make_response("Treasury updated", HTTPStatus.OK)

@treasury_bp.delete('/<int:treasury_id>')
def delete_treasury(treasury_id: int) -> Response:
    treasury_controller.delete(treasury_id)
    return make_response("Treasury deleted", HTTPStatus.OK)
