from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import payments_controller
from t08_flask_mysql.app.my_project.auth.domain import Payments

payments_bp = Blueprint('payments', __name__, url_prefix='/payments')

@payments_bp.get('')
def get_all_payments() -> Response:
    payments = payments_controller.find_all()
    return make_response(jsonify(payments), HTTPStatus.OK)

@payments_bp.post('')
def create_payment() -> Response:
    content = request.get_json()
    payment = Payments.create_from_dto(content)
    payments_controller.create(payment)
    return make_response(jsonify(payment.put_into_dto()), HTTPStatus.CREATED)

@payments_bp.get('/<int:payment_id>')
def get_payment(payment_id: int) -> Response:
    payment = payments_controller.find_by_id(payment_id)
    if payment:
        return make_response(jsonify(payment), HTTPStatus.OK)
    return make_response(jsonify({"error": "Payment not found"}), HTTPStatus.NOT_FOUND)

@payments_bp.put('/<int:payment_id>')
def update_payment(payment_id: int) -> Response:
    content = request.get_json()
    payment = Payments.create_from_dto(content)
    payments_controller.update(payment_id, payment)
    return make_response("Payment updated", HTTPStatus.OK)

@payments_bp.patch('/<int:payment_id>')
def patch_payment(payment_id: int) -> Response:
    content = request.get_json()
    payments_controller.patch(payment_id, content)
    return make_response("Payment updated", HTTPStatus.OK)

@payments_bp.delete('/<int:payment_id>')
def delete_payment(payment_id: int) -> Response:
    payments_controller.delete(payment_id)
    return make_response("Payment deleted", HTTPStatus.OK)
