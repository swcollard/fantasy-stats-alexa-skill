import nfl_client

players = nfl_client.fetch_player_name_map(2017, 6)
while True:
    x = raw_input("name > ")
    if x == 'exit':
        break
    print players[x.lower()]



