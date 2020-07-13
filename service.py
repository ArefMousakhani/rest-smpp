import re
from json.decoder import JSONDecodeError

import flask
from flask import request, jsonify
import json

from smpp import check as smpp_check, send as smpp_send
from kavenegar import send as kavenegar_send

app = flask.Flask(__name__)
app.config["DEBUG"] = False


def phone_number_validate(value):
    if not re.match(r'^(\+98|0)?9\d{9}$', value):
        return False, 'Entered phone_number is not correct.'
    return True, None


def message_validate(value):
    if len(value) > 500:
        return False, 'Entered message is not correct.'
    return True, None


def method_validate(value):
    if value not in ['smpp', 'ht']:
        return False, 'Entered method is not correct.'
    return True, None


def check_data(data, fields):
    try:
        data = json.loads(data)
    except JSONDecodeError:
        return False, ['Entered data must be json'], None
    else:
        result = True
        messages = []
        for field in fields:
            method_result, method_error = globals()[f'{field}_validate'](data.get(field))
            result = result and method_result
            if method_error is not None:
                messages.append(method_error)
        return result, messages if messages else None, data


def json_response(success, result):
    return jsonify({
        'success': success,
        'message': 'Success' if success else 'Fail',
        'response': result
    })


@app.route('/send/', methods=['POST'])
def send():
    is_valid, errors, data = check_data(request.data, ['phone_number', 'message', 'method'])
    if is_valid:

        if data['method'] == 'smpp':
            try:
                smpp_send(data['phone_number'], data['message'])
            except Exception as ex:
                print(ex)
                return json_response(False, ['Internal server error'])
            else:
                return json_response(True, None)

        else:
            try:
                response = kavenegar_send(data['phone_number'], data['message'])
            except Exception as ex:
                print(ex)
                return json_response(False, ['Internal server error'])
            else:
                if response['return']['status'] == 200:
                    return json_response(True, None)
                else:
                    print(response)
                    return json_response(False, ['Internal server error'])

    else:
        return json_response(is_valid, errors)


@app.route('/check/', methods=['GET'])
def check():
    try:
        smpp_check()
    except Exception as ex:
        print(ex)
        return json_response(False, 'smpp connection refused')
    else:
        return json_response(True, None)


if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
