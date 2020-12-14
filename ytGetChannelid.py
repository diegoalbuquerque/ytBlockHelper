#!/usr/bin/env python3
#
# Get all channel IDs from a specific Channel Name or User Name
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
# USAGE: ytGetChannelid.py -k <API_KEY> -c <CHANNEL_NAME_OR_USER_NAME>
# 

import json
import requests
import argparse

def getChanneID ( ChannelNAME, APIKEY ): 

	URL = "https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&fields=items%2Fsnippet%2FchannelId&q="+ChannelNAME+"&key="+APIKEY

	allChannels=list()

	response = requests.get(URL)
	contents = json.loads(response.text)

	numresults = len(contents["items"])

	for i in range(numresults): 
		channelId = contents["items"][i]["snippet"]["channelId"]
		allChannels.append(channelId)

	print(allChannels)

def main():

    ap = argparse.ArgumentParser("Get all Channel IDs from a specific Youtube Channel or Youtube User Name ")
    ap.add_argument("-c", "--channelname", required=True, help="Desired Channel Name ")
    ap.add_argument("-k", "--key", required=True, help="Your Youtube API key")

    args = vars(ap.parse_args())

    _APIKEY    = args["key"]
    _CHANNELID = args["channelname"]

    getChanneID( _CHANNELID, _APIKEY )

if __name__ == "__main__":
    main()


