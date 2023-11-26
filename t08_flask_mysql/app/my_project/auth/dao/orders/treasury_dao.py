from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Treasury
from typing import List

class TreasuryDAO(GeneralDAO):
    """
    Realization of Treasury data access layer.
    """
    _domain_type = Treasury
    # Add any specific methods related to treasury data access if needed
