import json
with open("sample json.txt","rt") as file:
    #read_file = file.read()
    _response = json.load(file)
    print(_response, type(_response))
# Extract users information from  the json.
_users = _response["users"]
print(_users)
print("Total no of items are:", len(_users))
# Run a loop and check for name: "Ravi" and if found extract the details.
get_filter_item = []
for data in range(len(_users)):
    if _users[data]["name"] =="Ravi":
        print("User found")
        get_filter_item.append(_users[data])
        print(f"Details extracted: {get_filter_item}")
        break
else:
    print("Name 'Ravi' not exist in Users.")

