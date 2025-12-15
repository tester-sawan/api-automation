import requests
import configparser
from pathlib import Path
from utilities import payloads
from utilities import headers

config = configparser.ConfigParser()

# Correct absolute-safe path
config_path = Path(__file__).parent[1] / "utilities" / "configurations.ini"
config.read(config_path)

print("Loaded sections:", config.sections())  # should print ['API']

add_book_api = "/Library/Addbook.php"

response_data = requests.post(
    config["API"]["endpoint"] + add_book_api,
    json=payloads.addbook("8564"),
    headers=headers.addbook_header
)

data = response_data.json()
print(data)
