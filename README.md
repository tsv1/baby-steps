# Baby Steps

[![PyPI](https://img.shields.io/pypi/v/baby-steps.svg?style=flat-square)](https://pypi.python.org/pypi/baby-steps/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/baby-steps?style=flat-square)](https://pypi.python.org/pypi/baby-steps/)
[![Python Version](https://img.shields.io/pypi/pyversions/baby-steps.svg?style=flat-square)](https://pypi.python.org/pypi/baby-steps/)

BDD steps for test markup. Just for readability.

## Installation

```sh
pip3 install baby-steps
```

## Usage

```python
import httpx
from baby_steps import given, when, then

def test_status_code():
    with given:
        code = 200

    with when:
        resp = httpx.get(f"https://httpbin.org/status/{code}")

    with then:
        assert resp.status_code == code
```

### Named Steps

```python
import httpx
from baby_steps import given, when, then

def test_status_code():
    with given("status code"):
        code = 200

    with when("user requests a resource"):
        resp = httpx.get(f"https://httpbin.org/status/{code}")

    with then("it should return expected status code"):
        assert resp.status_code == code
```

### Hooks

```python
from baby_steps import given, then, when
from baby_steps.hooks import add_hook

def test():
    with given("status code"):
        pass

    with when("user requests a resource"):
        pass

    with then("it should return expected status code"):
        pass


def hook(step, name):
    print(step, name)

add_hook(hook)
test()

# <class 'baby_steps.Given'> 'status code'
# <class 'baby_steps.When'> 'user requests a resource'
# <class 'baby_steps.Then'> 'it should return expected status code'
```

#### Advanced

```python
from baby_steps import when
from baby_steps.hooks import add_hook

def test():
    with when:
        print("when")


def hook(step, name):
    print("before", step)
    yield
    print("after", step)

add_hook(hook)
test()

# before <class 'baby_steps.When'>
# when
# after <class 'baby_steps.When'>
```

### Custom Steps

```python
from baby_steps import Step

class AndThen(Step):
    pass

and_then = AndThen()

with and_then("smth"):
    pass
```
