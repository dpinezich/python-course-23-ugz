import soccer_helper
team = {
    "99": {"position": "Keeper", "name": "Donnarumma", "worth": 50000000},
    "4": {"position": "Keeper", "name": "Rico", "worth": 4000000},
    "5": {"position": "Defender", "name": "Marquinhos", "worth": 70000000},
    "3": {"position": "Defender", "name": "Kimpembe", "worth": 35000000},
    "8": {"position": "Midfielder", "name": "Ruiz", "worth": 3800000},
    "35": {"position": "Midfielder", "name": "Gharbi", "worth": 500000},
    "10": {"position": "Striker", "name": "Neymar", "worth": 70000000},
    "30": {"position": "Striker", "name": "Messi", "worth": 45000000},
    "7": {"position": "Striker", "name": "Mbappé", "worth": 180000000},
}

soccer_helper.show_players(team)

