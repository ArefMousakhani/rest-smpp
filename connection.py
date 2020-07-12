import smpplib
import os
from smpplib import gsm
from smpplib import consts

HOST = os.environ['SMPP_HOST']
POST = os.environ['SMPP_PORT']
SYSTEM_ID = os.environ['SMPP_SYSTEM_ID']
PASSWORD = os.environ['SMPP_PASSWORD']
SOURCE_ADDRESS = os.environ['SMPP_SOURCE_ADDRESS']

client = smpplib.client.Client(HOST, POST)


def check():
    client.connect()
    client.bind_transceiver(system_id=SYSTEM_ID, password=PASSWORD)
    client.disconnect()


def send(phone_number, message):
    client.connect()
    client.bind_transceiver(system_id=SYSTEM_ID, password=PASSWORD)
    parts, encoding_flag, msg_type_flag = gsm.make_parts(message)
    for part in parts:
        client.send_message(
            source_addr_ton=smpplib.consts.SMPP_TON_ALNUM,
            source_addr_npi=smpplib.consts.SMPP_NPI_UNK,
            source_addr=SOURCE_ADDRESS,

            dest_addr_ton=smpplib.consts.SMPP_TON_INTL,
            dest_addr_npi=smpplib.consts.SMPP_NPI_ISDN,
            destination_addr=phone_number,
            short_message=part,

            data_coding=encoding_flag,
            esm_class=msg_type_flag,
            registered_delivery=True,
        )

    client.disconnect()
