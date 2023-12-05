from t08_flask_mysql.app.my_project.auth.service import bank_details_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class BankDetailsController(GeneralController):
    """
    Realization of Bank Details controller.
    """
    _service = bank_details_service
