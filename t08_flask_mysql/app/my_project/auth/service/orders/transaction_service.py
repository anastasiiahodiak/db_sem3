from t08_flask_mysql.app.my_project.auth.dao import transaction_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService
from typing import List, Dict
class TransactionService(GeneralService):
    """
    Service class for handling Transactions.
    """
    _dao = transaction_dao



    def find_transactions_by_accountid(self, user_id: int) -> List[object]:
        return self._dao.find_transactions_by_accountid(user_id)