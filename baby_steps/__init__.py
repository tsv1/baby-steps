from ._step import Step


class Given(Step):
    pass


class When(Step):
    pass


class Then(Step):
    pass


given = Given()
when = When()
then = Then()

__all__ = ("given", "when", "then", "Step",)
__version__ = "1.2.1"
