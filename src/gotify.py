import requests
from dotenv import load_dotenv
import os
load_dotenv()

class Gotify():

    def __init__(self):
        self._token=os.getenv("GOTIFY_TOKEN")
        self._baseURL=os.getenv("GOTIFY_URL")

    def pushMessage(self, message, title, priority=1):
        url=self._baseURL+"/message?token="+self._token
        body={
            "message": message,
            "priority": priority,
            "title": title
        }
        resp = requests.post(url, body)
        return body, url