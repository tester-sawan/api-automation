import requests
delete_api = '/Library/DeleteBook.php'
base_uri = 'http://216.10.245.166'
delete_payload = {"ID":'sawan227'}
response = requests.delete(base_uri+delete_api,json=delete_payload)
response_data = response.json()
print(response_data)
print(response.status_code)