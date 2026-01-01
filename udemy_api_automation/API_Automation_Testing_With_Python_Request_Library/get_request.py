import requests
base_uri = 'http://216.10.245.166'
get_book_api = '/Library/GetBook.php?AuthorName=rahulshetty'
response = requests.get(base_uri+get_book_api)
response_data = response.json() # This will return the json data.
for data in response_data:
    print(data)
print("************************************************************************")
#print(response_data)
# Get method accepts parameters in dictionary format.
response = requests.get(base_uri+'/Library/GetBook.php',params={"AuthorName":"rahulshetty"},)
response_data = response.json()
for data in response_data:
    print(data)
# response.status_code >> will return the status code received from the server.
print(f"Received Status code is: {response.status_code}")
assert response.status_code == 200
# response.headers >> will return the headers information received from the server.
header_info = response.headers
for header in header_info:
    print(header_info[header],':',header)
# Check whether the content type is application/json;charset=UTF-8
assert header_info['Content-Type'] == 'application/json;charset=UTF-8', "Expected Mismatched."
# response.cookies >> will return the cookies information from the server.
#print(response.cookies)
# Get the book information whose isbn no is 'RS180'
for _data in response_data:
     if _data['isbn'] == "9473031":
        print(_data)
        break