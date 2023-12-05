from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import ElAdress
from typing import List

class ElAdressDAO(GeneralDAO):
    """
    Realization of ElAdress data access layer.
    """
    _domain_type = ElAdress
    # Add any specific methods related to ElAdress data access if needed
