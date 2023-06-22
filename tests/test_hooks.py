import sys
from typing import Any
from unittest.mock import MagicMock, Mock, call

import pytest
from pytest import raises

from baby_steps import given
from baby_steps.hooks import _hooks, add_hook, del_hook


@pytest.fixture(autouse=True)
def empty_hooks():
    while len(_hooks) > 0:
        _hooks.pop()


def create_mock_hook(return_value: Any = None) -> MagicMock:
    mock = MagicMock(__exit__=Mock(side_effect=(return_value,)))

    def hook(step, name):
        with mock:
            yield

    add_hook(hook)

    return mock


def get_mock_last_call(mock: Mock):
    if sys.version_info >= (3, 8):
        return mock.mock_calls[-1].args[-1]
    return MagicMock(__eq__=Mock(return_value=True))


def test_hook_step():
    hook_ = Mock()
    add_hook(hook_)

    with given:
        pass

    assert hook_.mock_calls == [
        call(given.__class__, None)
    ]


async def test_hook_async_step():
    hook_ = Mock()
    add_hook(hook_)

    async with given:
        pass

    assert hook_.mock_calls == [
        call(given.__class__, None)
    ]


def test_hook_step_with_name():
    hook_ = Mock()
    add_hook(hook_)

    with given("smth"):
        pass

    assert hook_.mock_calls == [
        call(given.__class__, "smth")
    ]


def test_hook_del():
    hook1_, hook2_ = Mock(), Mock()
    add_hook(hook1_)
    add_hook(hook2_)
    del_hook(hook1_)

    with given:
        pass

    assert hook1_.mock_calls == []
    assert hook2_.mock_calls == [
        call(given.__class__, None)
    ]


def test_multiple_hooks():
    manager_ = Mock()
    manager_.hook1 = Mock()
    manager_.hook2 = Mock()

    add_hook(manager_.hook1)
    add_hook(manager_.hook2)

    with given:
        manager_.step()

    assert manager_.mock_calls == [
        call.hook1(given.__class__, None),
        call.hook2(given.__class__, None),
        call.step(),
    ]


def test_cm_hook_before_after():
    mock = create_mock_hook()

    with given:
        mock.step()

    assert mock.mock_calls == [
        call.__enter__(),
        call.step(),
        call.__exit__(None, None, None),
    ]


def test_cm_error_hook_before_after():
    mock = create_mock_hook()
    exception = AssertionError()

    with raises(Exception) as exc_info:
        with given:
            mock.step()
            raise exception

    assert exc_info.value == exception
    assert mock.mock_calls == [
        call.__enter__(),
        call.step(),
        call.__exit__(type(exception), exception, get_mock_last_call(mock))
    ]


def test_cm_error_hook_before_after_suppress():
    mock = create_mock_hook(return_value=True)
    exception = AssertionError()

    with raises(Exception) as exc_info:
        with given:
            mock.step()
            raise exception

    assert exc_info.value == exception
    assert mock.mock_calls == [
        call.__enter__(),
        call.step(),
        call.__exit__(type(exception), exception, get_mock_last_call(mock))
    ]


def test_cm_error_hook_before_after_reraise():
    exception = AssertionError()
    mock = create_mock_hook(return_value=exception)

    with raises(Exception) as exc_info:
        with given:
            mock.step()
            raise exception

    assert exc_info.value == exception
    assert mock.mock_calls == [
        call.__enter__(),
        call.step(),
        call.__exit__(type(exception), exception, get_mock_last_call(mock))
    ]


@pytest.mark.parametrize("raise_exc", [ValueError(), AssertionError()])
def test_cm_error_hook_before_after_raise(raise_exc: Exception):
    mock = create_mock_hook(return_value=raise_exc)
    exception = AssertionError()

    with raises(Exception) as exc_info:
        with given:
            mock.step()
            raise exception

    assert exc_info.value == raise_exc
    assert mock.mock_calls == [
        call.__enter__(),
        call.step(),
        call.__exit__(type(exception), exception, get_mock_last_call(mock))
    ]


def test_multiple_hooks_before_after():
    manager_ = Mock()

    def hook1(step, name):
        manager_.hook1_before(step, name)
        yield
        manager_.hook1_after(step, name)

    def hook2(step, name):
        manager_.hook2_before(step, name)
        yield
        manager_.hook2_after(step, name)

    add_hook(hook1)
    add_hook(hook2)

    with given:
        manager_.step()

    assert manager_.mock_calls == [
        call.hook1_before(given.__class__, None),
        call.hook2_before(given.__class__, None),
        call.step(),
        call.hook2_after(given.__class__, None),
        call.hook1_after(given.__class__, None),
    ]
