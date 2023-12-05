from t08_flask_mysql.app.my_project.auth.dao import account_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class AccountService(GeneralService):
    """
    Realization of Account service.
    """
    _dao = account_dao
