from types import TracebackType
from typing import Optional, Type


class Context:
    def __enter__(self) -> None:
        pass

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> bool:
        pass

    def __call__(self, name: str) -> "Context":
        return self


class Given(Context):
    pass


class When(Context):
    pass


class Then(Context):
    pass


given = Given()
when = When()
then = Then()


__all__ = ("given", "when", "then", "Context",)
__version__ = "0.1.0"
