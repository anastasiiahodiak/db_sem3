from t08_flask_mysql.app.my_project.auth.service import treasury_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class TreasuryController(GeneralController):
    """
    Realization of Treasury controller.
    """
    _service = treasury_service
