use bank;

DELIMITER //

CREATE PROCEDURE CreateTablesFromRandom()
BEGIN
    DECLARE isDone INT DEFAULT FALSE;
    DECLARE titleT VARCHAR(500);

    DECLARE cursorForRandom CURSOR FOR SELECT title FROM random;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET isDone = TRUE;

    OPEN cursorForRandom;

    readLoop: LOOP
        FETCH cursorForRandom INTO titleT;
        IF isDone THEN
            LEAVE readLoop;
        END IF;

        SET @createQuery = CONCAT('CREATE TABLES ', titleT);
        PREPARE createTables FROM @createQuery;
        EXECUTE createTables;
        DEALLOCATE PREPARE createTables;
    END LOOP;

    CLOSE cursorForRandom;
END //

DELIMITER ;

CALL CreateTablesFromRandom();
