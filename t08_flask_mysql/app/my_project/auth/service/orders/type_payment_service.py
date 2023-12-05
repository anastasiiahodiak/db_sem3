from t08_flask_mysql.app.my_project.auth.dao import type_payment_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class TypePaymentService(GeneralService):
    """
    Service class for handling Type Payments.
    """
    _dao = type_payment_dao
