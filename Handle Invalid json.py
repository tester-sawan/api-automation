import json

try:
    data = json.loads(json_string)
except json.JSONDecodeError as e:
    print("Invalid JSON:", e)
