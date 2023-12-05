from typing import Dict, Any
from t08_flask_mysql.app.my_project import db

class BankDetails(db.Model):
    __tablename__ = "bank_details"

    idbank_details = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bank_name = db.Column(db.String(45), nullable=False)
    bank_code = db.Column(db.String(45), nullable=False)
    account_idaccount = db.Column(db.Integer, db.ForeignKey('account.idaccount'), nullable=False)

    def __repr__(self) -> str:
        return f"BankDetails(idbank_details={self.idbank_details}, bank_name='{self.bank_name}', bank_code='{self.bank_code}', account_idaccount={self.account_idaccount})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'idbank_details': self.idbank_details,
            'bank_name': self.bank_name,
            'bank_code': self.bank_code,
            'account_idaccount': self.account_idaccount,
            'account_info': self.account.put_into_dto(extra_info=False)
        }

    @staticmethod
    def create_from_dto(bank_details_dict: Dict[str, Any]):
        return BankDetails(
            bank_name=bank_details_dict['bank_name'],
            bank_code=bank_details_dict['bank_code'],
            account_idaccount=bank_details_dict['account_idaccount']
        )
