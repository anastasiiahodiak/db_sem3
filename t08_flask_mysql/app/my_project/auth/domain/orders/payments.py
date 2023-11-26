from typing import Dict, Any
from t08_flask_mysql.app.my_project import db

class Payments(db.Model):
    __tablename__ = "payments"

    idpayments = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_payment_idtype_payment = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.DECIMAL, nullable=False)
    debt = db.Column(db.DECIMAL, nullable=False)

    def __repr__(self) -> str:
        return f"Payments(idpayments={self.idpayments}, type_payment_idtype_payment={self.type_payment_idtype_payment}, amount={self.amount}, debt={self.debt})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'idpayments': self.idpayments,
            'type_payment_idtype_payment': self.type_payment_idtype_payment,
            'amount': self.amount,
            'debt': self.debt
        }

    @staticmethod
    def create_from_dto(payments_dict: Dict[str, Any]):
        return Payments(
            type_payment_idtype_payment=payments_dict['type_payment_idtype_payment'],
            amount=payments_dict['amount'],
            debt=payments_dict['debt']
        )
