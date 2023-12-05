from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import cashback_controller
from t08_flask_mysql.app.my_project.auth.domain import Cashback

cashback_bp = Blueprint('cashback', __name__, url_prefix='/cashback')

@cashback_bp.get('')
def get_all_cashback() -> Response:
    cashback = cashback_controller.find_all()
    return make_response(jsonify(cashback), HTTPStatus.OK)

@cashback_bp.get('/treasury/<int:treasury_id>')
def get_cashback_by_treasury(treasury_id: int) -> Response:
    cashback = cashback_controller.find_by_treasury_id(treasury_id)
    return make_response(jsonify(cashback), HTTPStatus.OK)

@cashback_bp.post('')
def create_cashback() -> Response:
    content = request.get_json()
    cashback = Cashback.create_from_dto(content)
    cashback_controller.create(cashback)
    return make_response(jsonify(cashback.put_into_dto()), HTTPStatus.CREATED)

@cashback_bp.get('/<int:cashback_id>')
def get_cashback(cashback_id: int) -> Response:
    cashback = cashback_controller.find_by_id(cashback_id)
    if cashback:
        return make_response(jsonify(cashback), HTTPStatus.OK)
    return make_response(jsonify({"error": "Cashback not found"}), HTTPStatus.NOT_FOUND)

@cashback_bp.put('/<int:cashback_id>')
def update_cashback(cashback_id: int) -> Response:
    content = request.get_json()
    cashback = Cashback.create_from_dto(content)
    cashback_controller.update(cashback_id, cashback)
    return make_response("Cashback updated", HTTPStatus.OK)

@cashback_bp.patch('/<int:cashback_id>')
def patch_cashback(cashback_id: int) -> Response:
    content = request.get_json()
    cashback_controller.patch(cashback_id, content)
    return make_response("Cashback updated", HTTPStatus.OK)

@cashback_bp.delete('/<int:cashback_id>')
def delete_cashback(cashback_id: int) -> Response:
    cashback_controller.delete(cashback_id)
    return make_response("Cashback deleted", HTTPStatus.OK)
