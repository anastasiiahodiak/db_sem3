
from .orders.account import Account
from .orders.bank_details import BankDetails
from .orders.cashback import Cashback
from .orders.check import Check
from .orders.client import Client
from .orders.el_adress import ElAdress
from .orders.payments import Payments
from .orders.transaction import Transaction
from .orders.treasury import Treasury
from .orders.type_payment import TypePayment

account = Account()
bank_details = BankDetails()
cashback = Cashback()
check = Check()
client = Client()
el_adress = ElAdress()
payments = Payments()
transaction = Transaction()
treasury = Treasury()
type_payment = TypePayment()
