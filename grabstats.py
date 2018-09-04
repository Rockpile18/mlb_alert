import requests
import json
from six import iteritems

response = requests.get("https://api.sportradar.us/mlb/trial/v6/en/games/2018/06/15/boxscore.json?api_key=r56596kf9jzbazrmmyhvsvss")

data = response.json()

def gen_dict_extract(key, var):
    if hasattr(var,'iteritems'):
        for k, v in var.iteritems():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result

# def find_key_in_dictionary(key, dictionary):
#     for k, v in iteritems(dictionary):
#         if k == key:
#             yield v
#         elif isinstance(v, dict):
#             for result in find_key_in_dictionary(key, v):
#                 yield result
#         elif isinstance(v, list):
#             for d in v:
#                 for result in find_key_in_dictionary(key, d):
#                     yield result

print(list(gen_dict_extract('abbr', data)))

# print(data['league']['games'][0]['game']['away'])
