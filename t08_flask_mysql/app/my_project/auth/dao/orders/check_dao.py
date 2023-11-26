from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Check
from typing import List

class CheckDAO(GeneralDAO):
    """
    Realization of Check data access layer.
    """
    _domain_type = Check
    # Add any specific methods related to check data access if needed

