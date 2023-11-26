from t08_flask_mysql.app.my_project.auth.service import type_payment_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class TypePaymentsController(GeneralController):
    """
    Realization of Type Payments controller.
    """
    _service = type_payment_service
