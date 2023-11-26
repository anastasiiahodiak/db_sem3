from t08_flask_mysql.app.my_project.auth.dao import check_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class CheckService(GeneralService):
    """
    Service class for handling Checks.
    """
    _dao = check_dao
