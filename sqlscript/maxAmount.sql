use bank;

DELIMITER //

CREATE FUNCTION maxAmount()
    RETURNS DECIMAL(8, 2)
    DETERMINISTIC
    NO SQL
BEGIN
    DECLARE maxVal DECIMAL(8, 2);
    SELECT MAX(amount_money) INTO maxVal FROM treasury;
    RETURN maxVal;
END; //



CREATE PROCEDURE showMaxAmount()
BEGIN
    SELECT maxAmount();
END; 

DELIMITER ;
CALL showMaxAmount();