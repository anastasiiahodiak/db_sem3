from .orders.account_service import AccountService
from .orders.bank_details_service import BankDetailsService
from .orders.cashback_service import CashbackService
from .orders.check_service import CheckService
from .orders.client_service import ClientService
from .orders.el_adress_service import ElAdressService
from .orders.payments_service import PaymentsService
from .orders.transaction_service import TransactionService
from .orders.treasury_service import TreasuryService
from .orders.type_payment_service import TypePaymentService

account_service = AccountService()
bank_details_service = BankDetailsService()
cashback_service = CashbackService()
check_service = CheckService()
client_service = ClientService()
el_adress_service = ElAdressService()
payments_service = PaymentsService()
transaction_service = TransactionService()
treasury_service = TreasuryService()
type_payment_service = TypePaymentService()
