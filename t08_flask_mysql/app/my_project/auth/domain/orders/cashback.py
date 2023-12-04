from typing import Dict, Any
from t08_flask_mysql.app.my_project import db

class Cashback(db.Model):
    __tablename__ = "cashback"

    idcashback = db.Column(db.Integer, primary_key=True, autoincrement=True)
    percentage = db.Column(db.DECIMAL(10, 0), nullable=False)
    date_time = db.Column(db.DATETIME, nullable=True)
    treasury_idtreasury = db.Column(db.Integer, db.ForeignKey('treasury.idtreasury'), nullable=False)

    def __repr__(self) -> str:
        return f"Cashback(idcashback={self.idcashback}, percentage={self.percentage}, date_time={self.date_time}, treasury_idtreasury={self.treasury_idtreasury}, treasury_payments_idpayments={self.treasury_payments_idpayments})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'idcashback': self.idcashback,
            'percentage': self.percentage,
            'date_time': self.date_time,
            'treasury_idtreasury': self.treasury_idtreasury,
            'treasury_info':self.treasury.put_into_dto()
        }

    @staticmethod
    def create_from_dto(cashback_dict: Dict[str, Any]):
        return Cashback(
            percentage=cashback_dict['percentage'],
            date_time=cashback_dict['date_time'],
            treasury_idtreasury=cashback_dict['treasury_idtreasury'],
        )
