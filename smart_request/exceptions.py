from .config import CLASS_NAME_STARTS_WITH

class ObserverDerivationError(Exception):
    def __init__(self):
        self.message = "Observer not derived from AbsObserver"
        super().__init__(self.message)

    def __str__(self):
        return self.message


class AccountNameTypeError(Exception):
    def __init__(self):
        self.message = "Class Name is not of " + CLASS_NAME_STARTS_WITH + "+[int] Type"
        super().__init__(self.message)

    def __str__(self):
        return self.message
