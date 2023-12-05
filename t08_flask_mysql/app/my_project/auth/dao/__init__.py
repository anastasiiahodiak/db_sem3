
from .orders.account_dao import AccountDAO
from .orders.bank_details_dao import BankDetailsDAO
from .orders.cashback_dao import CashbackDAO
from .orders.check_dao import CheckDAO
from .orders.client_dao import ClientDAO
from .orders.el_adress_dao import ElAdressDAO
from .orders.payments_dao import PaymentsDAO
from .orders.transaction_dao import TransactionDAO
from .orders.treasury_dao import TreasuryDAO
from .orders.type_payment_dao import TypePaymentDAO

# Instantiate DAOs
account_dao = AccountDAO()
bank_details_dao = BankDetailsDAO()
cashback_dao = CashbackDAO()
check_dao = CheckDAO()
client_dao = ClientDAO()
el_adress_dao = ElAdressDAO()
payments_dao = PaymentsDAO()
transaction_dao = TransactionDAO()
treasury_dao = TreasuryDAO()
type_payment_dao = TypePaymentDAO()
