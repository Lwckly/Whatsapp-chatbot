import json
from dotenv import load_dotenv
import os
import requests
import aiohttp
import asyncio


load_dotenv()
ACCESS_TOKEN = str(os.getenv("EAAXD1z1dIBsBO42KTWnzbjwucaicLZCHzXZBaO9obiJB89MP5AVUXLZAXb3DhUKSUwqM1FeNtzc7wZBsIicZBRBBiFeJ3b0DcBeJhfZASk6fUznpQIjX2Wl2fDvawtUZCD2x1ZBJymowlf13AFYWmpHqjLYLIOYLMsajPlyaSiPfujai1HITXMZBLslPUXhS4Of91PGfwugQDTe6aOd9awkg39nRsq35S"))
RECIPIENT_WAID = os.getenv("+xxxxx")
PHONE_NUMBER_ID = os.getenv("xxxxx")
VERSION = os.getenv("22")

APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")
def send_whatsapp_message():
    url = f"https://graph.facebook.com/{VERSION}/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": "Bearer " + "EAAXD1z1dIBsBO42KTWnzbjwucaicLZCHzXZBaO9obiJB89MP5AVUXLZAXb3DhUKSUwqM1FeNtzc7wZBsIicZBRBBiFeJ3b0DcBeJhfZASk6fUznpQIjX2Wl2fDvawtUZCD2x1ZBJymowlf13AFYWmpHqjLYLIOYLMsajPlyaSiPfujai1HITXMZBLslPUXhS4Of91PGfwugQDTe6aOd9awkg39nRsq35S",
        "Content-Type": "application/json",
    }
    data = {
        "messaging_product": "whatsapp",
        "to": RECIPIENT_WAID,
        "type": "template",
        "template": {"name": "hello_world", "language": {"code": "en_US"}},
    }
    response = requests.post(url, headers=headers, json=data)
    return response

response = send_whatsapp_message()
print(response.status_code)
print(response.json())

#this been done in a while so Ill review it later, if im correct, its about kinda of working , believe all the keys are not useful anymore
