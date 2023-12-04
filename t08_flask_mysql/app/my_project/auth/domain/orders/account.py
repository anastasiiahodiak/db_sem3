from typing import Dict, Any
from t08_flask_mysql.app.my_project import db


class Account(db.Model):
    __tablename__ = "account"

    idaccount = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_number = db.Column(db.String(45), nullable=False)
    balance = db.Column(db.DECIMAL(10, 0), nullable=False)
    client_idclient = db.Column(db.Integer, db.ForeignKey('client.idclient'), nullable=False)

    bank_details = db.relationship("BankDetails", backref="account")
    treasuries = db.relationship('Treasury', backref="account")
    transactions = db.relationship('Transaction', backref="account")

    def __repr__(self) -> str:
        return f"Account(idaccount={self.idaccount}, account_number='{self.account_number}', balance={self.balance}, client_idclient={self.client_idclient})"

    def put_into_dto(self) -> Dict[str, Any]:
        dto = {
            'idaccount': self.idaccount,
            'account_number': self.account_number,
            'balance': self.balance,
            'client_idclient': self.client_idclient,
            'client_info': self.client.put_into_dto(),
            'transactions': [transaction.put_into_dto() for transaction in self.transactions]

        }



        return dto

    @staticmethod
    def create_from_dto(account_dict: Dict[str, Any]):
        return Account(
            **account_dict
        )
