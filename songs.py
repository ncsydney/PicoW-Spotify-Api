import requests
import config
import json
import time


def getSong():
    # Stores the current song that's playing
    cur_song = []

    # Stores the previous played song
    pre_song = []

    while True:

        get_play = requests.get(config.link_play(), headers={"Authorization": f"Bearer {config.token()}"})

        json_play = get_play.json()

        dump_play = json.dumps(json_play['item']['name'])

        artists = json_play['item']['artists']

        count = -1
        app = ''
        for i in artists:
            count += 1
            art = json.dumps(json_play['item']['artists'][count]['name'])
            songArtist = json.loads(art)
            app += f"{songArtist}, "

        songName = json.loads(dump_play)
                
        cur_song = songName

        if pre_song != cur_song:
            print(f"Now Playing: {cur_song} - {app[:-2]}")
            pre_song = cur_song
            
        time.sleep(1)


def pauseSong():

    paused = requests.put(config.link_pause(), headers={"Authorization": f"Bearer {config.token()}"})


def playSong():

    resume = requests.put(config.link_resume(), headers={"Authorization": f"Bearer {config.token()}"})

    

