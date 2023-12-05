from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import BankDetails
from typing import List

class BankDetailsDAO(GeneralDAO):
    """
    Realization of BankDetails data access layer.
    """
    _domain_type = BankDetails
    # Add any specific methods related to bank details data access if needed
