import requests
base_uri = 'http://216.10.245.166'
add_book_api = '/Library/Addbook.php'
get_book_api = '/Library/GetBook.php?AuthorName=Sawan Kumar'
get_book_api_id = '/Library/GetBook.php'
payload = {
"name":"Learn Appium Automation with Python",
"isbn":"sawan",
"aisle":"227",
"author":"Sawan Kumar"
}
payload1 = {"ID":"sawan227"}

# response = requests.post(base_uri+add_book_api,json=payload,)
# response_data = response.json()
# print(response_data)
response = requests.get(base_uri+get_book_api)
response_data = response.json()
print(response_data)
# Get book based on id:
response1 = requests.get(base_uri+get_book_api_id,params=payload1,)
response_data1 = response1.json()
print(response_data1)