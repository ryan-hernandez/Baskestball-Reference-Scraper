import csv, Stat, Player

class Season:

    header = []
    season_players = []

    def __init__(self, filename):
        self.parse(filename)

    def parse(self,filename):
        players = []
        with open(filename, "rb") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for row in reader:
                players.append([ele for ele in row if ele])

        self.header = players[0]

        for player in players:
            if player[0] == "Player":
                continue
            stats = []
            i = 0
            for ele in player:
                if i >= 28:
                    break
                stat = Stat.Stat(self.header[i], ele)
                stats.append(stat)
                i += 1
            season_player = Player.Player(stats)
            self.season_players.append(season_player)

        