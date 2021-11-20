import unittest

from baby_steps import Step, given, then, when


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
