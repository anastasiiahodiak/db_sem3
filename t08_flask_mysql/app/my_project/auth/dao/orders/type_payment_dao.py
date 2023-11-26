from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import TypePayment
from typing import List

class TypePaymentDAO(GeneralDAO):
    """
    Realization of TypePayment data access layer.
    """
    _domain_type = TypePayment
    # Add any specific methods related to type payment data access if needed
