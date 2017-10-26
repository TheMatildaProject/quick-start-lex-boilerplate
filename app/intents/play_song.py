import random

class PlaySong(object):
    def handle(self):
        return self.getRandomResponse()

    def getRandomResponse(self):
        return random.choice(self.getResponses())

    def getResponses(self):
        return [
            'Find it on yotuube then',
            "That's what's Spotify is for"
        ]
