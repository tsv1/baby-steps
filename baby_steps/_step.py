from types import GeneratorType, TracebackType
from typing import List, Optional, Type, Union

from .hooks import _hooks

__all__ = ("Step",)


class Step:
    def __init__(self) -> None:
        self._name: Union[str, None] = None
        self._stack: List[GeneratorType] = []

    def __enter__(self) -> None:
        for hook in _hooks:
            maybe_gen = hook(self.__class__, self._name)
            if isinstance(maybe_gen, GeneratorType):
                next(maybe_gen)
                self._stack.append(maybe_gen)

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> bool:
        while len(self._stack) > 0:
            gen = self._stack.pop()
            if exc_type is None:
                try:
                    next(gen)
                except StopIteration:
                    pass
            else:
                try:
                    gen.throw(exc_type, exc_val, exc_tb)
                except StopIteration:
                    pass
                except BaseException as e:
                    if e is not exc_val:
                        raise

        self._name = None
        self._stack = []

        return exc_type is None

    def __call__(self, name: str) -> "Step":
        self._name = name
        return self
