# Baby Steps

[![PyPI](https://img.shields.io/pypi/v/baby-steps.svg?style=flat-square)](https://pypi.python.org/pypi/baby-steps/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/baby-steps?style=flat-square)](https://pypi.python.org/pypi/baby-steps/)
[![Python Version](https://img.shields.io/pypi/pyversions/baby-steps.svg?style=flat-square)](https://pypi.python.org/pypi/baby-steps/)

BDD steps for test markup. Just for readability.

## Usage

```python
from unittest.mock import Mock, call, sentinel

from baby_steps import given, when, then


def test_smth():
    with given:
        value = sentinel.smth
        mock = Mock(return_value=value)

    with when:
        res = mock()

    with then:
        assert res == value
        assert mock.mock_calls == [call()]
```

## Installation

```sh
pip3 install baby-steps
```
