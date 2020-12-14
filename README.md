▓██   ██▓▄▄▄█████▓    ▄▄▄▄    ██▓     ▒█████   ▄████▄   ██ ▄█▀    ██░ ██ ▓█████  ██▓     ██▓███  ▓█████  ██▀███  
 ▒██  ██▒▓  ██▒ ▓▒   ▓█████▄ ▓██▒    ▒██▒  ██▒▒██▀ ▀█   ██▄█▒    ▓██░ ██▒▓█   ▀ ▓██▒    ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
  ▒██ ██░▒ ▓██░ ▒░   ▒██▒ ▄██▒██░    ▒██░  ██▒▒▓█    ▄ ▓███▄░    ▒██▀▀██░▒███   ▒██░    ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
  ░ ▐██▓░░ ▓██▓ ░    ▒██░█▀  ▒██░    ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄    ░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
  ░ ██▒▓░  ▒██▒ ░    ░▓█  ▀█▓░██████▒░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄   ░▓█▒░██▓░▒████▒░██████▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
   ██▒▒▒   ▒ ░░      ░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒    ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
 ▓██ ░▒░     ░       ▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░    ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
 ▒ ▒ ░░    ░          ░    ░   ░ ░   ░ ░ ░ ▒  ░        ░ ░░ ░     ░  ░░ ░   ░     ░ ░   ░░          ░     ░░   ░ 
 ░ ░                  ░          ░  ░    ░ ░  ░ ░      ░  ░       ░  ░  ░   ░  ░    ░  ░            ░  ░   ░     
 ░ ░                       ░                  ░                                                                  
	
#####                                             YOUTUBE BLOCK HELPER
#####                                         for a youtube without shits 
#####                                              by diegoalbuquerque  


A script to get all video urls from a given Youtube channel id!

The initial motivation to creation of this script was to catch all urls of a given channel to put in a WAF or something similar
to block specifics channels. 


#####              -_-_** GET YOUTUBE API KEY **_-_-

 To use this script It's necessary to get an youtube api key. 

 Follow the steps below to create an API Key.
   
       Go to the Google Developer Console https://console.developers.google.com.
       Create or select a project
       Type a name of your project. Google Console will create unique project ID.
       After creating a project, it will appear on top of the left sidebar.
       Click on Library. You will see list of Google APIs.
       Enable YouTube Data API.
       Click on the Credentials. Select API key under Create credentials.
       Copy the API key. We will need it in a moment.


#####            -_-_** GET YOUTUBE CHANNEL ID **_-_- 

There is some options.
 
1 - Search for <meta itemprop="channelId" content=" in source code of Channel,  like : 
    curl  https://www.youtube.com/user/<YOUTUBE_USER> | grep '<meta itemprop="channelId" content='
    
2 - Use this site: https://commentpicker.com/youtube-channel-id.php

3 - Use the  ytGetChannelid.py script at this repository, 

##### USAGE

ytBlockHelper.py -k <API_KEY> -c <YOUTUBE_CHANNEL_ID> 

