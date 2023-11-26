from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import account_controller
from t08_flask_mysql.app.my_project.auth.domain import Account

account_bp = Blueprint('accounts', __name__, url_prefix='/accounts')

@account_bp.get('')
def get_all_accounts() -> Response:
    accounts = account_controller.find_all()
    return make_response(jsonify(accounts), HTTPStatus.OK)

@account_bp.get('/client/<int:client_id>')
def get_accounts_by_client(client_id: int) -> Response:
    accounts = account_controller.find_by_client_id(client_id)
    return make_response(jsonify(accounts), HTTPStatus.OK)

@account_bp.post('')
def create_account() -> Response:
    content = request.get_json()
    account = Account.create_from_dto(content)
    account_controller.create(account)
    return make_response(jsonify(account.put_into_dto()), HTTPStatus.CREATED)

@account_bp.get('/<int:account_id>')
def get_account(account_id: int) -> Response:
    account = account_controller.find_by_id(account_id)
    if account:
        return make_response(jsonify(account), HTTPStatus.OK)
    return make_response(jsonify({"error": "Account not found"}), HTTPStatus.NOT_FOUND)

@account_bp.put('/<int:account_id>')
def update_account(account_id: int) -> Response:
    content = request.get_json()
    account = Account.create_from_dto(content)
    account_controller.update(account_id, account)
    return make_response("Account updated", HTTPStatus.OK)

@account_bp.patch('/<int:account_id>')
def patch_account(account_id: int) -> Response:
    content = request.get_json()
    account_controller.patch(account_id, content)
    return make_response("Account updated", HTTPStatus.OK)

@account_bp.delete('/<int:account_id>')
def delete_account(account_id: int) -> Response:
    account_controller.delete(account_id)
    return make_response("Account deleted", HTTPStatus.OK)
