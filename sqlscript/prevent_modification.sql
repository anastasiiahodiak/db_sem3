use bank;

DELIMITER //

CREATE TRIGGER trg_prevent_modification
BEFORE UPDATE
ON transactions
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Modifying data in this table is not allowed';
END //

DELIMITER ;
