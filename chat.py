# chatpdf_client.py
import os
import requests
from dotenv import load_dotenv

class ChatPDFClient:
    def __init__(self):
        load_dotenv()  
        self.api_key = os.getenv('API_KEY')
        self.source_id = os.getenv('SOURCE_ID')
        self.headers = {
            'x-api-key': self.api_key,
            "Content-Type": "application/json",
        }
        self.base_url = 'https://api.chatpdf.com/v1/chats/message'
    
    def send_message(self, message_content):
        data = {
            'sourceId': self.source_id,
            'messages': [
                {
                    'role': "user",
                    'content': message_content,
                }
            ]
        }
        
        response = requests.post(self.base_url, headers=self.headers, json=data)
        return response

    def get_response(self, message_content):
        response = self.send_message(message_content)
        if response.status_code == 200:
            return 'Result:', response.json()['content']
        else:
            return 'Status:', response.status_code, 'Error:', response.text
