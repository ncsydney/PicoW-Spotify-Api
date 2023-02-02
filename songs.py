# Importeert benodigde bibliotheken
import requests
import config
import json
import time


# Maakt een functie die het momenteel spelende nummer ophaalt
def getSong():

    # Maakt een variabel aan waarin het nummer wordt opgeslagen dat momenteel speelt
    cur_song = []

    # Maakt een variabele om het eerder afgespeelde nummer op te slaan
    pre_song = []
 
    # Zet de code in een oneindige lus
    while True:
                
        get_playing_song = requests.get(config.link_play(), headers={"Authorization": f"Bearer {config.token()}"})

        # Krijgt de rauwe JSON data van de API
        json_play = get_playing_song.json()

        # Haalt de titel van het nummer uit de JSON data
        songTitle = json.dumps(json_play['item']['name'])

        # Haalt de artiestennamen uit de JSON data
        artists_list = json_play['item']['artists']

        # Itereert door de reeks artisten en zet deze in een lijst
        count = -1
        artists = ''
        for i in artists_list:
            count += 1
            art = json.dumps(json_play['item']['artists'][count]['name'])
            songArtist = json.loads(art)
            artists += f"{songArtist}, "

        # Zet het JSON-object om tot een string
        songName = json.loads(songTitle)
        
        # Zet het huidig spelende nummer (songName) gelijk aan het variabel cur_song
        cur_song = songName


        # Checkt de status van het vorige gespelde nummer, als het niet gelijk is aan het nummer dat momenteel speelt, print een nieuw nummer.
        if pre_song != cur_song:
            print(f"Now Playing: {cur_song} - {artists[:-2]}")
            
            # Zet de waarde van cur_song gelijk aan pre_song
            pre_song = cur_song
            
        # Zet de code op pauze voor 1000ms 
        time.sleep(10)


# Maakt een functie die het nummer pauzeert 
def pauseSong():

    pause_song = requests.put(config.link_pause(), headers={"Authorization": f"Bearer {config.token()}"})


# Maakt een functie die het nummer hervat
def resumeSong():

    resume_song = requests.put(config.link_resume(), headers={"Authorization": f"Bearer {config.token()}"})


# Maakt een functie die het nummer overslaat 
def skipNext():
    
    skip_next = requests.post(config.link_next, headers={"Authorization": f"Bearer {config.token()}"})


# Maakt een functie die terugaat naar het voorgaande nummer 
def skipPrevious():
    
    skip_previous = requests.post(config.link_previous, headers={"Authorization": f"Bearer {config.token()}"})