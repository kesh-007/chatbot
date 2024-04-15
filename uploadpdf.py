import os
import requests
from dotenv import load_dotenv
load_dotenv()  

api_key = os.getenv('API_KEY')

headers = {
  'x-api-key': api_key,
  'Content-Type': 'application/json'
}
data = {'url': 'https://nida.nih.gov/sites/default/files/podat_1.pdf'}

response = requests.post(
    'https://api.chatpdf.com/v1/sources/add-url', headers=headers, json=data)

if response.status_code == 200:
    print('Source ID:', response.json()['sourceId'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)



