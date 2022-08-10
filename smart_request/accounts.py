from .account_base import AccountsBase

class Account1(AccountsBase):
    username = "username"
    password = "password"

    def send_request(self):
        print("account 1 -> request sent!")


class Account2(AccountsBase):
    username = "username"
    password = "password"

    def send_request(self):
        print("account 2 -> request sent!")

class Account3(AccountsBase):
    username = "username"
    password = "password"

    def send_request(self):
        print("account 3 -> request sent!")


class Account4(AccountsBase):
    username = "username"
    password = "password"

    def send_request(self):
        print("account 4 -> request sent!")
