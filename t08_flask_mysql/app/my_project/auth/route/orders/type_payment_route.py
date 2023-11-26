from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import type_payment_controller
from t08_flask_mysql.app.my_project.auth.domain import TypePayment
type_payment_bp = Blueprint('type_payment', __name__, url_prefix='/type-payments')

@type_payment_bp.get('')
def get_all_type_payments() -> Response:
    type_payments = type_payment_controller.find_all()
    return make_response(jsonify(type_payments), HTTPStatus.OK)

@type_payment_bp.post('')
def create_type_payment() -> Response:
    content = request.get_json()
    type_payment = TypePayment.create_from_dto(content)
    type_payment_controller.create(type_payment)
    return make_response(jsonify(type_payment.put_into_dto()), HTTPStatus.CREATED)

@type_payment_bp.get('/<int:type_payment_id>')
def get_type_payment(type_payment_id: int) -> Response:
    type_payment = type_payment_controller.find_by_id(type_payment_id)
    if type_payment:
        return make_response(jsonify(type_payment), HTTPStatus.OK)
    return make_response(jsonify({"error": "Type Payment not found"}), HTTPStatus.NOT_FOUND)

@type_payment_bp.put('/<int:type_payment_id>')
def update_type_payment(type_payment_id: int) -> Response:
    content = request.get_json()
    type_payment = TypePayment.create_from_dto(content)
    type_payment_controller.update(type_payment_id, type_payment)
    return make_response("Type Payment updated", HTTPStatus.OK)

@type_payment_bp.patch('/<int:type_payment_id>')
def patch_type_payment(type_payment_id: int) -> Response:
    content = request.get_json()
    type_payment_controller.patch(type_payment_id, content)
    return make_response("Type Payment updated", HTTPStatus.OK)

@type_payment_bp.delete('/<int:type_payment_id>')
def delete_type_payment(type_payment_id: int) -> Response:
    type_payment_controller.delete(type_payment_id)
    return make_response("Type Payment deleted", HTTPStatus.OK)
