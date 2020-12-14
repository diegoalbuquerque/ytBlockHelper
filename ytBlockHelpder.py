#!/usr/bin/env python3
#
#
#
# ▓██   ██▓▄▄▄█████▓    ▄▄▄▄    ██▓     ▒█████   ▄████▄   ██ ▄█▀    ██░ ██ ▓█████  ██▓     ██▓███  ▓█████  ██▀███  
#  ▒██  ██▒▓  ██▒ ▓▒   ▓█████▄ ▓██▒    ▒██▒  ██▒▒██▀ ▀█   ██▄█▒    ▓██░ ██▒▓█   ▀ ▓██▒    ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
#   ▒██ ██░▒ ▓██░ ▒░   ▒██▒ ▄██▒██░    ▒██░  ██▒▒▓█    ▄ ▓███▄░    ▒██▀▀██░▒███   ▒██░    ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
#   ░ ▐██▓░░ ▓██▓ ░    ▒██░█▀  ▒██░    ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄    ░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
#   ░ ██▒▓░  ▒██▒ ░    ░▓█  ▀█▓░██████▒░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄   ░▓█▒░██▓░▒████▒░██████▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
#    ██▒▒▒   ▒ ░░      ░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒    ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
#  ▓██ ░▒░     ░       ▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░    ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
#  ▒ ▒ ░░    ░          ░    ░   ░ ░   ░ ░ ░ ▒  ░        ░ ░░ ░     ░  ░░ ░   ░     ░ ░   ░░          ░     ░░   ░ 
#  ░ ░                  ░          ░  ░    ░ ░  ░ ░      ░  ░       ░  ░  ░   ░  ░    ░  ░            ░  ░   ░     
#  ░ ░                       ░                  ░                                                                  
#
#                         YOUTUBE BLOCK HELPER
#                       for a youtube without shits 
#                         by diegoalbuquerque  
#
#
# Script to get all video urls from a given Youtube channel id!
#
# The initial motivation to creation of this script was to catch all urls of a given channel to put in a WAF or something similar
# to block specifics channels. 
#
#               -_-_** GET YOUTUBE API KEY **_-_-
#
# To use this script It's necessary to get an youtube api key. 
#
# Follow the steps below to create an API Key.
#   
#       Go to the Google Developer Console https://console.developers.google.com.
#       Create or select a project
#       Type a name of your project. Google Console will create unique project ID.
#       After creating a project, it will appear on top of the left sidebar.
#       Click on Library. You will see list of Google APIs.
#       Enable YouTube Data API.
#       Click on the Credentials. Select API key under Create credentials.
#       Copy the API key. We will need it in a moment.
#
#
#            -_-_** GET YOUTUBE CHANNEL ID **_-_- 
#
# There is some options.
# 
# 1 - Search for <meta itemprop="channelId" content=" in source code of Channel,  like : 
#     curl  https://www.youtube.com/user/<YOUTUBE_USER> | grep '<meta itemprop="channelId" content='
#    
# 2 - Use this site: https://commentpicker.com/youtube-channel-id.php
#
# 3 - Use the  yt-get-channelid.py script at this repository, 
#
#
# USAGE: ytBlockHelper.py -k <API_KEY> -c <YOUTUBE_CHANNEL_ID> 


import json
import requests
import argparse


def getURLS( APIKEY, CHANNELID ):

    URL = "https://www.googleapis.com/youtube/v3/search?channelId="+CHANNELID+"&order=date&part=snippet&type=video&maxResults=50&key="+APIKEY

    allURLS=list()

    response = requests.get(URL)
    contents = json.loads(response.text)

    #Na primeira requisicao sera recuperada:
    #   totalResults: A quantidade total de resultados
    #   resultsPerPage: Quantidaade de resultados por pagina (o limite da API e de 50)
    #   nextPageToken : O token que devera ser inserido no parametro pageToken para iterar sobre todas as paginas

    nextPageToken   = contents["nextPageToken"]
    totalResults    = contents["pageInfo"]["totalResults"]
    resultsPerPage  = contents["pageInfo"]['resultsPerPage']

    #Iterar ate que a quantidade de resultados por pagina seja menor que 50. 
    #for page in range(int(totalGets)): 
    page = 1

    while 1: 

        if resultsPerPage < 50: break

        print("[+] Getting results - page %i " % (page) )
        page=page+1

    	# Captura todos os videos listados na pagina de resultado
        for i in range(resultsPerPage): 
            videoId = contents["items"][i]["id"]["videoId"]
            allURLS.append("https://youtube.com/watch?v="+videoId)

        print ("[+] .... %i urls captured " % (len(allURLS)))

        # Monta a URL com o novo token para nova pagina com os proximos resultados
        URL = "https://www.googleapis.com/youtube/v3/search?channelId="+CHANNELID+"&order=date&part=snippet&type=video&maxResults=50&key="+APIKEY+"&pageToken="+nextPageToken
        response = requests.get(URL)
        contents = json.loads(response.text)

        nextPageToken   = contents["nextPageToken"]
        resultsPerPage  = contents["pageInfo"]['resultsPerPage']
        

    print("[+] Total captured URLS =  %i " % (len(allURLS)) )
    print("[+] Captured URLS:  ")
    print(allURLS)


def main():

    ap = argparse.ArgumentParser("Get all video URLS from a specific Youtube channel ID")
    ap.add_argument("-k", "--key", required=True, help="Your Youtube API key")
    ap.add_argument("-c", "--channelid", required=True, help="Desired Channel ID")

    args = vars(ap.parse_args())

    _APIKEY    = args["key"]
    _CHANNELID = args["channelid"]

    getURLS( _APIKEY, _CHANNELID)

if __name__ == "__main__":
    main()




