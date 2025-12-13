import json
with open("sample json.txt") as file1:
    data1 = json.load(file1)
with open("sample json2.txt") as file2:
    data2 = json.load(file2)
# User assert for validation
# assert data1==data2
if data1 == data2:
    print("Both the json file has same data.")
else:
    print("Data Mismatched.")
