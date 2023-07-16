SELECT * FROM player;
INSERT INTO player (player_id,first_name, last_name, team_id)
    VALUES(12,'Gandalf','Gray', 1);

DESCRIBE player;

UPDATE player
SET team_id=2
    first_name ='Gandalf',
    last_name = 'White'  
WHERE player_id = 12;

DESCRIBE player;

DELETE FROM player
WHERE player_id = 12;

DESCRIBE player;