import  json
json_string = '''
{
  "users": [
    {"id": 1, "name": "Amit"},
    {"id": 2, "name": "Ravi"}
  ]
}
'''
response_data = json.loads(json_string)
# print(response_data)
# get the id from users data where name is 'Ravi'
print(response_data["users"][1]["id"])
# using for loop
for id in response_data["users"]:
    if id["name"] == "Ravi":
        print(f"The id fetched from users for name: 'Ravi' is: {id['id']}")
        break
else:
        print("Name not found")
print("Program has ended.")