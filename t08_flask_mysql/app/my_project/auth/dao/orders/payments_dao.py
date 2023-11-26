from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Payments
from typing import List

class PaymentsDAO(GeneralDAO):
    """
    Realization of Payment data access layer.
    """
    _domain_type = Payments
    # Add any specific methods related to payment data access if needed
