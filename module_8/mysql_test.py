CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'admin';
GRANT ALL PRIVILEGES ON pysports.* TO 'pysports_user'@'localhost';
DROP USER IF EXISTS 'pysports_user'@'localhost';

--I've already created the tables for player and team. I linked the tables through a third table which has the primary keys as foreign keys within it.

INSERT INTO team(team_name, mascot)
    VALUES ('Wolverines', 'Wolverine', 'Chiefs', 'Wolf', 'Vikings', 'Victor');

INSERT INTO player(player_id, first_name, last_name)
    VALUES (1, 'Walter', 'Payton', 2, 'Barry', 'Sanders', 3, 'Reggie', 'White');