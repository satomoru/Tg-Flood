from telethon.sync import TelegramClient
from telethon.errors import PhoneCodeInvalidError
from time import sleep
import os, sys
import pathlib
import linecache

phone_numbers = input("phone_number: ")
#
api_id = 10953300
api_hash = '9c24426e5d6fa1d441913e3906627f87'
#
session = "uzzz"
client = TelegramClient(session, api_id, api_hash)
client.connect()
#
for number in phone_numbers:
    try:
        client.send_code_request(number)
        print(f"Code request sent to {number}")
       
    try:
     client.sign_in(phone_numbers, '123456')
    except PhoneCodeInvalidError:
     sleep(1)
     print("succesed  ✓")

os.remove("uzzz.session")
os.system("python 1s.py"
