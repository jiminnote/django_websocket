import json
from channels.generic.websocket import WebsocketConsumer

from random import randint
from time import sleep
from integers.models import Integer

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    
        for i in range(1000):
            x = randint(1,100)
            Integer.objects.create(
                random  = x
            )
            self.send(json.dumps({'message' : x}))

            sleep(1)