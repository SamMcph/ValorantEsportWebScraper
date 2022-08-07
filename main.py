import requests
from bs4 import BeautifulSoup
class rankings():
    def na_ranking():
        r = requests.get('https://www.vlr.gg/rankings/north-america/')
        
        soup = BeautifulSoup(r.content, 'html.parser')
        list_of_teams = []
        for i in soup.findAll('div', class_='ge-text'):
            list_of_teams.append(str(i.get_text(",", strip=True)))
        team_rankings ={}
        for i in range(len(list_of_teams)):
            list_of_teams[i]= list_of_teams[i].split(',')
            team_rankings[i]= list_of_teams[i][0]
        return team_rankings
    def eu_ranking():
        r = requests.get('https://www.vlr.gg/rankings/europe')
        
        soup = BeautifulSoup(r.content, 'html.parser')
        list_of_teams = []
        for i in soup.findAll('div', class_='ge-text'):
            list_of_teams.append(str(i.get_text(",", strip=True)))
        team_rankings ={}
        for i in range(len(list_of_teams)):
            list_of_teams[i]= list_of_teams[i].split(',')
            team_rankings[i]= list_of_teams[i][0]
        return team_rankings
    def brazil_ranking():
        r = requests.get('https://www.vlr.gg/rankings/brazil')
        soup = BeautifulSoup(r.content, 'html.parser')
        list_of_teams = []
        for i in soup.findAll('div', class_='ge-text'):
            list_of_teams.append(str(i.get_text(",", strip=True)))
        team_rankings ={}
        for i in range(len(list_of_teams)):
            list_of_teams[i]= list_of_teams[i].split(',')
            team_rankings[i]= list_of_teams[i][0]
        return team_rankings
    def asia_pacific_ranking():
        r = requests.get('https://www.vlr.gg/rankings/asia-pacific')
        soup = BeautifulSoup(r.content, 'html.parser')
        list_of_teams = []
        for i in soup.findAll('div', class_='ge-text'):
            list_of_teams.append(str(i.get_text(",", strip=True)))
        team_rankings ={}
        for i in range(len(list_of_teams)):
            list_of_teams[i]= list_of_teams[i].split(',')
            team_rankings[i]= list_of_teams[i][0]
        return team_rankings   


