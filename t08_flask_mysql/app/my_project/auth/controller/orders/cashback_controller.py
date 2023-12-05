from t08_flask_mysql.app.my_project.auth.service import cashback_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class CashbackController(GeneralController):
    """
    Realization of Cashback controller.
    """
    _service = cashback_service
