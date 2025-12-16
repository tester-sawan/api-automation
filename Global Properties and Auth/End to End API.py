import requests
import configparser
from pathlib import Path
from utilities import payloads
from utilities import headers

config = configparser.ConfigParser()

# Correct absolute-safe path
config_path = Path(__file__).parents[1] / "utilities" / "configurations.ini"
config.read(config_path)

print("Loaded sections:", config.sections())  # should print ['API']

add_book_api = "/Library/Addbook.php"
delete_book_api = "/Library/DeleteBook.php"

response_data = requests.post(
    config["API"]["endpoint"] + add_book_api,
    json=payloads.addbook("8564"),
    headers=headers.addbook_header
)

data = response_data.json()

if data['Msg'] == "Book Already Exists":
    ID = data['ID']
    print("Duplicate book found")
    print("Start delete book*************")
    response2 = requests.post(config['API']['endpoint'] + delete_book_api, json=payloads.deletebook(ID),headers=headers.addbook_header,)
    data2 = response2.json()
    print(data2)
elif data['Msg']=="successfully added":
    ID = data['ID']
    print(f"New Book has been created having id {ID}")
    print(data)

