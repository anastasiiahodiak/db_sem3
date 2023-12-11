use bank;

DELIMITER //

CREATE PROCEDURE insert_random(IN p_title VARCHAR(255), IN p_treasury_id INT)
BEGIN
    INSERT INTO Random (title, treasury_id) VALUES (p_title, p_treasury_id);
END //

DELIMITER ;