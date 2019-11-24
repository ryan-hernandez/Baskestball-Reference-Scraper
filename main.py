import time, csv, scraper, Season, Stat

class main:
    
    seasons = []
    
    user_input = raw_input("Would you like to download per game data from basketball-reference? Y/N ")
    y = "y"
    if user_input.lower() == y:
        per_game = True
        per_min = False
        _scraper = scraper.scraper()

        year = 1950
        print("Creating .csv files...")
        while year < 2020:
            _scraper.player_per_game_scraper(year, per_game, per_min)
            year += 1
            #time.sleep(1)
            print("...")
            if year == 2010:
                print("...Almost done...")
        print("Done!")

    user_input = raw_input("Would you like to download per min data from basketball-reference? Y/N ")
    if user_input.lower() == y:
        per_game = False
        per_min = True

        _scraper = scraper.scraper()

        year = 1950
        print("Creating .csv files...")
        while year < 2020:
            _scraper.player_per_game_scraper(year, per_game, per_min)
            year += 1
            #time.sleep(1)
            print("...")
            if year == 2010:
                print("...Almost done...")
        print("Done!")
        
    year = 1950
    print("Starting...")
    while year < 2020:
        filename = "data/per_game/player_per_game_stats_" + str(year) + ".csv"
        season = Season.Season(filename)
        seasons.append(season)
        year += 1
    print("Finished!")
    
    def scrape(self, per_game, per_min):
        _scraper = scraper.scraper()

        year = 1950
        print("Creating .csv files...")
        while year < 2020:
            _scraper.player_per_game_scraper(year, per_game, per_min)
            year += 1
            #time.sleep(1)
            print("...")
            if year == 2010:
                print("...Almost done...")
        print("Done!")
