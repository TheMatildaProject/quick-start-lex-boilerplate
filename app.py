import json, boto3, sys
from app.intents.chit_chat import ChitChat
from app.intents.play_song import PlaySong


lex = boto3.client('lex-runtime', region_name='us-east-1', aws_access_key_id=sys.argv[1], aws_secret_access_key=sys.argv[2])

while True:
    var = input("")

    lex_response = lex.post_text(botName='exampletestone', botAlias='exampletestone', userId='asdasdsa', inputText=var)

    if ('intentName' in lex_response):
        if (lex_response['dialogState'] == 'ReadyForFulfillment'):
            intent_class = eval(lex_response['intentName'])()
            print(intent_class.handle())
        else:
            print(lex_response['message'])

    else:
        print(lex_response['message'])
