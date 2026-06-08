class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        self.__account_number = "123456"

import json

data = {
    "name": "Safana",
    "balance": 1000
}

with open("accounts.json", "w") as file:
    json.dump(data, file, indent=4)

import json

with open("accounts.json", "r") as file:
    data = json.load(file)

print(data)

try:
    with open("accounts.json", "r") as file:
        data = json.load(file)

except FileNotFoundError:
    print("File not found")

except json.JSONDecodeError:
    print("Invalid JSON")