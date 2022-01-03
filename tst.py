
import json
import requests
def get_match_history(pid, region, key, lim=20):
    req = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/' + str(pid) + '/ids?start=0&count=' + str(lim) + '&api_key=' + str(key)
    x = requests.get(req).content
    x = str(x)[1:]
    x = x.replace("'",'')
    x = x.replace('"', '')
    x = x.replace('[','')
    x = x.replace(']','')
    match_list = x.split(',')
    return match_list

def get_match_info(region, mid, key):
    req = 'https://americas.api.riotgames.com/lol/match/v5/matches/' + str(mid) + '?api_key=' + str(key)
    info = json.loads(requests.get(req).content)
    return info

def get_name_from_id(region, pid, key):
    req = 'https://americas.api.riotgames.com/riot/account/v1/accounts/by-puuid/' + str(pid)  + '?api_key=' + str(key)
    info = json.loads(requests.get(req).content)
    return info
