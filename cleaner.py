from datetime import datetime


def get_clean_match_data(raw_match_data: dict, puuid: str) -> dict | None:
    info = raw_match_data["info"]
    game_start = datetime.fromtimestamp(info["gameStartTimestamp"] / 1000.0)
    game_duration_minutes = info["gameDuration"] / 60.0

    if game_duration_minutes < 10:
        return None

    participants = info["participants"]
    player = next(p for p in participants if p["puuid"] == puuid)
    player_challenges = player["challenges"]
    opponent = next(
        p
        for p in participants
        if p["teamPosition"] == player["teamPosition"]
        and p["teamId"] != player["teamId"]
    )

    cs_per_minute = (
        player["totalMinionsKilled"] + player["neutralMinionsKilled"]
    ) / game_duration_minutes
    gold_per_minute = player["goldEarned"] / game_duration_minutes

    opponent_cs_per_minute = (
        opponent["totalMinionsKilled"] + opponent["neutralMinionsKilled"]
    ) / game_duration_minutes
    opponent_gold_per_minute = opponent["goldEarned"] / game_duration_minutes

    return {
        "game_start": game_start.strftime("%Y-%m-%d %H:%M:%S"),
        "game_duration_minutes": game_duration_minutes,
        "win": player["win"],
        "champion": player["championName"],
        "opponent_champion": opponent["championName"],
        "role": player["teamPosition"],
        "kills": player["kills"],
        "deaths": player["deaths"],
        "assists": player["assists"],
        "kill_participation": player_challenges["killParticipation"],
        "team_damage_percentage": player_challenges["teamDamagePercentage"],
        "damage_per_minute": player_challenges["damagePerMinute"],
        "vision_score_per_minute": player_challenges["visionScorePerMinute"],
        "cs_per_minute": cs_per_minute,
        "gold_per_minute": gold_per_minute,
        "opponent_cs_per_minute": opponent_cs_per_minute,
        "opponent_gold_per_minute": opponent_gold_per_minute,
    }
