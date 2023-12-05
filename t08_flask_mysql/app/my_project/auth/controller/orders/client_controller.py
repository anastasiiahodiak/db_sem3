from t08_flask_mysql.app.my_project.auth.service import client_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class ClientController(GeneralController):
    """
    Realization of Client controller.
    """
    _service = client_service
