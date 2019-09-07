import os
import dotenv
import requests
dotenv.load_dotenv()


TOKEN = os.getenv("ID")


def authRequest(url, params=()):
    headers = {
    'Client-ID': TOKEN
    }
    response = requests.get(url, headers=headers,params= params)
    return response.json()



def addtwitchId(serie):
    url= 'https://api.twitch.tv/helix/users?login='
    twitch=[]
    for player in serie:
        complete_url = url+player
        request = authRequest(complete_url)
        try:
            twitch.append(request['data'][0]['id'])
            print(request['data'][0]['id'],request['data'][0]['login'])
        except:
            twitch.append('no response from twitch')
            print('no response from twitch')
        time.sleep(0.6)
        
    return twitch



