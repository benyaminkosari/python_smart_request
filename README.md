

Python Smart Request
===============
Have you ever tried to spread your requests' traffic equally through
multiple accounts? This app is nicely designed for this specific purpose.


Getting Started
====

Download the source code or clone it using this command:

    git clone https://github.com/benyaminkosari/python_smart_request.git

* make sure to update `accounts.py` and `config.py` files according to your needs.



Usage
====

### Directly by its context manager:
```python
from smart_request.manager import AccountManager, DisposableList

with AccountManager() as manager:
    with DisposableList(manager.call_observers()):
        for _ in range(5):
            manager.send_request()
```

### Using decorators:

  - without specifying requests' starting point:
```python
from smart_request.decorators import DefaultAMContext

@DefaultAMContext
def call(*manager):
    for _ in range(5):
        manager[0].send_request()

call()
print("Request count:", call.count)
```

  - pass and save request count for later use:
```python
from smart_request.decorators import AMContext

start = 3
amc_decorator = AMContext(start)

@amc_decorator
def call(*manager):
    for _ in range(5):
        manager[0].send_request()

call()
print("This Context:", amc_decorator.count)
print("Total:", amc_decorator.total_count)
```

How does it work?
====
This app is designed using the power of Observer(dependent) design pattern to create a
many to one relationship between the accounts and their manager class.

<p align="center">
  <img src="/pattern-uml.png">
</p>
