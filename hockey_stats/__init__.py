
def team_max_striker(player_stats):
    max_striker_goals = 0

    for player in player_stats:
        if player["goals"] > max_striker_goals:
            max_striker_goals = player["goals"]
            max_striker = player["name"]
    return max_striker_goals, max_striker
