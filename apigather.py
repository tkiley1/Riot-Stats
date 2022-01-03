#!usr/bin/env python
from riotwatcher import LolWatcher, ApiError
from tst import *
import apikey
import InVade_Players
import json
import pandas as pd


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
    for i in range(len(my_ranked)):
        if my_ranked[i]['queueType'] == 'RANKED_FLEX_SR':
            FLEX = i
        if my_ranked[i]['queueType'] =='RANKED_SOLO_5x5':
            SOLODUO = i

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
    for i in range(len(my_ranked)):
        if my_ranked[i]['queueType'] == 'RANKED_FLEX_SR':
            FLEX = i
        if my_ranked[i]['queueType'] =='RANKED_SOLO_5x5':
            SOLODUO = i
    mrank = str(my_ranked[SOLODUO]['tier']) + ' ' + str(my_ranked[SOLODUO]['rank'])
    mwins = float(my_ranked[SOLODUO]['wins'])
    mlosses = float(my_ranked[SOLODUO]['losses'])
    mlp = (my_ranked[SOLODUO]['leaguePoints'])
    mname = my_ranked[SOLODUO]['summonerName']
    stats_i_care_about = {'name' : mname, 'rank' : mrank, 'lp' : mlp, 'wins' : mwins, 'losses' : mlosses, 'ratio' : f"{float(mwins/mlosses):.3f}"}

    my_matches = get_match_history(me['puuid'], my_region, api_key)
    # fetch last match detail
    last_match = my_matches[0]
    #match_detail = watcher.match.by_id(my_region, last_match)
    match_detail = get_match_info(my_region, last_match, api_key)
    participants = []
    for row in match_detail['info']['participants']:
        participants_row = {}
        participants_row['player'] = get_name_from_id(my_region, row['puuid'], api_key)['gameName']
        participants_row['champion'] = row['championName']
        participants_row['lane'] = row['lane']
        participants_row['role'] = row['role']
        #participants_row['spell1'] = row['spell1Id']
        #participants_row['spell2'] = row['spell2Id']
        participants_row['win'] = row['win']
        participants_row['kills'] = row['kills']
        participants_row['deaths'] = row['deaths']
        participants_row['assists'] = row['assists']
        participants_row['totalDamageDealt'] = row['totalDamageDealt']
        participants_row['goldEarned'] = row['goldEarned']
        participants_row['champLevel'] = row['champLevel']
        participants_row['totalMinionsKilled'] = row['totalMinionsKilled']
        participants_row['item0'] = row['item0']
        participants_row['item1'] = row['item1']
        participants_row['item2'] = row['item2']
        participants_row['item2'] = row['item3']
        participants_row['item2'] = row['item4']
        participants_row['item2'] = row['item5']
        participants.append(participants_row)
    df = pd.DataFrame(participants)
    return(df.to_html())

def return_home_page_stats():
    player_info = {}
    ret_string = ""
    for i in player_list:
        ret_string = ret_string + '<h1>' + str(i) + "'s Most Recent Game </h1>" + '<br>' + str(return_player_stats_by_name(i))
    return(ret_string)
