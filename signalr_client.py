from config import SIGNAL_R_URL
from signalrcore.hub_connection_builder import HubConnectionBuilder
import requests

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

class SignalRClient:
    # def __init__(self, url):
    #     self.connection = HubConnectionBuilder().with_url(url, options={"verify_ssl": False}).build()

    # def start(self):
    #     self.connection.start()

    # def send_message(self, message):
    #     self.connection.send("SendMessageToAll", [message])
    
    def __init__(self, url):
        self.connection = HubConnectionBuilder().with_url(url, options={"verify_ssl": False}).build()
        print("SignalR client initialized with URL:", url)

    def start(self):
        self.connection.start()
        print("Mock start of SignalR connection")

    def send_message(self, message):
        self.connection.send("SendMessageToAll", [message])
        print("Mock send message:", message)

signalr_client = SignalRClient(SIGNAL_R_URL)
signalr_client.start()