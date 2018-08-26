import nfl_client
from player import sort_by_week_points

players = sort_by_week_points(nfl_client.fetch_player_list(2017, 8))
for p in players:
    print str(p)
    x = raw_input("name > ")
    if x == 'exit':
        break


