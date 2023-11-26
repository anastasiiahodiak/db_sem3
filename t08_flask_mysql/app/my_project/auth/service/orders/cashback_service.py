from t08_flask_mysql.app.my_project.auth.dao import cashback_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class CashbackService(GeneralService):
    """
    Service class for handling Cashback details.
    """
    _dao = cashback_dao
