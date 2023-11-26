from .orders.account_controller import AccountController
from .orders.bank_details_controller import BankDetailsController
from .orders.cashback_controller import CashbackController
from .orders.check_controller import CheckController
from .orders.client_controller import ClientController
from .orders.el_adress_controller import ElAdressController
from .orders.payments_controller import PaymentsController
from .orders.transaction_controller import TransactionController
from .orders.treasury_controller import TreasuryController
from .orders.type_payment_controller import TypePaymentsController

# Instantiate controllers
account_controller = AccountController()
bank_details_controller = BankDetailsController()
cashback_controller = CashbackController()
check_controller = CheckController()
client_controller = ClientController()
el_adress_controller = ElAdressController()
payments_controller = PaymentsController()
transaction_controller = TransactionController()
treasury_controller = TreasuryController()
type_payment_controller = TypePaymentsController()
