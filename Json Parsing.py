# Parse the json string  in python.
# Sample JSON string is: json_string = '{"name": "Sawan", "role": "QA", "experience": 3}'
# json module is used to parse the json string and convert it into python object like dict/list
import json
json_string = '{"name": "Sawan", "role": "QA", "experience": 3}'
print(type(json_string))
response_data = json.loads(json_string)
print(response_data)
print(type(response_data))
# Accessing values after parsing using dictionary() methods.
print(response_data["name"])#This will return the value for the key:name
print(response_data.get("experience"))# Using get() method.
# Check all keys in dictionaries using keys() method.
print(response_data.keys())
# Check all values of the dictionaries using values()
print(response_data.values())
# Get all items using items()
print(response_data.items())