# import requests module to access http methods.
import requests
# This will return a response so we need to store in a variable.
data = requests.get("http://216.10.245.166/Library/GetBook.php",
             params={"AuthorName":"rahul shetty2"},)
response = data.json() # Automatically convert the string into list/dictionary.
print(response)
# print(type(response))
# print(len(response))
# print(response[0]["book_name"])
print(f"Received status code is: {data.status_code}")
# print(data.headers) # This will return the headers revceived from the response as dictionary object.
if data.headers["Content-Type"] == "application/json;charset=UTF-8":
    print("Actual content type is same as expected.\n'Test Passed'")
else:
    print("Actual Content-Type not matched\n'Test Failed'")
get_search_book = {}
# Get the book details for isbn: 'KC201' from the response
for data in range(len(response)):
    if response[data]["isbn"] == "KC201":
        print("Item founded")
        get_search_book.update(response[data])
        break
else:
    print("Search item not found.")
print(get_search_book)

