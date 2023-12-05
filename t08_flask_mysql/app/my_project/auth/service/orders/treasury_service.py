from t08_flask_mysql.app.my_project.auth.dao import treasury_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class TreasuryService(GeneralService):
    """
    Service class for handling Treasury.
    """
    _dao = treasury_dao
