from t08_flask_mysql.app.my_project.auth.service import transaction_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from typing import List, Dict
class TransactionController(GeneralController):
    """
    Realization of Transaction controller.
    """
    _service = transaction_service
    def find_transactions_by_accountid(self, account_id: int) -> List[Dict[str, object]]:
        """
        Finds libraries associated with a specific user by user_id.
        :param user_id: ID of the user
        :return: List of libraries associated with the user
        """
        return list(map(lambda x: x.put_into_dto(), self._service.find_transactions_by_accountid(account_id)))
