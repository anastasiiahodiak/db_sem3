from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import transaction_controller
from t08_flask_mysql.app.my_project.auth.domain import Transaction
transaction_bp = Blueprint('transaction', __name__, url_prefix='/transactions')

@transaction_bp.get('')
def get_all_transactions() -> Response:
    transactions = transaction_controller.find_all()
    return make_response(jsonify(transactions), HTTPStatus.OK)

@transaction_bp.post('')
def create_transaction() -> Response:
    content = request.get_json()
    transaction = Transaction.create_from_dto(content)
    transaction_controller.create(transaction)
    return make_response(jsonify(transaction.put_into_dto()), HTTPStatus.CREATED)

@transaction_bp.get('/<int:transaction_id>')
def get_transaction(transaction_id: int) -> Response:
    transaction = transaction_controller.find_by_id(transaction_id)
    if transaction:
        return make_response(jsonify(transaction), HTTPStatus.OK)
    return make_response(jsonify({"error": "Transaction not found"}), HTTPStatus.NOT_FOUND)

@transaction_bp.put('/<int:transaction_id>')
def update_transaction(transaction_id: int) -> Response:
    content = request.get_json()
    transaction = Transaction.create_from_dto(content)
    transaction_controller.update(transaction_id, transaction)
    return make_response("Transaction updated", HTTPStatus.OK)

@transaction_bp.patch('/<int:transaction_id>')
def patch_transaction(transaction_id: int) -> Response:
    content = request.get_json()
    transaction_controller.patch(transaction_id, content)
    return make_response("Transaction updated", HTTPStatus.OK)

@transaction_bp.delete('/<int:transaction_id>')
def delete_transaction(transaction_id: int) -> Response:
    transaction_controller.delete(transaction_id)
    return make_response("Transaction deleted", HTTPStatus.OK)

@transaction_bp.get('/account/<int:user_id>')
def get_transactions_by_accountid(user_id: int) -> Response:
    """
    Gets libraries associated with a specific user by user ID.
    :param user_id: ID of the user
    :return: Response object
    """
    transactions = transaction_controller.find_transactions_by_accountid(user_id)
    return make_response(jsonify(transactions), HTTPStatus.OK)