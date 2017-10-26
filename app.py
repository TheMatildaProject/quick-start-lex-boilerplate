import json, boto3, sys

lex = boto3.client('lex-runtime', region_name='us-east-1', aws_access_key_id=sys.argv[1], aws_secret_access_key=sys.argv[2])

while True:
    var = input("Talk dirty to me: ")

    response = lex.post_text(botName='exampletestone', botAlias='exampletestone', userId='asdasdsa', inputText=var)

    print (response)
