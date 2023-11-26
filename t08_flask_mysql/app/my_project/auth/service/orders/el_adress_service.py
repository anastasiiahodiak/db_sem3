from t08_flask_mysql.app.my_project.auth.dao import el_adress_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class ElAdressService(GeneralService):
    """
    Service class for handling El Addresses.
    """
    _dao = el_adress_dao
