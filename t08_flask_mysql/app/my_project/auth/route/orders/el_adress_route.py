from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import el_adress_controller
from t08_flask_mysql.app.my_project.auth.domain import ElAdress

el_adress_bp = Blueprint('el_adress', __name__, url_prefix='/el-adress')

@el_adress_bp.get('')
def get_all_el_adresses() -> Response:
    el_adresses = el_adress_controller.find_all()
    return make_response(jsonify(el_adresses), HTTPStatus.OK)

@el_adress_bp.post('')
def create_el_adress() -> Response:
    content = request.get_json()
    el_adress = ElAdress.create_from_dto(content)
    el_adress_controller.create(el_adress)
    return make_response(jsonify(el_adress.put_into_dto()), HTTPStatus.CREATED)

@el_adress_bp.get('/<int:el_adress_id>')
def get_el_adress(el_adress_id: int) -> Response:
    el_adress = el_adress_controller.find_by_id(el_adress_id)
    if el_adress:
        return make_response(jsonify(el_adress), HTTPStatus.OK)
    return make_response(jsonify({"error": "ElAdress not found"}), HTTPStatus.NOT_FOUND)

@el_adress_bp.put('/<int:el_adress_id>')
def update_el_adress(el_adress_id: int) -> Response:
    content = request.get_json()
    el_adress = ElAdress.create_from_dto(content)
    el_adress_controller.update(el_adress_id, el_adress)
    return make_response("ElAdress updated", HTTPStatus.OK)

@el_adress_bp.patch('/<int:el_adress_id>')
def patch_el_adress(el_adress_id: int) -> Response:
    content = request.get_json()
    el_adress_controller.patch(el_adress_id, content)
    return make_response("ElAdress updated", HTTPStatus.OK)

@el_adress_bp.delete('/<int:el_adress_id>')
def delete_el_adress(el_adress_id: int) -> Response:
    el_adress_controller.delete(el_adress_id)
    return make_response("ElAdress deleted", HTTPStatus.OK)
