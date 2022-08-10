from .manager import AccountManager, DisposableList

class DefaultAMContext:
    def __init__(self, func):
        self._func = func
        self.count = int()

    def __call__(self):
        with AccountManager() as manager:
            with DisposableList(manager.call_observers()):
                self._func(manager)
                self.count = manager.current_request


class AMContext:
    def __init__(self, start):
        self._count = int()
        self.start = start

    def __call__(self, func):
        def wrapper():
            with AccountManager(self.start) as manager:
                with DisposableList(manager.call_observers()):
                    func(manager)
                    self._count = manager.current_request
        return wrapper

    @property
    def count(self):
        return self._count - self.start

    @property
    def total_count(self):
        return self._count
