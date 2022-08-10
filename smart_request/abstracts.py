from abc import ABCMeta, abstractmethod
from .exceptions import ObserverDerivationError

class AbsSubject(metaclass=ABCMeta):
    _observer = set()
    _observer.clear()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise ObserverDerivationError
        self._observer |= {observer}

    def detach(self, observer):
        self._observer -= {observer}

    def notify(self, value=None):
        for observer in self._observer:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    def __enter__(self):
        return self

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        pass

class AbsObserver(metaclass=ABCMeta):
    @abstractmethod
    def update(self, value):
        pass

    def send_request(request):
        pass

    def __enter__(self):
        return self

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        pass
