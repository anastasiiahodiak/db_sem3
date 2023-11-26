from typing import Dict, Any
from t08_flask_mysql.app.my_project import db

class ElAdress(db.Model):
    __tablename__ = "el_adress"

    idel_adress = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=True)
    client_idclient = db.Column(db.Integer, db.ForeignKey('client.idclient'), nullable=False)

    def __repr__(self) -> str:
        return f"ElAdress(idel_adress={self.idel_adress}, name={self.name}, client_idclient={self.client_idclient})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'idel_adress': self.idel_adress,
            'name': self.name,
            'client_idclient': self.client_idclient
        }

    @staticmethod
    def create_from_dto(el_adress_dict: Dict[str, Any]):
        return ElAdress(
            name=el_adress_dict['name'],
            client_idclient=el_adress_dict['client_idclient']
        )
