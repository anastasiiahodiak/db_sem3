from t08_flask_mysql.app.my_project.auth.service import check_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class CheckController(GeneralController):
    """
    Realization of Check controller.
    """
    _service = check_service
