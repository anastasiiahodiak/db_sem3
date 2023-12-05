from t08_flask_mysql.app.my_project.auth.service import el_adress_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class ElAdressController(GeneralController):
    """
    Realization of El Adress controller.
    """
    _service = el_adress_service
