#!usr/bin/env python
from riotwatcher import LolWatcher, ApiError
import apikey
import InVade_Players
import json


# golbal variables
api_key = apikey.api_key_ignored
player_list = InVade_Players.plist
watcher = LolWatcher(api_key)
my_region = 'na1'
SOLODUO = 0
FLEX = 1

#Depricated function to return player stats based on hardcoded value
def return_player_stats():
    me = watcher.summoner.by_name(my_region, 'KingLouieV5')
    my_ranked = watcher.league.by_summoner(my_region, me['id'])
    my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])
    if my_ranked[0]['queueType'] == 'RANKED_FLEX_SR':
        FLEX = 0
        SOLODUO = 1
    else:
        FLEX = 1
        SOLODUO = 0

    mrank = str(my_ranked[SOLODUO]['tier']) + ' ' + str(my_ranked[SOLODUO]['rank'])
    mwins = float(my_ranked[SOLODUO]['wins'])
    mlosses = float(my_ranked[SOLODUO]['losses'])
    mlp = (my_ranked[SOLODUO]['leaguePoints'])
    mname = my_ranked[SOLODUO]['summonerName']

    stats_i_care_about = {'name' : mname, 'rank' : mrank, 'lp' : mlp, 'wins' : mwins, 'losses' : mlosses, 'ratio' : f"{float(mwins/mlosses):.3f}"}
    return(stats_i_care_about)

#Function to return stats dynamically by player name
def return_player_stats_by_name(player_name):
    me = watcher.summoner.by_name(my_region, player_name)
    my_ranked = watcher.league.by_summoner(my_region, me['id'])
    if my_ranked[0]['queueType'] == 'RANKED_FLEX_SR':
        FLEX = 0
        SOLODUO = 1
    else:
        FLEX = 1
        SOLODUO = 0
    mrank = str(my_ranked[SOLODUO]['tier']) + ' ' + str(my_ranked[SOLODUO]['rank'])
    mwins = float(my_ranked[SOLODUO]['wins'])
    mlosses = float(my_ranked[SOLODUO]['losses'])
    mlp = (my_ranked[SOLODUO]['leaguePoints'])
    mname = my_ranked[SOLODUO]['summonerName']
    stats_i_care_about = {'name' : mname, 'rank' : mrank, 'lp' : mlp, 'wins' : mwins, 'losses' : mlosses, 'ratio' : f"{float(mwins/mlosses):.3f}"}
    return(stats_i_care_about)

def return_home_page_stats():
    player_info = {}
    for i in player_list:
        player_info[i] = return_player_stats_by_name(i)
    return(json.dumps(player_info, indent = 4))
