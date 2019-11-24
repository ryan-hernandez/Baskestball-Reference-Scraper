class Player:

    stats = []
    def __init__(self, stats):
        self.stats = stats

    def print_player(self):
        player = ""
        for stat in self.stats:
            player += stat.value + " "
        return str(player)