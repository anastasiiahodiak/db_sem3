from t08_flask_mysql.app.my_project.auth.dao import bank_details_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class BankDetailsService(GeneralService):
    """
    Service class for handling Bank Details.
    """
    _dao = bank_details_dao
