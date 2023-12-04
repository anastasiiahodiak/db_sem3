
INSERT INTO bank.type_payment (type) VALUES
('water'),
('wifi'),
('apartaments'),
('wifi'),
('wifi'),
('music'),
('photoshop'),
('water'),
('wifi'),
('music');

INSERT INTO bank.payments (type_payment_idtype_payment, amount, debt) VALUES
(1, 500, 0),
(2, 800, 0),
(3, 1200, 0),
(4, 300, 0),
(5, 1500, 0),
(1, 200, 0),
(2, 900, 0),
(3, 600, 0),
(4, 1100, 0),
( 5, 700, 0);


INSERT INTO bank.client (name, surname) VALUES
('John', 'Doe'),
('Jane', 'Smith'),
('Mike', 'Johnson'),
('Emily', 'Williams'),
('David', 'Brown'),
('Emma', 'Miller'),
('Christopher', 'Taylor'),
('Sophia', 'Anderson'),
('William', 'Martinez'),
('Olivia', 'Moore');

INSERT INTO bank.account (account_number, balance, client_idclient) VALUES
('123456789', 5000, 1),
('987654321', 8000, 2),
('111223344', 12000, 3),
('555666777', 3000, 4),
('999000111', 15000, 5),
('777888999', 2000, 6),
('444333222', 9000, 7),
('888777666', 6000, 8),
('222111444', 11000, 9),
('666555888', 7000, 10);


INSERT INTO bank.bank_details (bank_name, bank_code, account_idaccount) VALUES
('Bank A', 'A123', 1),
('Bank B', 'B456', 2),
('Bank C', 'C789', 3),
('Bank D', 'D012', 4),
('Bank E', 'E345', 5),
('Bank F', 'F678', 6),
('Bank G', 'G901', 7),
('Bank H', 'H234', 8),
('Bank I', 'I567', 9),
('Bank J', 'J890', 10);

INSERT INTO bank.treasury (amount_money, annual_percentage, account_idaccount, payments_idpayments) VALUES
(50000, 5, 1, 1),
(80000, 6, 2, 2),
(120000, 4, 3, 3),
(30000, 3, 4, 4),
(150000, 7, 5, 5),
(20000, 8, 6, 6),
(90000, 4, 7, 7),
(60000, 5, 8, 8),
(110000, 6, 9, 9),
(70000, 7, 10, 10);

INSERT INTO bank.el_adress (name, client_idclient) VALUES
('Home', 1),
('Work', 2),
('Office', 3),
('Apartment', 4),
('Studio', 5),
('Cottage', 6),
('Warehouse', 7),
('Villa', 8),
('Loft', 9),
('Mansion', 10);

INSERT INTO bank.check (date_time, amount, el_adress_idel_adress) VALUES
('2023-10-24 14:00:00', 100, 1),
('2023-10-25 15:30:00', 150, 2),
('2023-10-26 11:45:00', 200, 3),
('2023-10-27 16:10:00', 80, 4),
('2023-10-28 09:45:00', 120, 5),
('2023-10-29 10:55:00', 90, 6),
('2023-10-30 13:15:00', 180, 7),
('2023-10-31 14:40:00', 110, 8),
('2023-11-01 16:50:00', 130, 9),
('2023-11-02 18:00:00', 160, 10);


INSERT INTO bank.transactions (amount, timestamp, status, number, account_idaccount, check_idcheck, payments_idpayments) VALUES
(100, '2023-10-24 14:30:00', 'Success', 123, 1, 1, 1),
(150, '2023-10-25 15:45:00', 'Success', 124, 2, 2, 2),
(200, '2023-10-26 12:00:00', 'Pending', 125, 3, 3, 3),
(80, '2023-10-27 16:15:00', 'Success', 126, 4, 4, 4),
(120, '2023-10-28 10:00:00', 'Pending', 127, 5, 5, 5),
(90, '2023-10-29 11:15:00', 'Success', 128, 6, 6, 6),
(180, '2023-10-30 13:30:00', 'Pending', 129, 7, 7, 7),
(110, '2023-10-31 14:45:00', 'Success', 130, 8, 8, 8),
(130, '2023-11-01 17:00:00', 'Success', 131, 9, 9, 9),
(160, '2023-11-02 18:15:00', 'Pending', 132, 10, 10, 10);



INSERT INTO bank.cashback (percentage, date_time, treasury_idtreasury) VALUES
(2, '2023-10-24 14:30:00', 1),
(3, '2023-10-25 15:45:00', 2),
(1, '2023-10-26 12:15:00', 3),
(2, '2023-10-27 16:20:00', 4),
(4, '2023-10-28 10:10:00', 5),
(1, '2023-10-29 11:30:00', 6),
(3, '2023-10-30 13:40:00', 7),
(2, '2023-10-31 14:50:00', 8),
(4, '2023-11-01 17:00:00', 9),
(3, '2023-11-02 18:10:00', 10);