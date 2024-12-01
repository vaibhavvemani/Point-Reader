import requests
import json

def get_meaning(word):
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    data = json.loads(response.text)
    print(data[0]['meanings'][0]['definitions'][0]['definition'])
get_meaning('altercation')