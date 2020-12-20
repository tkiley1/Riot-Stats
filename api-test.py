#!usr/bin/env python

from riotwatcher import LolWatcher, ApiError
import pandas as pd

SOLODUO = 0
FLEX = 1

# golbal variables
api_key = 'RGAPI-7b05da3f-984a-44c0-b79a-fa0b89d413c9'
watcher = LolWatcher(api_key)
my_region = 'na1'

me = watcher.summoner.by_name(my_region, 'InVade Flymuf')
my_ranked = watcher.league.by_summoner(my_region, me['id'])
my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])
print(len(my_matches['matches']))
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
print(stats_i_care_about)
