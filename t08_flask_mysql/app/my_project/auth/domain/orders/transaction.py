# t08_flask_mysql/app/my_project/models/transaction.py
from typing import Dict, Any
from t08_flask_mysql.app.my_project import db

class Transaction(db.Model):
    __tablename__ = "transactions"

    idtransactions = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.DECIMAL(10, 0), nullable=False)
    timestamp = db.Column(db.DATETIME, nullable=False)
    status = db.Column(db.String(45), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    account_idaccount = db.Column(db.Integer, db.ForeignKey('account.idaccount'), nullable=False)
    check_idcheck = db.Column(db.Integer, db.ForeignKey('check.idcheck'), nullable=False)
    payments_idpayments = db.Column(db.Integer, nullable=False)
    payments_type_payment_idtype_payment = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return (f"Transaction(idtransactions={self.idtransactions}, amount={self.amount}, "
                f"timestamp='{self.timestamp}', status='{self.status}', number={self.number}, "
                f"account_idaccount={self.account_idaccount}, check_idcheck={self.check_idcheck}, "
                f"payments_idpayments={self.payments_idpayments}, "
                f"payments_type_payment_idtype_payment={self.payments_type_payment_idtype_payment})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'idtransactions': self.idtransactions,
            'amount': self.amount,
            'timestamp': str(self.timestamp),
            'status': self.status,
            'number': self.number,
            'account_idaccount': self.account_idaccount,
            'check_idcheck': self.check_idcheck,
            'payments_idpayments': self.payments_idpayments,
            'payments_type_payment_idtype_payment': self.payments_type_payment_idtype_payment
        }

    @staticmethod
    def create_from_dto(transaction_dict: Dict[str, Any]):
        return Transaction(
            amount=transaction_dict['amount'],
            timestamp=transaction_dict['timestamp'],
            status=transaction_dict['status'],
            number=transaction_dict['number'],
            account_idaccount=transaction_dict['account_idaccount'],
            check_idcheck=transaction_dict['check_idcheck'],
            payments_idpayments=transaction_dict['payments_idpayments'],
            payments_type_payment_idtype_payment=transaction_dict['payments_type_payment_idtype_payment']
        )
