import requests
import configparser
import os
from utilities import payloads,headers
config = configparser.ConfigParser()
# This refers the current working directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# This will join the working and utilities.
config_dir = os.path.join(base_dir,'utilities/configurations.ini')
data=config.read(config_dir)
url = (config['API']['endpoint'])+(config['ADD BOOK']['add_api'])
print(url)
response = requests.post(url,json=payloads.addbook("74321"),headers=headers.addbook_header,)
server_response = response.json()
print(server_response)