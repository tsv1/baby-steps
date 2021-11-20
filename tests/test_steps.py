import unittest
from unittest.mock import Mock, call

from baby_steps import Step, given, then, when
from baby_steps.hooks import add_hook, del_hook


class TestSteps(unittest.TestCase):
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
        mock = Mock()
        add_hook(mock)

        with given:
            pass

        assert mock.mock_calls == [
            call(given.__class__, None)
        ]

    def test_hook_step_with_name(self):
        mock = Mock()
        add_hook(mock)

        with given("smth"):
            pass

        assert mock.mock_calls == [
            call(given.__class__, "smth")
        ]

    def test_hook_del(self):
        mock1, mock2 = Mock(), Mock()
        add_hook(mock1)
        add_hook(mock2)
        del_hook(mock1)

        with given:
            pass

        assert mock1.mock_calls == []
        assert mock2.mock_calls == [
            call(given.__class__, None)
        ]
