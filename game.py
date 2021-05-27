import random

class DiceGame():
    def __init__(self, initiator:str):
        self.score = {}
    
    def rollDice(self, roller:str):
        score = int(random.random() * 6)
        if roller not in self.score.keys():
            self.score[roller] = score
            return self.score[roller], score
        else:
            self.score[roller] += score
            return self.score[roller], score

    def getCurrentScore(self):
        title = "Score:\n"
        player = "{} - {} Points \n"
        players = ""
        for key in self.score.keys():
            players += player.format(key, self.score[key])
        
        return "```" + title + players + "```"

    def playerInGame(self, player:str):
        return player in self.score.keys()

    def join(self, player:str):
        self.score[player] = 0
        return player in self.score.keys()

class Welcomer():

    def __init__(self):
        self.welcomes = self.getwelcomes()

    def getRandomWelcomer(self):
        return self.welcomes[random.randint(0, len(self.welcomes))]
     
    def getwelcomes(self):
        options = []
        with open('welcomers.txt') as file:
            for row in file:
                clean = row.rstrip()
                options.insert(len(options), clean)
        return options

