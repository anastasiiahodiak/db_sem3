use bank;

DELIMITER //

CREATE TRIGGER trg_prevent_delete
BEFORE DELETE
ON bank_details
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Deleting rows from this table is not allowed';
END //

DELIMITER ;