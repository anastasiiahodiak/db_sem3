from typing import Dict, Any
from t08_flask_mysql.app.my_project import db

class Client(db.Model):
    __tablename__ = "client"

    idclient = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)

    el_adresses = db.relationship("ElAdress", backref="client")
    accounts = db.relationship("Account", backref="client")
    def __repr__(self) -> str:
        return f"Client(idclient={self.idclient}, name='{self.name}', surname='{self.surname}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'idclient': self.idclient,
            'name': self.name,
            'surname': self.surname
        }

    @staticmethod
    def create_from_dto(client_dict: Dict[str, Any]):
        return Client(
            **client_dict
        )
