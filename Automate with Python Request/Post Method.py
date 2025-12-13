# Add a booklist using the post method. Verify the status code. capture the response and validate the response body.
import requests
base_url = "http://216.10.245.166"
add_book_api = "/Library/Addbook.php"
body_payload = {
"name":"Learn Appium Automation with Java",
"isbn":"abc",
"aisle":"963",
"author":"Sawan Kumar"
}
_header = {"Content-Type":"application/json"}

response = requests.post(base_url+add_book_api,json=body_payload,headers=_header,)
body=response.json()
#print(body)

if response.status_code == 200:
    if body["Msg"] == "successfully added":
        print("Test Passed")
    else:
        print("Test Failed")
        print(f"Received response is: {body} and the status code is: {response.status_code}")
print("Thank You !!!")
