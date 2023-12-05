from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Account  # Assuming this is the domain class for accounts
from typing import List

class AccountDAO(GeneralDAO):
    """
    Realization of Account data access layer.
    """
    _domain_type = Account
    # Add any specific methods related to account data access if needed
