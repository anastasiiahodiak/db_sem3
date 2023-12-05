from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Cashback
from typing import List

class CashbackDAO(GeneralDAO):
    """
    Realization of Cashback data access layer.
    """
    _domain_type = Cashback
    # Add any specific methods related to cashback data access if needed
