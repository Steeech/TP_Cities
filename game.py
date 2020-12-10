import math
from random import random
import json
import jsonschema
from jsonschema import validate

NUMBER_OF_PLAYERS = 2
MAX_INITIAL_DISTANCE = 10
MIN_INITIAL_DISTANCE = 2
MAX_ANGLE = 360

schema = {
    "type": "object",
    "properties": {
        "players": {
            "type": "array",
            "minItems": NUMBER_OF_PLAYERS,
            "maxItems": NUMBER_OF_PLAYERS,
            "items": {
                "username": {"type": "string"}
            }
        },
        "cities": {
            "type": "array",
            "items": {
                "city": {"type": "string"}
            }
        }
    },
    "required": [
        "players",
        "cities"
    ]
}


def create_player(username, cities, client):
    return Player(username, cities, client)


def parse_data(data):
    players = list()
    cities = list()
    for cities_data in data['cities']:
        cities.append(cities_data['city'])
    for player_data in data['players']:
        player = Player(player_data['username'],
                        cities,
                        None)
        players.append(player)
    return players


def init_players():
    players = list()
    cities = list()
    for i in range(0, NUMBER_OF_PLAYERS):
        players.append(
            create_player(
                f"player{i}", cities, None
            )
        )
    return players


def validate_json(data):
    try:
        validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


def load_game_state_from_json(json_file_path):
    with open(json_file_path) as json_file:
        try:
            data = json.load(json_file)
            if validate_json(data):
                return True, data
        except json.decoder.JSONDecodeError:
            pass
    return False, None


def dump_game_state_to_json(players, cities, json_file_path):
    data = {'players': [], "cities": []}
    for player in players:
        data['players'].append(player.dict())
    for city in player.cities:
        data['cities'].append({'city': city})
    with open(json_file_path, 'w') as outfile:
        json.dump(data, outfile, indent=4)


class Cities:
    def __init__(self, cities):
        self.cities = cities

    # def dict(self, city):
    #     return {
    #         'city': city
    #     }


class Player:

    def __init__(self, username, cities, client_socket):
        self.username = username
        self.cities = cities
        self.client_socket = client_socket

    def __str__(self):
        return f"Player username: {self.username}"

    # def cities(self):
    #     return self.cities.cities

    def move(self, city):
        self.cities.append(city.lower())

    def can_move(self, city):
        return self.cities[-1][-1] == (city.lower())[0]

    def fail(self, city):
        return city.lower() in set(self.cities)

    def dict(self):
        return {
            'username': self.username
        }
