from baby_steps import Step, given, then, when


def test_given():
    with given:
        pass


async def test_async_given():
    async with given:
        pass


def test_given_with_name():
    with given("smth"):
        pass


async def test_async_given_with_name():
    async with given("smth"):
        pass


def test_when():
    with when:
        pass


def test_when_with_name():
    with when("smth"):
        pass


def test_then():
    with then:
        pass


def test_then_with_name():
    with then("smth"):
        pass


def test_custom_step():
    class AndThen(Step):
        pass
    and_then = AndThen()
    with and_then:
        pass


async def test_custom_async_step():
    class AndThen(Step):
        pass
    and_then = AndThen()
    async with and_then:
        pass
