import requests


def getJoke():
    resp = requests.get('https://sv443.net/jokeapi/v2/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist')

    try:
        fmt = "Q: {} \nA: {}"
        rs = resp.json()
        return fmt.format(rs['setup'], rs['delivery'])
    except:
        return "I was not able to access my joke bank."
