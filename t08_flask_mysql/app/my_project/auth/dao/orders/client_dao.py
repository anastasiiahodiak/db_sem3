from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Client
from typing import List

class ClientDAO(GeneralDAO):
    """
    Realization of Client data access layer.
    """
    _domain_type = Client
    # Add any specific methods related to client data access if needed
