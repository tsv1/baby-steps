from types import TracebackType
from typing import Optional, Type, Union

from .hooks import _hooks

__all__ = ("Step",)


class Step:
    def __init__(self) -> None:
        self._name: Union[str, None] = None

    def __enter__(self) -> None:
        for hook in _hooks:
            hook(self.__class__, self._name)

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> bool:
        self._name = None
        return exc_type is None

    def __call__(self, name: str) -> "Step":
        self._name = name
        return self
