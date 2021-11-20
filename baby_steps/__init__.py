from types import TracebackType
from typing import Optional, Type


class Step:
    def __enter__(self) -> None:
        pass

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> bool:
        pass

    def __call__(self, name: str) -> "Step":
        return self


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
__version__ = "1.0.2"
