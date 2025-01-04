import re
from .abstracts import AbsObserver
from .exceptions import AccountNameTypeError
from .config import CLASS_NAME_STARTS_WITH, TOTAL_ACCOUNTS

class AccountsBase(AbsObserver):
    _current_request = int()
    account_number = int()
    sending_accounts = list()

    def __new__(cls, self):
        ends_with_digit = re.search(r'\d+$', cls.__name__)
        if not cls.__name__.startswith(CLASS_NAME_STARTS_WITH) or ends_with_digit is None:
            raise AccountNameTypeError
        cls.account_number = int(ends_with_digit.group())
        return super(AccountsBase, cls).__new__(cls)

    def __init__(self, myobservers):
        self._myobservers = myobservers
        self._myobservers.attach(self)

    def update(self):
        self._current_request = self._myobservers.current_request
        if self.is_my_turn():
            if self.is_available():
                self.sending_accounts.append(self.account_number)
                self.pre_request()
                self.send_request()
                self.post_request()
                self.sending_accounts.remove(self.account_number)
            else:
                print("Error - account already in use!")

    def choose_proper_account(self):
        n = 0
        while (self._current_request - (n * TOTAL_ACCOUNTS)) > 0:
            n += 1
        return self._current_request - ((n-1) * TOTAL_ACCOUNTS)

    def is_my_turn(self):
        which_account = self.choose_proper_account()
        if self.account_number == which_account:
            return True
        return False

    def is_available(self):
        if self.account_number in self.sending_accounts:
            return False
        return True

    def __exit__(self, exc_type, exc_value, traceback):
        self._myobservers.detach(self)
