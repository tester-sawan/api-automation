# Parse JSON string with nested objects (API-style)
import json
json_string = '''
{
  "status": "success",
  "data": {
    "token": "abc123",
    "expires_in": 3600
  }
}
'''
response_data = json.loads(json_string)
# get the expires_in data from response_data
for data in response_data:
    if data == "data":
        for item  in response_data[data]:
            if item == "expires_in":
                print(f"The value showing for 'expires_in' is: {response_data[data][item]}")
                break
        else:
            print("Requested keys not found.")
print("Program ended!!")