
def team_max_striker(player_stats):
    """
    Esta funcion recibe una lista de diccionarios con las estadisticas de los jugadores y devuelve al maximx goleadorx del equipo y la cantidad de goles que hizo
    """
    max_striker_goals = 0

    for player in player_stats:
        if player["goals"] > max_striker_goals:
            max_striker_goals = player["goals"]
            max_striker = player["name"]
    return max_striker_goals, max_striker

def most_influent_player(player_stats):
    """
    Esta funcion recibe una lista de diccionarios con las estadisticas de los jugadores y devuelve al jugadorx más influyente del equipo y los puntos de influencia que consiguió
    """
    mvp_points = 0

    for player in player_stats:
        total_influent = player["goals"]*1.5 + player["goals_avoided"]*1.25 + player["assists"]
        if total_influent > mvp_points:
            mvp_points = total_influent
            mvp = player["name"]
    return mvp_points, mvp

def team_goals(player_stats):
    """
    Esta funcion recibe una lista de diccionarios con las estadisticas de los jugadores y devuelve la cantidad de goles totales que metió el equipo
    """
    total_goals = sum(map(lambda player: player["goals"], player_stats))
    return total_goals