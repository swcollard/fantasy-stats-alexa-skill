class Player:
    def __init__(self, name, position, team_abbr, stats, season_pts,
                 season_projected_pts, week_pts, week_projected_pts):
        self.name = name
        self.position = position
        self.team_abbr = team_abbr
        self.stats = stats
        self.season_pts = season_pts
        self.season_projected_pts = season_projected_pts
        self.week_pts = week_pts
        self.week_projected_pts = week_projected_pts

    def __str__(self):
        return str(self.name) + ' has ' + str(self.week_pts) + ' points this week.'


def decode_player(player):
    return Player(name=str(player['name']),
                  position=str(player['position']),
                  team_abbr=str(player['teamAbbr']),
                  stats=str(player['stats']),
                  season_pts=str(player['seasonPts']),
                  season_projected_pts=str(player['seasonProjectedPts']),
                  week_pts=str(player['weekPts']),
                  week_projected_pts=str(player['weekProjectedPts']))
