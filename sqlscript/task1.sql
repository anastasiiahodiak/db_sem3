use bank;

DELIMITER //

CREATE TABLE IF NOT EXISTS Random (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    treasury_id INT
);

CREATE TRIGGER trg_insert_random
BEFORE INSERT ON Random
FOR EACH ROW
BEGIN
    DECLARE parent_count INT;

    SELECT COUNT(*) INTO parent_count
    FROM Treasury
    WHERE id = NEW.treasury_id;

    IF parent_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid parent record in review';
    END IF;
END; //

CREATE TRIGGER trg_update_random
BEFORE UPDATE ON Random
FOR EACH ROW
BEGIN
    DECLARE parent_count INT;

    SELECT COUNT(*) INTO parent_count
    FROM Treasury
    WHERE id = NEW.treasury_id;

    IF parent_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid parent record in review';
    END IF;
END; //

CREATE TRIGGER trg_delete_random
BEFORE DELETE ON Treasury
FOR EACH ROW
BEGIN
    DELETE FROM Random
    WHERE treasury_id = OLD.id;
END; //
DELIMITER ;

INSERT INTO Random (title, treasury_id) values ('phone', 2);