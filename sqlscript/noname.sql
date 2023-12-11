use bank;

DELIMITER //

CREATE PROCEDURE InsertNonameRecords(IN treasury_id1 int)
BEGIN
    DECLARE counter INT DEFAULT 1;

    WHILE counter <= 10
        DO
            INSERT INTO random (treasury_id, title) VALUES (treasury_id1, CONCAT('Noname', counter));
            SET counter = counter + 1;
        END WHILE;
END //

DELIMITER ;
call InsertNonameRecords(5);