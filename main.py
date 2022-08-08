from urllib import request
import requests
from bs4 import BeautifulSoup
import json


def get_rankings(region_link): #returns the top ten teams in a specific reagion given by the region link
    r = requests.get(region_link)
    soup = BeautifulSoup(r.content, 'html.parser')
    list_of_teams = []
    for i in soup.findAll('div', class_='ge-text'):
        list_of_teams.append(str(i.get_text(",", strip=True)))
    team_rankings ={}
    for i in range(10): #len(list_of_teams) for all teams in that region
        list_of_teams[i]= list_of_teams[i].split(',')
        team_rankings[i]= list_of_teams[i][0]
    return team_rankings
def player_stats(team_link): # returns all the players of teams given the link
    r = requests.get(team_link)
    soup = BeautifulSoup(r.content,'html.parser')
    team = soup.find("h1", class_='wf-title')
    # print(team.get_text(strip =True))
    player_names = []
    for i in soup.findAll("div", class_='team-roster-item-name-alias'):
        player_names.append(str(i.get_text(",", strip=True)))
    return(player_names)

def get_player_teams(region_link): #grabs the teams and each player from their respected teams and return in a dictonary
        r = requests.get(region_link)
        teams_ranking = get_rankings(region_link)
        soup = BeautifulSoup(r.content, 'html.parser')
        link_list=[]

        for link in soup.findAll('a',class_="rank-item-team fc-flex"):
            link_list.append(link.get('href'))
        player_teams = {}
        for i in teams_ranking:
            player_teams[teams_ranking[i]]= player_stats(f'https://www.vlr.gg{link_list[i]}')
        return player_teams    
        
        

player_list = get_player_teams("https://www.vlr.gg/rankings/north-america")
print(player_list)
with open('data.json', 'w') as f:
    json.dump(player_list,f,indent=4)

