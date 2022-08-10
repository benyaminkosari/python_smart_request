import re, inspect, importlib
from .abstracts import AbsSubject
from .config import CLASS_NAME_STARTS_WITH

class AccountManager(AbsSubject):
    def __init__(self, start=0):
        self._current_request = start

    @property
    def current_request(self):
        return self._current_request

    def set_current_request(self):
        self._current_request += 1
        self.notify()

    def send_request(self):
        self.set_current_request()

    def __exit__(self, exc_type, exc_value, traceback):
        self._observer.clear()

    def call_observers(self):
        objects = list()
        main_module, modules = self.get_modules("smart_request.accounts")
        for class_ in modules:
            if self.check_name_type(class_):
                objects.append(getattr(main_module, class_[0])(self))
        return objects

    @staticmethod
    def get_modules(file_name):
        main_module = importlib.import_module(file_name)
        modules = inspect.getmembers(main_module, inspect.isclass)
        return main_module, modules

    @staticmethod
    def check_name_type(class_):
        ends_with_digit = re.search(r'\d+$', class_[0])
        if class_[0].startswith(CLASS_NAME_STARTS_WITH) and ends_with_digit is not None:
            return True
        return False


class DisposableList(list):
    def __enter__(self):
        for v in self:
            v.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        for v in self:
            v.__exit__(exc_type, exc_value, traceback)
