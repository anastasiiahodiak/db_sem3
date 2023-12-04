from typing import Dict, Any
from t08_flask_mysql.app.my_project import db

class Treasury(db.Model):
    __tablename__ = "treasury"

    idtreasury = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount_money = db.Column(db.DECIMAL(10, 0), nullable=False)
    annual_percentage = db.Column(db.DECIMAL(10, 0), nullable=False)
    account_idaccount = db.Column(db.Integer, db.ForeignKey('account.idaccount'), nullable=False)
    payments_idpayments = db.Column(db.Integer, db.ForeignKey('payments.idpayments'), nullable=False)

    cashbacks= db.relationship('Cashback', backref="treasury")
    def __repr__(self) -> str:
        return f"Treasury(idtreasury={self.idtreasury}, amount_money={self.amount_money}, annual_percentage={self.annual_percentage}, account_idaccount={self.account_idaccount}, payments_idpayments={self.payments_idpayments})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'idtreasury': self.idtreasury,
            'amount_money': self.amount_money,
            'annual_percentage': self.annual_percentage,
            'account_idaccount': self.account_idaccount,
            'account_info': self.account.put_into_dto(),
            'payments_idpayments': self.payments_idpayments,
            'payments_info': self.payments.put_into_dto()
        }

    @staticmethod
    def create_from_dto(treasury_dict: Dict[str, Any]):
        return Treasury(
            amount_money=treasury_dict['amount_money'],
            annual_percentage=treasury_dict['annual_percentage'],
            account_idaccount=treasury_dict['account_idaccount'],
            payments_idpayments=treasury_dict['payments_idpayments']
        )
