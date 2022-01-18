import sys
import unittest
from types import TracebackType
from unittest.mock import Mock, call, MagicMock

from baby_steps import Step, given, then, when
from baby_steps.hooks import _hooks, add_hook, del_hook


class TestSteps(unittest.TestCase):
    def setUp(self) -> None:
        while len(_hooks) > 0:
            _hooks.pop()

    def test_given(self):
        with given:
            pass

    def test_given_with_name(self):
        with given("smth"):
            pass

    def test_when(self):
        with when:
            pass

    def test_when_with_name(self):
        with when("smth"):
            pass

    def test_then(self):
        with then:
            pass

    def test_then_with_name(self):
        with then("smth"):
            pass

    def test_custom_step(self):
        class AndThen(Step):
            pass
        and_then = AndThen()
        with and_then:
            pass

    def test_hook_step(self):
        hook_ = Mock()
        add_hook(hook_)

        with given:
            pass

        assert hook_.mock_calls == [
            call(given.__class__, None)
        ]

    def test_hook_step_with_name(self):
        hook_ = Mock()
        add_hook(hook_)

        with given("smth"):
            pass

        assert hook_.mock_calls == [
            call(given.__class__, "smth")
        ]

    def test_hook_del(self):
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

    def test_multiple_hooks(self):
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

    def test_cm_hook_before_after(self):
        mock_ = MagicMock()

        def hook(step, name):
            with mock_(step, name):
                yield

        add_hook(hook)

        with given:
            mock_.step()

        assert mock_.mock_calls == [
            call(given.__class__, None),
            call().__enter__(),
            call.step(),
            call().__exit__(None, None, None),
        ]

    def test_cm_error_hook_before_after(self):
        mock_ = MagicMock()

        def hook(step, name):
            with mock_(step, name):
                yield

        add_hook(hook)

        exception = AssertionError()
        with self.assertRaises(type(exception)):
            with given:
                mock_.step()
                raise exception

        assert mock_.mock_calls[:-1] == [
            call(given.__class__, None),
            call().__enter__(),
            call.step(),
        ]
        if sys.version_info >= (3, 8):
            last_call = mock_.mock_calls[-1]
            assert last_call.args[0] == type(exception)
            assert last_call.args[1] == exception
            assert isinstance(last_call.args[2], TracebackType)

    def test_multiple_hooks_before_after(self):
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
