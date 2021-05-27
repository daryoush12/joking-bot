import requests

def getPokemon(name:str):
    resp = requests.get('https://pokeapi.co/api/v2/pokemon/'+name)
    pokemon = resp.json()
    info = "```{}```\n ```Height: {}\nWeight: {}``` \n{}"

    return info.format(pokemon['name'], pokemon['height'], pokemon['weight'], pokemon['sprites']['front_default'])
