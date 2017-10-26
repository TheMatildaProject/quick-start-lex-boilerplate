import random

class ChitChat(object):
    def handle(self):
        return self.getRandomResponse()

    def getRandomResponse(self):
        return random.choice(self.getResponses())

    def getResponses(self):
        return [
            'Hi',
            'Hello',
            'Sup?'
        ]
