# Baby Steps

## Installation

```sh
pip3 install baby-steps
```

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
