# coding: utf8
import urllib2
import csv
from datetime import datetime
from bs4 import BeautifulSoup

class scraper:

    def player_per_game_scraper(self, year, per_game, per_min):
        # Header list for the .csv file
        header_per_game = ["Player", "Pos", "Age", "Tm", "G", "GS", "MP", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "2P", "2PA", "2P%", "eFG%", 
                "FT", "FTA", "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS"]
        header_per_min = header_per_game = ["Player", "Pos", "Age", "Tm", "G", "GS", "MP", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "2P", "2PA", "2P%", 
                "FT", "FTA", "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS"]

        # URL to scrape
        if per_game:
            quote_page = "https://www.basketball-reference.com/leagues/NBA_" + str(year).encode('utf-8') + "_per_game.html"
        elif per_min:
            quote_page = "https://www.basketball-reference.com/leagues/NBA_" + str(year).encode('utf-8') + "_per_minute.html"

        # Parse page using BeautifulSoup and store in soup
        soup = self.make_soup(quote_page)
        
        if per_game:
            # Table rows from the scraped page
            player_table_rows = self.get_rows(soup, per_game, per_min)
        if per_min:
            player_table_rows = self.get_rows(soup, per_game, per_min)
        # Individual player data parsed from table
        player_data = self.parse_rows(player_table_rows)

        if per_game:
            # Filename for .csv
            filename = "data/per_game/player_per_game_stats_" + str(year).encode('utf-8') + ".csv"
        elif per_min:
            # Filename for .csv
            filename = "data/per_min/player_per_min_stats_" + str(year).encode('utf-8') +".csv"
        
        # Writes data to .csv
        if per_game:
            self.write_file(filename, header_per_game, player_data)
        elif per_min:
            self.write_file(filename, header_per_min, player_data)

    def make_soup(self, quote_page):
        try:
            # Query website and return html to variable 'page'
            page = urllib2.urlopen(quote_page)
        except urllib2.URLError as e:
            print("An error occured fetching %s \n %s" % (quote_page, e.reason))
            return 1
        soup = BeautifulSoup(page, "html.parser")

        return soup

    def get_rows(self, soup, per_game, per_min):
        try: 
            if per_game:
                player_table = soup.find("table", attrs={"id": "per_game_stats"})
            elif per_min:
                player_table = soup.find("table", attrs={"id": "per_minute_stats"})
            player_table_body = player_table.find("tbody")
            player_table_rows = player_table_body.find_all("tr")
        except AttributeError as e:
            print("No table found \n %s" % (e.message))
            return 1

        return player_table_rows
        
    def parse_rows(self, rows):
        # List containing table data for each player
        player_data = []

        # Iterates over each row in the list of rows
        for row in rows:
            player_cols = row.find_all("td")
            new_player_cols = []
            for ele in player_cols:
                if not ele.text.encode('utf-8').strip() or ele.text.strip() == "xe9":
                    new_player_cols.append(" ")
                else: 
                    new_player_cols.append(ele.text.strip())
            player_data.append([ele for ele in new_player_cols if ele])
        
        return player_data

    def write_file(self, filename, header, player_data):
        with open(filename, "w") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)
            for player in player_data:
                if player:
                    player_info = []
                    for stat in player:
                        player_info.append(stat)
                    try:
                        writer.writerow(player_info)
                    except UnicodeEncodeError as e:
                        print(e.message)

