from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import check_controller
from t08_flask_mysql.app.my_project.auth.domain import Check

check_bp = Blueprint('check', __name__, url_prefix='/check')

@check_bp.get('')
def get_all_checks() -> Response:
    checks = check_controller.find_all()
    return make_response(jsonify(checks), HTTPStatus.OK)

@check_bp.get('/el_address/<int:el_address_id>/<int:client_id>')
def get_check_by_el_address(el_address_id: int, client_id: int) -> Response:
    check = check_controller.find_by_el_address(el_address_id, client_id)
    return make_response(jsonify(check), HTTPStatus.OK)

@check_bp.post('')
def create_check() -> Response:
    content = request.get_json()
    check = Check.create_from_dto(content)
    check_controller.create(check)
    return make_response(jsonify(check.put_into_dto()), HTTPStatus.CREATED)

@check_bp.get('/<int:check_id>')
def get_check(check_id: int) -> Response:
    check = check_controller.find_by_id(check_id)
    if check:
        return make_response(jsonify(check), HTTPStatus.OK)
    return make_response(jsonify({"error": "Check not found"}), HTTPStatus.NOT_FOUND)

@check_bp.put('/<int:check_id>')
def update_check(check_id: int) -> Response:
    content = request.get_json()
    check = Check.create_from_dto(content)
    check_controller.update(check_id, check)
    return make_response("Check updated", HTTPStatus.OK)

@check_bp.patch('/<int:check_id>')
def patch_check(check_id: int) -> Response:
    content = request.get_json()
    check_controller.patch(check_id, content)
    return make_response("Check updated", HTTPStatus.OK)

@check_bp.delete('/<int:check_id>')
def delete_check(check_id: int) -> Response:
    check_controller.delete(check_id)
    return make_response("Check deleted", HTTPStatus.OK)
