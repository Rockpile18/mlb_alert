import requests
import json
from six import iteritems

response = requests.get("https://api.sportradar.us/mlb-t6/games/2018/06/15/boxscore.json?api_key=r56596kf9jzbazrmmyhvsvss")

data = response.json()

print(data)
