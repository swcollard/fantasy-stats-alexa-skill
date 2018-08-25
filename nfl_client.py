import json
import player
import urllib2

BASE_URL = 'http://api.fantasy.nfl.com/v1/players/stats?statType=seasonStats&season={0}&week={1}&format=json'


def call_nfl(year, week):
    url = BASE_URL.format(year, week)
    url_response = urllib2.urlopen(url)
    return json.load(url_response)


def fetch_player_list(year, week):
    players = []
    player_json = call_nfl(year, week)
    for p in player_json['players']:
        players.append(player.decode_player(p))
    return players


def fetch_player_name_map(year, week):
    players = {}
    player_json = call_nfl(year, week)
    for p in player_json['players']:
        player_obj = player.decode_player(p)
        players[player_obj.name.lower()] = player_obj
    return players
