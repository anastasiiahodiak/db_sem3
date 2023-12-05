from typing import Dict, Any
from t08_flask_mysql.app.my_project import db

class TypePayment(db.Model):
    __tablename__ = "type_payment"

    idtype_payment = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(45), nullable=False)

    payments = db.relationship('Payments', backref="type_payment")
    def __repr__(self) -> str:
        return f"TypePayment(idtype_payment={self.idtype_payment}, type='{self.type}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'idtype_payment': self.idtype_payment,
            'type': self.type,
            'all_payments_of_this_type': [{
                            'idpayment': payment.idpayments,
                            'amount': payment.amount,
                            'debt': payment.debt
                        } for payment in self.payments]
        }

    @staticmethod
    def create_from_dto(type_payment_dict: Dict[str, Any]):
        return TypePayment(
            type=type_payment_dict['type']
        )
