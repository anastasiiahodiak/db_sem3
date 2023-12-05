from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Transaction
from typing import List

class TransactionDAO(GeneralDAO):
    """
    Realization of Transaction data access layer.
    """
    _domain_type = Transaction
    # Add any specific methods related to transaction data access if needed
    def find_transactions_by_accountid(self, user_userid: int) -> List[object]:
        return self._session.query(Transaction).filter(Transaction.account_idaccount == user_userid).all()
