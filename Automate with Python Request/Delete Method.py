import  requests
base_url = "http://216.10.245.166"
delete_api = "/Library/DeleteBook.php"
_header = {"Content-Type":"application/json"}
response = requests.post(base_url+delete_api,json={
    "ID":"ooo569"},headers=_header,)
data = response.json()
print(data)
