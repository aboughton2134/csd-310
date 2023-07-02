SELECT * FROM player;
SELECT team_id, team_name, mascot FROM team;
cursor = db.cursor()
cursor.execute(“SELECT team_id, team_name, mascot FROM team”)
cursor.execute("SELECT player_id, first_name, last_name FROM player")
teams = cursor.fetchall()
player = cursor.fetchall()

for team in teams:
print(“Team Name: {}”.format(team[1]))