import requests
import os
TOKEN = os.environ['KAVENEGAR_KEY']


def send(phone_number, message):
    return requests.get(f'https://api.kavenegar.com/v1/{TOKEN}/sms/send.json', {
        'receptor': phone_number,
        'message': message,
    }).json()
