from flask import Flask, jsonify, request
from random import choice, randint, uniform

app = Flask(__name__)

MESSAGES = [
    "Hello",
    "This is a test message.",
    "How are you?",
    "Hello there.",
    "I'm good.",
    "This is another test message.",
    "Goodbye!"
]


@app.route('/api/conversation/start', methods=['GET'])
def conversation_start():
    return jsonify({'cid': randint(1000, 10000)})


@app.route('/api/conversation/end/<int:cid>', methods=['GET'])
def conversation_end(cid):
    return 'OK', 200


@app.route('/api/conversation/flag/<int:cid>', methods=['GET'])
def conversation_flag(cid):
    return 'OK', 200


@app.route('/api/conversation/send/<int:cid>', methods=['POST'])
def conversation_send(cid):
    return 'OK', 200


@app.route('/api/conversation/receive/<int:cid>', methods=['GET'])
def conversation_receive(cid):
    if uniform(0, 1) < 0.15:
        return jsonify({'messages': [{'id': 0, 'text': choice(MESSAGES), 'timestamp': '2020-01-01 00:00:00'}]})
    else:
        return jsonify({'messages': []})


@app.route('/api/conversation/guess/<int:cid>', methods=['POST'])
def conversation_guess(cid):
    if uniform(0, 1) < 0.5:
        return jsonify({'result': 0})
    else:
        return jsonify({'result': 1})


@app.route('/api/conversation/typing/set/<int:cid>', methods=['GET'])
def conversation_typing_set(cid):
    return 'OK', 200


@app.route('/api/conversation/typing/get/<int:cid>', methods=['GET'])
def conversation_typing_get(cid):
    if uniform(0, 1) < 0.2:
        return jsonify({'typing': 1})
    else:
        return jsonify({'typing': 0})


@app.route('/api/leaderboards', methods=['GET'])
def leaderboards():
    return jsonify({'users': [
        {'rank': 0, 'username': 'user1', 'score': 0.95},
        {'rank': 1, 'username': 'user2', 'score': 0.90},
        {'rank': 2, 'username': 'user3', 'score': 0.85},
        {'rank': 3, 'username': 'user4', 'score': 0.80},
        {'rank': 4, 'username': 'user5', 'score': 0.75}
    ]})


app.run(port=8080)
