from typing import Dict, Any
from t08_flask_mysql.app.my_project import db

class Check(db.Model):
    __tablename__ = "check"

    idcheck = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_time = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.DECIMAL(10, 0), nullable=False)
    el_adress_idel_adress = db.Column(db.Integer, nullable=False)
    el_adress_client_idclient = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Check(idcheck={self.idcheck}, date_time={self.date_time}, amount={self.amount}, el_adress_idel_adress={self.el_adress_idel_adress}, el_adress_client_idclient={self.el_adress_client_idclient})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'idcheck': self.idcheck,
            'date_time': self.date_time,
            'amount': self.amount,
            'el_adress_idel_adress': self.el_adress_idel_adress,
            'el_adress_client_idclient': self.el_adress_client_idclient
        }

    @staticmethod
    def create_from_dto(check_dict: Dict[str, Any]):
        return Check(
            date_time=check_dict['date_time'],
            amount=check_dict['amount'],
            el_adress_idel_adress=check_dict['el_adress_idel_adress'],
            el_adress_client_idclient=check_dict['el_adress_client_idclient']
        )
