import json
import asyncio

class BankAccount:
    FILE_NAME = "accounts.json"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
            return

        self._balance -= amount

    def get_balance(self):
        return self._balance

    async def save(self):
        data = {
            "owner": self.owner,
            "balance": self._balance
        }

        await asyncio.sleep(1)

        with open(self.FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    @classmethod
    async def load(cls):
        try:
            await asyncio.sleep(1)

            with open(cls.FILE_NAME, "r") as file:
                data = json.load(file)

            return cls(
                data["owner"],
                data["balance"]
            )

        except FileNotFoundError:
            return None


async def main():
    account = BankAccount("Safana", 5000)

    account.deposit(1000)

    await account.save()

    loaded = await BankAccount.load()

    print(
        loaded.owner,
        loaded.get_balance()
    )

asyncio.run(main())