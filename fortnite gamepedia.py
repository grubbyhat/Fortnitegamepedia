import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np

tracker = 'https://fortnite-esports.fandom.com/wiki/Power_Rankings/PC/Europe'
response = requests.get(tracker)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all("table", class_='wikitable')
dfs=pd.read_html(str(table))
df = dfs[0]
df.rename(columns = {'Unnamed: 4':'First Place', 'Unnamed: 5':'Second Place', 'Unnamed: 6':'Third Place', 'Unnamed: 7':'Fourth Place'}, inplace = True) 
df = df.drop([0])
df.fillna(0, inplace=True)
df.drop('Team', axis=1, inplace=True)
cols = ['First Place','Second Place','Third Place','Points','Fourth Place']
df[cols] = df[cols].applymap(np.int64)
pd.options.display.float_format = '{:,.0f}'.format

class Create_Player:
    def __init__(self, player_choice):
        try:
            player_tracker = f'https://fortnite-esports.fandom.com/wiki/{player}'
            response_player = requests.get(player_tracker)
            soup_player = BeautifulSoup(response_player.text, 'html.parser')
            player_achvs = soup_player.find_all("table", class_='wikitable')
            about = soup_player.find_all('table', class_='infobox')
            about_player = pd.read_html(str(about))
            dfs_player=pd.read_html(str(player_achvs))
            self.player = dfs_player
            if len(self.player) < 2:
                pass
            else:
                self.team = about_player[1]
                self.df_player_settings = dfs_player[0]
                self.df_player_achvs = dfs_player[1]
        except Exception as e:
            pass
def find_player(player_choice):
    player_tracker = f'https://fortnite-esports.fandom.com/wiki/{player_choice}'
    response_player = requests.get(player_tracker)
    soup_player = BeautifulSoup(response_player.text, 'html.parser')
    player_achvs = soup_player.find_all("table", class_='wikitable')
    about = soup_player.find_all('table', class_='infobox')
    about_player = pd.read_html(str(about))
    dfs_player=pd.read_html(str(player_achvs))
    df_player_settings = dfs_player[0]
    df_player_achvs = dfs_player[1]
    return df_player_settings, df_player_achvs, about_player

sens = 0
counter = 0
for player in df['Player']:
    try:
        player = Create_Player(player)
        print (len(player.player))
        if len(df_player) < 2: pass
        else:
            df_player_settings_1 = player.player[0]
            player_sens = df_player_settings.iloc[0]
            player_list = list(player_sens)
            print(player_list)
            if player_list[0] or player_list[1] == 'NaN': 
            else:
                sens_x = float(player_list[1].replace("%", ""))
                edpi = int(float(x[0])*sens_x)
                sens += edpi
                counter+=1
                print(counter)

   
    except Exception as e:
        pass

    
    
total_edpi = sens/counter


for player in df['Player']:
    print(player)
    sens = 0
    counter = 0
    player = Create_Player(player)
    player_sens = player.df_player_settings.iloc[0]
    player_list = list(player_sens)
    print(player_list[0],player_list[1])
    player_list[0].replace("nan", "0")
    player_list[1].replace("nan", "0")
    sens_x = float(player_list[1].replace("%", ""))
    edpi = int(float(x[0])*sens_x)
    sens += edpi
    counter+=1
    print(counter)
    
    
        