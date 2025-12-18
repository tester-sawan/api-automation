import requests
import configparser
import  os
config = configparser.ConfigParser()
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
config_dir = os.path.join(base_dir,'Simple Grocery App /utilities1/configuration.ini')
config.read(config_dir)
# For Testing purpose
print("Configuration Path:", config_dir) # Returns the directory path
print("File Exist:", os.path.exists(config_dir)) # Check whether file exists or not
server_response = requests.get(config['API']['base_uri']+config['Get Status']['get_status'])
response = server_response.json()
print(response)
get_status_code = server_response.status_code
if get_status_code == 200:
    print("Test Passed! Server is Active.")
    if response['status'] == 'UP':
        print("Response Validation Passed.")
elif get_status_code != 200:
    print("Test Failed! Received status code is:",get_status_code)
else:
    print("Some Unkownn Error Found.")