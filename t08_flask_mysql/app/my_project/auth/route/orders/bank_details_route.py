from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import bank_details_controller
from t08_flask_mysql.app.my_project.auth.domain import BankDetails

bank_details_bp = Blueprint('bank_details', __name__, url_prefix='/bank-details')

@bank_details_bp.get('')
def get_all_bank_details() -> Response:
    bank_details = bank_details_controller.find_all()
    return make_response(jsonify(bank_details), HTTPStatus.OK)

@bank_details_bp.get('/account/<int:account_id>')
def get_bank_details_by_account(account_id: int) -> Response:
    bank_details = bank_details_controller.find_by_account_id(account_id)
    return make_response(jsonify(bank_details), HTTPStatus.OK)

@bank_details_bp.post('')
def create_bank_details() -> Response:
    content = request.get_json()
    bank_details = BankDetails.create_from_dto(content)
    bank_details_controller.create(bank_details)
    return make_response(jsonify(bank_details.put_into_dto()), HTTPStatus.CREATED)

@bank_details_bp.get('/<int:bank_details_id>')
def get_bank_details(bank_details_id: int) -> Response:
    bank_details = bank_details_controller.find_by_id(bank_details_id)
    if bank_details:
        return make_response(jsonify(bank_details), HTTPStatus.OK)
    return make_response(jsonify({"error": "Bank details not found"}), HTTPStatus.NOT_FOUND)

@bank_details_bp.put('/<int:bank_details_id>')
def update_bank_details(bank_details_id: int) -> Response:
    content = request.get_json()
    bank_details = BankDetails.create_from_dto(content)
    bank_details_controller.update(bank_details_id, bank_details)
    return make_response("Bank details updated", HTTPStatus.OK)

@bank_details_bp.patch('/<int:bank_details_id>')
def patch_bank_details(bank_details_id: int) -> Response:
    content = request.get_json()
    bank_details_controller.patch(bank_details_id, content)
    return make_response("Bank details updated", HTTPStatus.OK)

@bank_details_bp.delete('/<int:bank_details_id>')
def delete_bank_details(bank_details_id: int) -> Response:
    bank_details_controller.delete(bank_details_id)
    return make_response("Bank details deleted", HTTPStatus.OK)
