import re
from json.decoder import JSONDecodeError

import flask
from flask import request, jsonify
import json

from connection import check as smpp_check, send as smpp_send

app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route('/send/', methods=['POST'])
def send():
    try:
        data = json.loads(request.data)
    except JSONDecodeError:
        response = {
            'success': False,
            'message': 'entered data is not json.',
            'response': None
        }
    else:
        try:
            phone_number = data['phone_number']
            message = data['message']
        except KeyError:
            response = {
                'success': False,
                'message': 'required params not send. (`phone_number`, `message`)',
                'response': None
            }
        else:
            if re.match(r'^(\+98|0)?9\d{9}$', phone_number):
                if len(data['message']) < 500:
                    smpp_send(phone_number, message)
                    response = {
                        'success': True,
                        'message': 'success',
                        'response': None
                    }
                else:
                    response = {
                        'success': False,
                        'message': '`message` is long.',
                        'response': None
                    }
            else:
                response = {
                    'success': False,
                    'message': '`phone_number` is not correct.',
                    'response': None
                }
    return jsonify(response)


@app.route('/check/', methods=['GET'])
def check():
    try:
        smpp_check()
    except Exception as ex:
        print(ex)

        response = {
            'success': False,
            'message': 'smpp connection refused',
            'response': None
        }
    else:
        response = {
            'success': True,
            'message': 'success',
            'response': None
        }
    return jsonify(response)


if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
