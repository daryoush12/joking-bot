import requests


def getJoke():
    resp = requests.get('https://sv443.net/jokeapi/v2/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist')

    if resp.status_code != 200:
        return None;
    else:
        fmt = "Q: {} \nA: {}"
        rs = resp.json()
        return fmt.format(rs['setup'], rs['delivery'])
