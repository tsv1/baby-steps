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


### Custom Steps

```python
from baby_steps import Step

class AndThen(Step):
    pass

and_then = AndThen()

with and_then("smth"):
    pass
```
