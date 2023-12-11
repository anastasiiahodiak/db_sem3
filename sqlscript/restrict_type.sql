use bank;

DELIMITER //

CREATE TRIGGER trg_restrict_type
BEFORE INSERT
ON type_payment
FOR EACH ROW
BEGIN
    IF NEW.type NOT IN ('water', 'wifi', 'apartaments', 'music', 'photoshop') THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid type in type';
    END IF;
END //

DELIMITER ;