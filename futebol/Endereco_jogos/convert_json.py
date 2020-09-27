import json


def json_importer(file_to_inport):
    with open(f"Endereco_jogos/{file_to_inport}.json") as file:
        games = json.load(file)[file_to_inport]
        game_keys = list(games.keys())
        all_links = []
        for rodada in game_keys:
            games_links = [game_link for game_link in games[rodada][0]]
            all_links.extend(games_links)
        return all_links