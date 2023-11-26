from flask import Flask

def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    from .orders.account_route import account_bp
    from .orders.bank_details_route import bank_details_bp
    from .orders.cashback_route import cashback_bp
    from .orders.check_route import check_bp
    from .orders.client_route import client_bp
    from .orders.el_adress_route import el_adress_bp
    from .orders.payments_route import payments_bp
    from .orders.transaction_route import transaction_bp
    from .orders.treasury_route import treasury_bp
    from .orders.type_payment_route import type_payment_bp

    app.register_blueprint(account_bp)
    app.register_blueprint(bank_details_bp)
    app.register_blueprint(cashback_bp)
    app.register_blueprint(check_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(el_adress_bp)
    app.register_blueprint(payments_bp)
    app.register_blueprint(transaction_bp)
    app.register_blueprint(treasury_bp)
    app.register_blueprint(type_payment_bp)

    # Register error handler blueprint
