import os, sys
from flask import Flask, jsonify, request
from app.handlers.lex import Lex as LexHandler
from app.handlers.frontal_lobe import FrontalLobe

app = Flask(__name__)
lex = LexHandler()
fl = FrontalLobe()

@app.route('/', methods=['POST'])
def run():
    if not request.json or not 'message' in request.json:
        return jsonify({'error': 'Missing message'}), 400

    lexResponse = lex.sendMessage(request.json)
    response = fl.handleResponse(lexResponse)

    return jsonify({'message': response});

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
