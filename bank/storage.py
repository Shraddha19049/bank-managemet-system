import json
import os
from account import Account


class Storage:
    def __init__(self):
        self.file_name = os.path.join(os.path.dirname(__file__), "accounts.json")

    def load_accounts(self):
        if not os.path.exists(self.file_name):
            return []

        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                if os.path.getsize(self.file_name) == 0:
                    return []
                data = json.load(file)
        except (OSError, json.JSONDecodeError, ValueError):
            return []

        if not isinstance(data, list):
            return []

        accounts = []
        for account_data in data:
            if not isinstance(account_data, dict):
                continue
            account = Account.from_dict(account_data)
            accounts.append(account)
        return accounts

    def save_accounts(self, accounts):
        data = []
        for account in accounts:
            data.append(account.to_dict())
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)